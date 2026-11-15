# Chibi-Robo! Wii mod

Mods for the Japanese Wii release of Chibi-Robo! (R24J01), built from the
[decompilation](https://github.com/LabDennis/chibirobo-decomp), which this
repository uses as the git submodule `decomp/`.

One build, no options. What is in it:

- All languages: the game in Japanese, English, German, French, Spanish or Italian, following the
  Wii's system language. The text and the textures with writing on them are generated from your own
  GameCube discs at build time.
- The title logo of the US or European release, taken from your GameCube disc, where the game
  runs in one of their languages.
- A first screen of its own in place of the Wii Remote strap pages: "Press A on your controller",
  drawn with the game's font over its diagonal stripes, both taken from your disc.
- The disc image carries no region (code 3 instead of Japan), so that Dolphin does not switch the
  game to Japanese: it then uses its fallback region and the language set for the Wii.
- The first A press there picks the controls: on a GameCube controller the GameCube controls, on
  the Wii Remote the Wii controls.

```sh
git clone --recursive https://github.com/LabDennis/chibirobo-wii-mod.git
cd chibirobo-wii-mod
# put your disc images into decomp/orig/R24J01/ and into GGTE01/ or GGTP01/ (see below)
python3 build.py
```

`build.py` makes a patched copy of the decomp in `build/decomp` and builds it there. The output
appears under `build/decomp/build/wii-global-gcncon/`: `main.dol`, `game.json` for Dolphin,
`riivolution.xml` and the disc image `wii-global-gcncon.iso`. Writing the image needs
[Wiimms ISO Tools](https://wit.wiimm.de) (`wit` on `PATH` or in `~/.local/opt/wit/bin`).

The aim is one "ultimate" build of the game made from the decompilation and your own discs, and
later a patcher that turns the disc image into it directly, without a compiler.

## What you need

- The Japanese Wii disc (R24J01).
- A GameCube disc of the game: the US release (GGTE01) for English, or the European release
  (GGTP01) for English, German, French, Spanish and Italian. With both, English comes from the US
  disc. A language the build has no disc for plays in English.
- Optional: the Japanese GameCube disc (GGTJ01_01). With it more of the textures that carry writing
  can be matched to their Wii counterparts.

Everything translated is taken from these discs when you build. No game data is in this repository: everything comes from your discs.

## Status

`decomp/` follows the decomp's `all-releases` branch, which builds all four
releases (GGTE01, GGTJ01_01, GGTP01 and R24J01) and holds no mod code. The
mod is carried as `patches/wii-mod.patch` on top of it: the mod's `#if`
blocks in the game code, its configure options (which `build.py` always passes) and build steps,
its tools and the translations in `mods/wii-localization/`.

Next steps: split the patch into mod units that the game reaches through
one-line hooks, and generate the translations from the discs instead of
shipping text.
