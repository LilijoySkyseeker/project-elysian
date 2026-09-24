# DOC-10 / DOC-02B age structure of the Sol population at NOW — cohort survival model
# Usage: awk [-v NOW=550 -v H=0.0025 -v HW=0.01 -v BSPREAD=0.021 -v BNOW=0.0065] -f age_structure.awk
#
# Births follow the D-53 curve: ~320 Written by AF 30 (early hazard HW, D-39); the Spread
# (AF 44-236) at a child per Cluster every ~6 yr (BSPREAD = 1/(6*8) of population per year,
# net ~1.9 %/yr, 320 -> 15,000); after AF 236 net +0.4 %/yr (D-53), so births BNOW = 0.004 + H.
# Everyone born after AF 30 dies at the canonical hazard H (0.25 %/yr, DOC-02B §8).
# Ark exports (~7,200, D-52/D-53) are a cross-section of ages and are ignored for *structure*;
# the absolute total is scaled to the D-53 Sol figure at the end.
BEGIN{
  if(NOW=="")NOW=550; if(H=="")H=0.0025; if(HW=="")HW=0.01
  if(BSPREAD=="")BSPREAD=0.021; if(BNOW=="")BNOW=0.004+H
  # Written: 320 born 0-30; early hazard HW (D-39) for the first century, canonical H after.
  # (HW for life would leave ~1 of 320; HW to AF 100 then H leaves ~40 — the D-50 figure.)
  written=320*exp(-HW*(100-15))*exp(-H*(NOW-100))
  pop=320; total=written; sat150=0; sat250=0; old314=0
  for(t=31;t<=NOW;t++){
    b = (t<=236) ? BSPREAD*pop : BNOW*pop
    surv = b*exp(-H*(NOW-t)); age=NOW-t
    alive[age]=surv; total+=surv
    if(age>=150)sat150+=surv; if(age>=250)sat250+=surv; if(age>=314)old314+=surv
    pop += b - H*pop
  }
  # median age
  cum=0; for(a=0;a<=NOW;a++){cum+=alive[a]; if(cum>=total/2 && med==""){med=a}}
  # mean age
  for(a=0;a<=NOW;a++){s+=a*alive[a]}; mean=s/total
  printf "NOW=AF %d  hazard %.2f%%/yr  Written alive ~%d (of 320)\n", NOW, H*100, written
  printf "model total (pre-export) %.0f ; D-53 Sol figure 45,000 -> scale %.2f\n", total, 45000/total
  printf "median age of a living Kin  : %d yr\n", med
  printf "mean age                    : %.0f yr\n", mean
  printf "aged >=150 (index filling)  : %.0f%%\n", 100*sat150/total
  printf "aged >=250 (past saturation): %.0f%%\n", 100*sat250/total
  printf "Spread-born (>=314, AF<=236): %.0f%%  (~%.0f Kin after export scaling)\n", 100*old314/total, old314*45000/total
  printf "implied births/yr now       : %.0f  = one compile per Cluster of 8 every %.0f yr\n", BNOW*pop, 1/(BNOW*8)
}
