# Sifu: The Tarnished Fist

**Status: design scaffold only — not a playable build, not tested, and not submitted to Melty.**

A planned solo crossover with **ELDEN RING - Adventure Guide** as the primary host and **SIFU** as a required companion. The initial scope is one unarmed ability set, one Sifu-inspired boss, one NPC, and a minimal test mode.

## Creative direction
The player begins by meeting a martial-arts mentor, equips an adapted unarmed technique, tests it on a training target, then encounters a Sifu-inspired challenger. Sifu's actual character and animation references must come from the player's own Sifu installation; host-compatible implementation remains to be verified.

## Repository contents
- `project.json`: project scope and compatibility assumptions
- `abilities.json`: first-pass move-set design
- `characters.json`: first-pass NPC/boss concepts
- `moves.json`: animation/move adaptation notes
- `systems.json`: gameplay systems and intended behavior
- `preflight.json`: validation gates before any build or publication
- `preflight_check.py`: checks the design data for unresolved blockers
- `LICENSE`: MIT license for original code/docs only

## Asset policy
This project must not bundle either game's proprietary assets. It should read only the required content from each player's own installed copies, including SIFU, if technically feasible. No game assets are licensed by this project.

## License and remixing
MIT applies to original code and documentation only. Others may remix that original material. It does not permit redistribution of ELDEN RING or SIFU assets. See `LICENSE`.

## Source of truth
The JSON sheets are authoritative. Any `TODO`, `unverified`, or unresolved reference is a preflight failure. Run `python preflight_check.py` before every build; the current result is expected to be blocked until the actual games and mod route are inspected.

## Current blockers
The Melty service could not be reached from this environment, and the current tools do not expose Melty's publishing/modding actions or the user's Windows game-install folders. Consequently, the installed game versions, loader support, content formats, actual in-game implementation, screenshot, recipe validation, one-click check, package inspection, and Melty release test remain unverified. This scaffold must not be represented as a working mod.

## Credits
- SIFU: Sloclap. All rights to the game and its content remain with their respective rights holders.
- ELDEN RING - Adventure Guide: the exact edition/publisher/creator credit must be verified before the final Melty listing.
- Original code and documentation: Sifu: The Tarnished Fist contributors, MIT License.
