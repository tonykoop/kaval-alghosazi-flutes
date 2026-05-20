# Kaval + Alghosazi Fipple Flutes

**Packet ID:** KAV-ALG-FAM-001  
**Family:** open-pipe woodwind / duct-fipple flute  
**Pipeline:** cnc-lathe hybrid: split blank or deep bore, fipple head, lathe rounding, optional two-piece joint  
**Date:** 2026-05-06  
**Done-bar references:** `fujara`, `flutes`, `drone-flutes`, `pistalka`, `transverse-flute`

## Project Intent

Design a buildable family of long fipple kavals and Alghosazi flutes that feel close to the Fujara Flutes references while using Tony's existing fujara/flute workshop logic: parametric dimensions, a controllable fipple sound-window head, split-blank CNC or deep-bore construction, validation tables, and documented tuning loops.

The first physical goal is not a perfect production run. It is a controlled prototype ladder: prove the fipple head, build one A3 5-hole kaval, build one A#3 Alghosazi with a thumb hole, then decide whether the two-piece and double-drone versions deserve full CAD.

## Source And Scope

External reference pages checked:

- Fujara Flutes Kaval page: 5-hole fipple kavals, 7-hole expanded kavals, lengths from about 62-90 cm, and double Kaval/Kavalghoza drone concept.
- Fujara Flutes Alghosazi page: fipple adaptation of Anasazi-style flute, top hole moved to the back as a thumb hole, lengths from about 70-85 cm, and a double-drone option.
- Flutopedia Anasazi tuning notes: used only to justify the Alghosazi starter offset set as an Anasazi-derived primary sequence.

Local source artifacts inspected:

- `fujara/design-table/fujara_equations.md` and SolidWorks dimension extracts for fipple/flue plug geometry.
- `drone-flutes/design.md` and `flutes/skills/parametric-design-table.md` for open-pipe, shop, and validation workflow.
- `pistalka/docs/build-packet/design.md` for a compact fipple-flute build sequence.

## Governing Model

These flutes are modeled as **open-open cylindrical fipple flutes** with a non-NAF fujara-style sound-window end correction.

```text
f = c / (2 * L_eff)
c = 13552 in/s at about 68 F
L_eff = physical_labium_to_foot + foot_end_correction + sound_window_correction
foot_end_correction ~= 0.6 * bore_radius
sound_window_correction = measured prototype value, not Tony's NAF K2 table
```

For first-pass hole placement, the packet uses a proportional open-pipe layout:

```text
x_from_labium = labium_to_foot * 2^(-semitone_offset / 12)
x_from_foot = labium_to_foot - x_from_labium
```

The hole schedule is intentionally a **starter drill schedule**. The builder drills undersized, tunes the root by trimming the foot, then opens each hole upward by careful reaming/undercutting. If a hole goes sharp, the recovery is wax test, bushing, or a rebuilt body.

`family-spec.csv` includes `estimated_sound_window_correction_in`. Positive values mean the fipple/window system or added acoustic path must make the instrument behave longer than the visible labium-to-foot length. Negative values mean the source-observed body length is overlong for the nominal root under a simple open-pipe model; treat those as overlength blanks to trim or as evidence that the commercial key naming may not equal the all-closed root.

The first-pass schedules do not yet include a measured sound-window correction. Back-solve it after P0 with:

```text
L_eff_measured = c / (2 * measured_root_hz)
sound_window_correction = L_eff_measured - labium_to_foot - foot_end_correction
foot_end_correction ~= 0.6 * bore_radius
```

Record the result in `sound-window-correction-log.csv`. Only then update `Kaval-Alghosazi-Design.xlsx`, `family-spec.csv`, and the hole schedules.

## Scale Plans

### 5-Hole Fipple Kaval

The 5-hole kaval follows the published C-reference pitch set:

```text
0, +2, +3, +6, +7, +8 semitones
Example in C: C D D# F# G G#
```

### 7-Hole Fipple Kaval

The expanded kaval adds the two half-step options described by the reference page:

```text
0, +2, +3, +4, +6, +7, +8, +9 semitones
Example in C: C D D# E F# G G# A
```

### Alghosazi

