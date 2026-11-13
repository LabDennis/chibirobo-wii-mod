"""Build the Chibi-Robo Wii mod from the decompilation in decomp/ (a git submodule).

Options go to the decomp's configure.py: --gcncon, --langpack <locale|global>, --iso, --fanpatch <folder>.
Place your own R24J01 disc in decomp/orig/R24J01 (and the GameCube discs for --langpack) first.
"""

import subprocess
import sys
from pathlib import Path

DECOMP = Path(__file__).resolve().parent / "decomp"


def main() -> None:
    subprocess.run([sys.executable, "configure.py", "--version", "R24J01", *sys.argv[1:]], cwd=DECOMP, check=True)
    subprocess.run(["ninja"], cwd=DECOMP, check=True)


if __name__ == "__main__":
    main()
