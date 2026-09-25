{
  description = "Project Elysian: tools for agent-built stories (linter, ebook builder, validators)";

  # git+https (shallow) instead of github: so no GitHub API is needed (the cloud sandbox only allows git reads).
  inputs.nixpkgs.url = "git+https://github.com/NixOS/nixpkgs?ref=nixos-24.11&shallow=1";

  outputs = { self, nixpkgs }:
    let
      systems = [ "x86_64-linux" "aarch64-linux" "x86_64-darwin" "aarch64-darwin" ];
      forAll = f: nixpkgs.lib.genAttrs systems (system: f nixpkgs.legacyPackages.${system});
    in {
      devShells = forAll (pkgs: {
        default = pkgs.mkShell {
          packages = [
            pkgs.python3     # tools/tells.py, tools/build_ebook.py (stdlib only)
            pkgs.epubcheck   # validates built EPUBs: epubcheck library/<book>.epub
            pkgs.zip
            pkgs.gawk        # models/*.awk
          ];
          shellHook = ''
            echo "Project Elysian tools: python3, epubcheck, zip, gawk. See AGENTS.md."
          '';
        };
      });
    };
}
