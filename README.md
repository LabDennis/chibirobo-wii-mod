# Chibi-Robo! Wii mod

Mods for the Japanese Wii release of Chibi-Robo! (R24J01), built from the
[decompilation](https://github.com/LabDennis/chibirobo-decomp), which this
repository uses as the git submodule `decomp/`.

- `--gcncon`: GameCube controller. The first A press on the first screen picks
  the controls: GameCube controller, or the Wii Remote with its extras.
- `--langpack <locale>` / `--langpack global`: the game in English, German,
  French, Spanish or Italian, or chosen by the Wii's system language. The text
  is generated from your own GameCube discs at build time.
- `--iso`: also write a disc image (needs [Wiimms ISO Tools](https://wit.wiimm.de)).

```sh
git clone --recursive https://github.com/LabDennis/chibirobo-wii-mod.git
cd chibirobo-wii-mod
# put your discs into decomp/orig/R24J01/, decomp/orig/GGTE01/, decomp/orig/GGTP01/
python3 build.py --langpack global --gcncon --iso
```

`build.py` makes a patched copy of the decomp in `build/decomp` and builds it
there. The output appears under `build/decomp/build/wii-*/`, named after the
options, for example `build/decomp/build/wii-global-gcncon/` with `main.dol`,
`game.json` for Dolphin, `riivolution.xml`, and with `--iso` the disc image.

No game data is in this repository: everything comes from your discs.

## Status

`decomp/` follows the decomp's `all-releases` branch, which builds all four
releases (GGTE01, GGTJ01_01, GGTP01 and R24J01) and holds no mod code. The
mod is carried as `patches/wii-mod.patch` on top of it: the mod's `#if`
blocks in the game code, its configure options and build steps, its tools and
the translations in `mods/wii-localization/`.

Next steps: split the patch into mod units that the game reaches through
one-line hooks, and generate the translations from the discs instead of
shipping text.
