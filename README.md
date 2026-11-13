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
# put your discs into decomp/orig/R24J01, decomp/orig/GGTE01, decomp/orig/GGTP01
python3 build.py --langpack global --gcncon --iso
```

No game data is in this repository: everything comes from your discs.

## Status

The mod code still lives in the decomp's `wii-mod` branch, which `decomp/`
points at. Next steps: move the mod code and its hooks into this repository,
keep the decomp clean, and generate every translation from the discs instead of
shipping text.
