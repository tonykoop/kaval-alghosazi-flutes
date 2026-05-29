# Sound-Window Correction — Acoustic Back-Solve Model

Status: L1 model estimate. No physical P0 measurement has been performed yet.
All corrections below are first-order analytical values. The P0 fipple-head
measurement must be completed before any hole position is considered authoritative.

## Purpose

The side sound-window and splitting edge of a fipple flute create an acoustic
end-correction that shifts the effective length of the air column away from the
physical labium-to-foot distance. This correction must be measured at P0 and
applied to the hole-schedule before drilling.

## Model

For an open-open cylindrical fipple flute, the effective length is:

```
L_eff = c / (2 × f_root)
```

where:
- `c` = speed of sound at lab conditions ≈ 345,400 mm/s at 22 °C (13,598 in/s)
- `f_root` = measured root pitch in Hz (tuner capture at P0)

The total effective length is composed of:

```
L_eff = labium_to_foot + sound_window_correction + foot_end_correction
```

Rearranging to back-solve the sound-window correction:

```
sound_window_correction = L_eff - labium_to_foot - foot_end_correction
```

The foot end-correction for an unflanged open end:

```
foot_end_correction ≈ 0.6 × bore_radius
```

## Model Estimates (pending P0 measurement)

These are **pre-P0 estimates only**. Do not use for cutting. Record the
measured back-solve in `sound-window-correction-log.csv` after the P0 build.

Sound speed at 22 °C / 345.4 m/s = 13,598 in/s = 345,400 mm/s.

### KAV-A3-5H (kaval, A3 root, 5-hole)

| Parameter | Value | Source |
| --- | --- | --- |
| Target root | A3 = 220.000 Hz | family-spec.csv |
| Bore ID | 0.875 in = 22.23 mm | Kaval-Alghosazi-Design.xlsx |
| Bore radius | 11.11 mm | derived |
| L_eff at 220 Hz | 345,400 / (2 × 220) = 785.0 mm | model estimate |
| Foot end-correction | 0.6 × 11.11 = 6.7 mm | standard approximation |
| Labium-to-foot (nominal) | ~735 mm | workbook estimate — measurement required |
| **Model sound-window correction** | **785.0 − 735 − 6.7 ≈ +43 mm** | **model estimate — pending P0** |

**Acoustic honesty caveat:** The labium-to-foot distance is a workbook estimate
from source references. The actual P0-measured value may differ by ±10 mm or
more depending on fipple-head geometry and plug setting. The model correction
of +43 mm is a **starting reference only**, not a dimensional authority.

### ALG-AS3-J2 (alghosazi, A#3 root, two-piece, 6-hole)

| Parameter | Value | Source |
| --- | --- | --- |
| Target root | A#3 = 233.082 Hz | family-spec.csv |
| Bore ID | 0.875 in = 22.23 mm | Kaval-Alghosazi-Design.xlsx |
| Bore radius | 11.11 mm | derived |
| L_eff at 233.082 Hz | 345,400 / (2 × 233.082) = 741.2 mm | model estimate |
| Foot end-correction | 0.6 × 11.11 = 6.7 mm | standard approximation |
| Labium-to-foot (nominal) | ~690 mm | workbook estimate — measurement required |
| **Model sound-window correction** | **741.2 − 690 − 6.7 ≈ +44.5 mm** | **model estimate — pending P0** |

**Acoustic honesty caveat:** Same as KAV-A3-5H above. All values are
analytical estimates; the P0 measurement log drives actual hole positions.

## Hole-Schedule Update Rule

If the back-solved P0 correction shifts any hole center by more than 2.5 mm
(0.100 in), regenerate the hole-schedule(s) from the corrected labium-to-foot
before marking any column `measured`.

The `effective_length_correction_mm` column in `hole-schedule.csv`,
`kaval-hole-schedule.csv`, and `alghosazi-hole-schedule.csv` holds the
correction applied for the row's geometry. Until P0 is complete, all values
in that column are `pending_measurement`.

## Reference

- Fletcher and Rossing, *Physics of Musical Instruments*, §16.2 — end corrections
  for open cylindrical pipes.
- Benade, *Fundamentals of Musical Acoustics*, §21.2 — fipple and labium
  end-correction discussion.
- `docs/p0-fipple-head-measurement.md` — measurement procedure and P0 pass criteria.
- `sound-window-correction-log.csv` — back-solve log to fill after P0 build.
