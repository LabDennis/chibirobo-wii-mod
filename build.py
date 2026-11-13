"""Build the Chibi-Robo Wii mod: the clean decomp in decomp/ (a git submodule) plus patches/*.patch.

The patched copy is a git worktree of the submodule's commit at build/decomp. Options go to its
configure.py: --gcncon, --langpack <locale|global>, --iso, --fanpatch <folder>. Put your own discs
into decomp/orig/<ID>/ first (R24J01, and GGTE01 and GGTP01 for --langpack).
"""

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DECOMP = ROOT / "decomp"
WORK = ROOT / "build" / "decomp"
PATCHES = sorted(str(p) for p in (ROOT / "patches").glob("*.patch"))


def git(cwd: Path, *args: str, check: bool = True) -> subprocess.CompletedProcess:
    # a failing command shows its message; a probe (check=False) stays quiet
    return subprocess.run(["git", *args], cwd=cwd, check=check, text=True, stdout=subprocess.PIPE,
                          stderr=None if check else subprocess.DEVNULL)


def prepare() -> None:
    head = git(DECOMP, "rev-parse", "HEAD").stdout.strip()
    if not (WORK / ".git").exists():
        git(DECOMP, "worktree", "add", "--detach", str(WORK), head)
    elif git(WORK, "rev-parse", "HEAD").stdout.strip() == head and \
            git(WORK, "apply", "--check", "--reverse", "--index", *PATCHES, check=False).returncode == 0:
        return  # already patched: keep the files' timestamps, so ninja rebuilds nothing
    git(WORK, "reset", "-q", "--hard", head)
    git(WORK, "apply", "--index", *PATCHES)


def link_discs() -> None:
    # the discs stay in decomp/orig; the working copy sees them through symlinks
    for disc in (DECOMP / "orig").glob("*/*"):
        target = WORK / "orig" / disc.parent.name / disc.name
        if disc.name != ".gitkeep" and not target.exists():
            target.parent.mkdir(parents=True, exist_ok=True)
            target.symlink_to(disc)


def main() -> None:
    prepare()
    link_discs()
    subprocess.run([sys.executable, "configure.py", "--version", "R24J01", *sys.argv[1:]], cwd=WORK, check=True)
    subprocess.run(["ninja"], cwd=WORK, check=True)


if __name__ == "__main__":
    main()