The Alghosazi starter scale uses an Anasazi-derived primary sequence. The top hole is placed on the back as a thumb hole, matching the design note from the reference page.

```text
0, +2, +4, +7, +9, +11, +12 semitones
Example in A#: A# C D F G A A#
```

This is marked as a musical-design assumption. If Tony wants a different Alghosazi mode after listening to examples, change the offsets in `Kaval-Alghosazi-Design.xlsx` and regenerate `hole-schedule.csv`.

## Fujara-Style Fipple Head

The requested head architecture is:

```text
mouth at end -> rectangular inlet -> internal windway/flue -> side true sound window -> splitting edge -> main bore
```

Starter dimensions:

| Feature | Kaval Starter | Alghosazi Starter | Notes |
| --- | ---: | ---: | --- |
| Top end to true window datum | 1.45-1.65 in | 1.65-1.80 in | Adjust for comfort and joint location. |
| Windway height | 0.033-0.045 in | 0.035-0.048 in | Start with removable flue plug trials. |
| Windway width | 0.45-0.55 in | 0.45-0.58 in | About 55-65 percent of bore. |
| Window length | 0.25-0.38 in | 0.28-0.42 in | Widen/lengthen only after tone test. |
| Splitting edge offset KPI | 0.005-0.015 in | 0.005-0.015 in | Borrowed from Tony's fujara canary, not a final law. |
| Plug fit | wax-sealed slip | wax-sealed slip | Removable until final voicing. |

### P0 Measurement Loop

Build `P0-FIPPLE-HEAD` before a full flute body. Use scrap stock or a short half-bore test channel matching the selected bore, cut the end mouth inlet, test removable plug shims at 0.033, 0.038, and 0.045 in, and vary only one window or splitting-edge parameter between trials.

For each speaking trial, log the measured windway height, window length, window width, splitting-edge offset, blow-pressure note, temperature/RH, measured root pitch, and whether the tone chokes, overblows, or stabilizes. The geometry stays inferred until that log exists.

## Two-Piece And Double Options

The two-piece option is a **shop convenience and tuning risk**, not a decorative afterthought. Use it only after a solid prototype speaks well.

- Tenon engagement: 1.25 in minimum.
- Cork compression: fit by sanding; no forced assembly.
- Joint location: avoid placing the joint within 0.75 in of a tone hole.
- Bore step: less than 0.005 in at the joint after final sanding.
- Ferrule: recommended for A/A# bodies and double-flute assemblies.

Double-drone versions are documented in `double-drone-spec.csv` and `drawings/double-drone-layout.svg`. Each side gets its own windway so the melody flute can be played alone and the drone can be tuned independently.

## Family Table

See `family-spec.csv` for the source of truth. The core starter members are:

| Member | Role |
| --- | --- |
| `KAV-A3-5H` | First kaval prototype. |
| `KAV-AS3-7H` | Two-piece expanded kaval prototype. |
| `ALG-AS3-J2` | First Alghosazi prototype. |
| `ALG-A3-J3` | Three-piece Alghosazi joint stress test. |

## Manufacturing Path

Preferred path for the first two prototypes:

1. Make a removable fipple-head test tile from scrap.
2. Record the speaking head settings and back-solve the sound-window correction in `sound-window-correction-log.csv`.
3. Build a split-blank body so the bore, windway, and window are visible and correctable.
4. Glue and turn only after the fipple speaks.
5. Drill holes undersized from a laser/CNC template or V-block setup.
6. Tune root first, then holes from foot upward.
7. Record measurements in `validation.csv` and `validation-loop.csv`, then update the next prototype.

Deep-bore drilling is allowed for later solid-body builds. Use the skill reference `headstock-driven-deep-bore-drilling.md` before attempting a long solid blank.

## Assumptions

- A4 = 440 Hz.
- 68 F speed-of-sound baseline.
- Website lengths are used as precedent dimensions, not guaranteed acoustic formulas.
- Alghosazi tuning is a starter interpretation based on contemporary Anasazi-tuned six-hole practice.
- Tone hole positions ignore final hole-diameter perturbation until measured prototype data exists.
- The fipple head is Tony's derived design and must be validated by physical tests.
- The P0 correction is unknown until measured; do not promote this packet above `L1_packet` from source observations alone.
