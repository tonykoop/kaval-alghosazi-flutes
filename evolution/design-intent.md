# Design Intent — kaval-alghosazi-flutes rev A

- Master CAD: `cad/kaval_alghosazi_master.scad` (sha256: c42d454dca177201263adffe5e6119c1dd6b02e1e94f62a42d3a19850f0d5d58) + `cad/kaval_alghosazi_body.scad` (sha256: 21786146c1ea73cd9707182d0e88491040a9f89159951d2f006b13d59cee006a), driven by `Kaval-Alghosazi-Design.xlsx` (sha256: e3fb7870a6145c4f49f438ee006fb4e052e1e944b8448978cd7332c4566e9df4)
- Function: A family of long duct/fipple flutes — a Moldavian/Romanian-style fipple kaval (5-hole, 7-hole, two-piece, double-drone variants) and a fipple Alghosazi (Anasazi/Basketmaker-lineage-inspired, rear thumb hole). The head is a Tony-shop fujara/NAF hybrid fipple (end mouth inlet, internal flue, side true sound window + splitting edge), not a copy of a commercial maker's head.
- Environment: hand-held wind instrument; long solid or split-blank wooden body; fipple/flue plug is removable and wax-sealed for voicing iteration.
- Target qty: prototype ladder — one A3 5-hole kaval, then one A#3 Alghosazi with thumb hole, before deciding on two-piece/double-drone variants. Deadline: TBD. Budget/unit ceiling: TBD.

## Critical dimensions (carry tolerances)

| Feature | Nominal | Tolerance | Why critical | Source |
| --- | --- | --- | --- | --- |
| Fipple/sound-window correction | unknown | build P0-FIPPLE-HEAD, compare root prediction vs measured (risks.md Acoustic) | governs all downstream hole positions | sound-window-correction-log.csv (measurement_required) |
| Hole positions (kaval/Alghosazi) | first-pass proportional | drill undersized, record before/after cents per hole (validation.csv) | intonation | hole-schedule.csv / family-spec.csv (measurement_required) |
| Bore-wander tolerance | ≤ 0.050 in exit offset | bore scrap first and measure; switch to split-blank CNC if exceeded (risks.md Structural) | wall integrity | risks.md (measurement_required) |
| Windway height | 0.033-0.045 in (trial range) | voicing iteration on removable plug (bom.csv BOM-002) | attack/tone | bom.csv (measurement_required) |
| Alghosazi thumb hole placement | mark with tape, air-grip test | drill undersized before final (risks.md Ergonomic) | playability/ergonomics | risks.md (measurement_required) |

## Incidental (free for DFM)

- Exterior finish (shellac/oil/wax), ferrule material choice (brass vs. hardwood), cosmetic body shaping outside bore/fipple/hole geometry.

## Must-nots (DFM may never violate)

- Do not finalize hole locations before P0 fipple-head sound-window correction is measured and logged (design.md Project Intent; sound-window-correction-log.csv).
- Do not apply heavy finish to the windway or splitting edge — mask both and recheck attack after cure (risks.md Fit And Finish).
- Do not choose ferrule dimensions before the body OD is turned (risks.md Supply).
- Do not commit to elder/locust stock length/scale without verifying supplier stock first; use ash/maple/cherry for prototypes instead (risks.md Supply).
- Do not drill final tone-hole or thumb-hole diameters directly — undersize and tune/fit-test incrementally (risks.md Acoustic/Ergonomic).

## Material intent

- Preferred: straight-grain elder, locust, ash, maple, cherry, or walnut body blank (bom.csv BOM-001).
- Acceptable subs: ash/maple/cherry for prototypes if elder/locust supply is constrained (risks.md Supply).
- Forbidden: none recorded beyond the prototype-before-final-stock sequencing above.

## Stage status

Stage 0 intake complete 2026-07-01. Gate A (Alpha shop compile) NOT yet run — no concessions logged, nothing presented as shippable. Packet stays L1_packet per README until P0 fipple-head and sound-window correction measurements exist.
