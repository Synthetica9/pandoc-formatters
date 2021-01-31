with import (builtins.fetchTarball
  "https://github.com/nixos/nixpkgs/archive/8dd2e6d7198e7420dd80913594bae449ec099401.tar.gz")
  { };
let ourPy = python3.withPackages (p: with p; [ panflute ]);
in mkShell { buildInputs = [ ourPy ]; }
