# Risks

## Acoustic

- **Fipple/sound-window correction is unknown.** Test: build `P0-FIPPLE-HEAD`, record root prediction vs measured, and update `sound-window-correction-log.csv` before trusting final hole locations.
- **Hole positions are first-pass proportional.** Test: drill undersized and record before/after cents for every hole in `validation.csv`.
- **Double-drone windways may steal pressure from each other.** Test: record each windway alone and together; compare attack and cents drift.

## Structural

- **Long solid blanks can wander while drilling.** Test: bore scrap first and measure exit offset; use split-blank CNC if wander exceeds 0.050 in.
- **Two-piece joints can leak or crack.** Test: vacuum/leak check and dry assembly force check before finishing.
- **Splitting edge is fragile.** Test: inspect under magnification after each voicing change.

## Ergonomic

- **7-hole kaval lower holes may require base-of-finger coverage.** Test: paper wrap mockup before drilling final diameters.
- **Alghosazi thumb hole may not fit all hands.** Test: mark with tape, play air-grip, then drill undersized.

## Supply

- **Elder and locust blanks may be hard to source in required lengths.** Test: verify supplier stock before committing scale/key; use ash/maple/cherry for prototypes.
- **Ferrule dimensions may not match body OD.** Test: choose ferrule after body OD is turned, not before.

## Fit And Finish

- **Finish can clog the windway.** Test: mask windway and splitting edge; recheck attack after cure.
- **Cork compression changes with humidity.** Test: assemble/disassemble after overnight humidity change and record fit.
