# DOC-01E.2 integrated vacuum budget — lumped thermal + compartment O2 + acidosis
# Usage: awk -v SCEN=<name> [-v M=60 -v KA= -v KB= -v ALB=1 -v TB= -v LOCK=] -f vacuum_budget.awk
# Scenarios: shadow_eva shadow_drift sun_eva sun_drift worst_sun_eva
#
# M is the reference individual mass in kg (canon 60, D-68). Every term below scales
# from the 50 kg derivation of DOC-01E.1 by its own exponent:
#   stores, heat capacity, acid buffer, locomotor draw ~ M^1.00
#   radiating/absorbing surfaces (ears, pelt, solar)     ~ M^0.67
#   torpor (basal) draw                                  ~ M^0.75   (Kleiber)
# Because the State-A pool and the State-A draw share the M^1.00 exponent, the
# 17-minute envelope is mass-invariant by construction.
function ear(T,open){ return open ? EARMAX*(T/310.15)^4 : EARMIN }
function pelt(T,k){ return k*(T-183)/(310.65-183) }
function torp(T){ return TB*2.5^((T-310.65)/10) }
BEGIN{
  if(M=="")M=60
  S1=M/50; S23=exp(2*log(S1)/3); S75=exp(0.75*log(S1))
  if(KA=="")KA=70*S23; if(KB=="")KB=25*S23; if(ALB=="")ALB=1
  if(TB=="")TB=3.0*S75; if(LOCK=="")LOCK=1.5*S1
  EARMAX=71.2*S23; EARMIN=5.0*S23
  C=3470*M; dt=10; T=310.65; t=0
  poolA=6.0*S1-LOCK+0.29*S1+1.27*S1; mb=1.33*S1+LOCK; anaer=37000*S1
  P_FULL=120*S1; P_CRAWL=25*S1
  sun=(SCEN ~ /sun/); worst=(SCEN ~ /worst/); drift=(SCEN ~ /drift/)
  mode= drift ? "TORPOR" : "FULL"
  printf "== %s  M=%gkg (KA=%.1f KB=%.1f ALB=%s TB=%.2fW LOCK=%.2fL poolA=%.2fL Mb=%.2fL)\n", SCEN, M, KA, KB, ALB, TB, LOCK, poolA, mb
  printf "%8s %7s %7s %7s %6s  %s\n","t(min)","T(C)","poolA","Mb","P_met","event"
  log_(t,T,"start "mode)
  Tmax=T; Tmin=T
  while(t<48*3600){
    if(mode=="FULL"){P=P_FULL;k=KA} else if(mode=="CRAWL"){P=P_CRAWL;k=KA} else {P=torp(T);k=KB}
    # ear controller
    if(mode=="TORPOR") open=(T>300.15); else if(mode=="CRAWL") open=1; else open=(T>310.65)
    if(worst){ loss=EARMAX; gain=142.9*S23 }
    else if(!sun){ loss=ear(T,open)+pelt(T,k); gain=0 }
    else {
      inward = ALB ? 5*S23 : 10*S23
      if(mode=="TORPOR"){ bare=57*S23 } else { bare=20*S23 }
      loss=ear(T,open)+0.5*pelt(T,k); gain=bare+inward
    }
    dT=(P+gain-loss)/C*dt; T+=dT; t+=dt
    if(T>Tmax)Tmax=T; if(T<Tmin)Tmin=T
    # O2 / acid accounting
    if(mode=="FULL"){ poolA-=P/20100*dt; if(poolA<=0){poolA=0; mode="CRAWL"; log_(t,T,"State A pool spent -> CRAWL-HOME (anaerobic)")} }
    else if(mode=="CRAWL"){ anaer-=P*dt; if(anaer<=0){mode="TORPOR"; log_(t,T,"acid buffer spent -> STATE B torpor")} }
    else { need=P/20100*dt; if(poolA>0){poolA-=need; if(poolA<0){mb+=poolA;poolA=0}} else mb-=need
           if(mb<=0){log_(t,T,"ANOXIA — Mb reserve exhausted"); break} }
    if(mode!="TORPOR" && T>=312.65){mode="TORPOR"; log_(t,T,"THERMAL LIMIT +2K -> forced STATE B")}
    if(T>=315.15){log_(t,T,"HEAT DEATH 42C"); break}
    if(T<=278.15){log_(t,T,"COLD DEATH 5C"); break}
    if(mode=="TORPOR" && !cool && T<=300.15){cool=1; log_(t,T,"torpor cooled to 27C setpoint, ears fold")}
    if(!des && t>=12*3600){des=1; log_(t,T,"12 h canon desiccation ceiling (DOC-01E)")}
    if(!h24 && t>=24*3600){h24=1; log_(t,T,"24 h mark")}
  }
  if(t>=48*3600) log_(t,T,"48 h cap — still viable")
  printf "   Tmin=%.1fC Tmax=%.1fC\n\n",Tmin-273.15,Tmax-273.15
}
function log_(t,T,msg){ printf "%8.1f %7.2f %7.2f %7.2f %6.1f  %s\n",t/60,T-273.15,poolA,mb,P,msg }
