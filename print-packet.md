# Kaval + Alghosazi Fipple Flutes Capstone Print Packet

Generated: 2026-05-05
Packet folder: `/mnt/c/Users/Tony/Documents/GitHub/kaval-alghosazi-flutes`

## File Map

| File | Purpose |
| --- | --- |
| `design.md` | Project intent, catalog metadata, assumptions, and validation plan. |
| `bom.csv` | Starter bill of materials with part categories, quantities, drawing refs, and notes. |
| `sourcing.csv` | Supplier/search tracker with specs, price/date fields, lead time, substitutes, and risks. |
| `cut-list.csv` | Rough/final stock sizes, material, grain/orientation, operations, yield, and offcuts. |
| `drawing-brief.md` | Manufacturing drawing and technical product sketch brief. |
| `assembly-manual.md` | Shop-facing sequence, tools, fixtures, safety, tuning, finishing, and maintenance notes. |
| `validation.csv` | Target/measured values, tolerance, environment, result, and tuning/build action log. |
| `supplier-rfq.md` | Supplier email/request-for-quote starter. |
| `visual-bom-brief.md` | Art direction for an image-forward visual BOM. |
| `wolfram-starter.wl` | Wolfram starter for physics, optimization, visualization, and validation. |
| `README.md` | Project artifact. |
| `alghosazi-hole-schedule.csv` | Project artifact. |
| `double-drone-spec.csv` | Project artifact. |
| `family-spec.csv` | Project artifact. |
| `hole-schedule.csv` | Project artifact. |
| `kaval-hole-schedule.csv` | Project artifact. |
| `photo-shotlist.md` | Project artifact. |
| `risks.md` | Project artifact. |
| `sources.md` | Project artifact. |

<div class="page-break"></div>

## design.md

Project intent, catalog metadata, assumptions, and validation plan.

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
2. Build a split-blank body so the bore, windway, and window are visible and correctable.
3. Glue and turn only after the fipple speaks.
4. Drill holes undersized from a laser/CNC template or V-block setup.
5. Tune root first, then holes from foot upward.
6. Record measurements in `validation.csv` and update the next prototype.

Deep-bore drilling is allowed for later solid-body builds. Use the skill reference `headstock-driven-deep-bore-drilling.md` before attempting a long solid blank.

## Assumptions

- A4 = 440 Hz.
- 68 F speed-of-sound baseline.
- Website lengths are used as precedent dimensions, not guaranteed acoustic formulas.
- Alghosazi tuning is a starter interpretation based on contemporary Anasazi-tuned six-hole practice.
- Tone hole positions ignore final hole-diameter perturbation until measured prototype data exists.
- The fipple head is Tony's derived design and must be validated by physical tests.

<div class="page-break"></div>

## bom.csv

Starter bill of materials with part categories, quantities, drawing refs, and notes.

| item | assembly | part | qty | spec | make_buy | est_cost_usd | source_status | drawing_ref | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BOM-001 | all | Primary body blank | 1 per flute | Straight-grain elder, locust, ash, maple, cherry, or walnut; length per family-spec plus 2 in trim | buy | 25-90 | spec only | drawings/*-body.svg | Avoid runout through tone holes and joint tenons. |
| BOM-002 | head | Removable fipple/flue plug | 1 plus 2 test plugs | Hard maple, pear, or dense straight-grain scrap; 0.033-0.045 in windway height trials | make | 5 | shop scrap ok | drawings/fipple-head-section.svg | Wax-sealed removable plug makes voicing iteration survivable. |
| BOM-003 | joint | Cork sheet or natural cork rings | 1 strip per joint | 1/32 to 1/16 in cork, sanded to airtight slip fit | buy | 8-15 | verify before purchase | drawings/two-piece-joint.svg | Use only on removable joints; permanent split bodies use glue. |
| BOM-004 | joint | Brass or hardwood ferrule sleeve | optional | Thin brass tube or hardwood collar sized to body OD | buy/make | 10-25 | verify diameter | drawings/two-piece-joint.svg | Recommended for long A/A# bodies and double-flute assemblies. |
| BOM-005 | finish | Exterior finish | 1 | Shellac, polymerized oil, or oil/wax; keep windway and bore lightly sealed only after tuning | buy | 10-30 | shop stock likely | assembly-manual.md | No heavy finish on splitting edge. |
| BOM-006 | fixture | V-block and drilling template stock | 1 set | MDF/plywood V-block, laser-cut paper/acrylic hole templates, 1/4 in dowel pins | make | 10-20 | shop stock likely | cnc/setup-sheet.md | Template holes should be undersized pilots. |
| BOM-007 | validation | Tuning/measurement kit | 1 | Chromatic tuner, thermometer/hygrometer, calipers, small round files, recording device | use shop kit | 0-60 | existing kit likely | validation.csv | Record temperature with every tuning pass. |

<div class="page-break"></div>

## sourcing.csv

Supplier/search tracker with specs, price/date fields, lead time, substitutes, and risks.

| component | required_spec | search_terms | candidate_supplier | price_each | date_checked | lead_time | substitutes | risk |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| straight-grain hardwood blanks | 1.25-1.50 in square or round, 28-38 in long, stable and dry | elder wood blank, locust spindle blank, ash turning blank, maple turning blank | local hardwood dealer / Woodcraft / Rockler / Global Wood Source | TBD | TBD | TBD | maple/cherry/walnut for prototype | Species and grain affect cracking and tone; verify straight grain before purchase. |
| cork joint material | thin sheet or rings, sandable, airtight | woodwind tenon cork sheet 1/32 1/16 | music repair supplier / Amazon / McMaster | TBD | TBD | TBD | waxed hemp thread for tests | Loose joint leaks; tight joint cracks socket. |
| brass ferrule sleeve | ID/OD matched to selected body, thin wall | brass tube 1.25 inch 1.375 inch thin wall | K&S, McMaster, OnlineMetals | TBD | TBD | TBD | hardwood collar turned on lathe | Metal sleeve changes exterior feel and may buzz if poorly fitted. |
| small brad point drill bits and reamers | 1/8 to 3/8 in, sharp, clean entry | brad point drill bit set small reamer | Woodcraft / Rockler / McMaster | TBD | TBD | TBD | number drill bits plus tapered reamer | Tearout around holes shifts tuning and looks sloppy. |

<div class="page-break"></div>

## cut-list.csv

Rough/final stock sizes, material, grain/orientation, operations, yield, and offcuts.

| member_id | blank_part | material | qty | rough_size_in | final_size_in | grain_orientation | operation | yield_notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| KAV-GS3-5H | main body blank | Locust or elder | 1 | 1.625 x 1.625 x 33.102 | OD 1.375, bore 0.875, length 31.102 | straight along bore axis | square, split or bore, route/drill, glue if split, turn/round, tune foot | Leave 2 in trim for root tuning and chuck/fixture allowance. |
| KAV-GS3-5H | joint tenon/socket allowance | Locust or elder plus cork/ferrule | 1 | extra 2.5 in distributed around joint | 1.250 in tenon engagement, 0.003-0.006 in cork-adjusted compression | same as body | turn tenon/socket after bore alignment is proven | Cut joint after body is acoustically proven on a sacrificial overlength blank. |
| KAV-A3-5H | main body blank | Elder | 1 | 1.625 x 1.625 x 31.134 | OD 1.375, bore 0.875, length 29.134 | straight along bore axis | square, split or bore, route/drill, glue if split, turn/round, tune foot | Leave 2 in trim for root tuning and chuck/fixture allowance. |
| KAV-A3-5H | joint tenon/socket allowance | Elder plus cork/ferrule | 1 | extra 2.5 in distributed around joint | 1.250 in tenon engagement, 0.003-0.006 in cork-adjusted compression | same as body | turn tenon/socket after bore alignment is proven | Cut joint after body is acoustically proven on a sacrificial overlength blank. |
| KAV-B3-5H | main body blank | Elder | 1 | 1.562 x 1.562 x 28.378 | OD 1.312, bore 0.812, length 26.378 | straight along bore axis | square, split or bore, route/drill, glue if split, turn/round, tune foot | Leave 2 in trim for root tuning and chuck/fixture allowance. |
| KAV-C4-5H | main body blank | Elder, maple, or cherry | 1 | 1.500 x 1.500 x 26.409 | OD 1.250, bore 0.750, length 24.409 | straight along bore axis | square, split or bore, route/drill, glue if split, turn/round, tune foot | Leave 2 in trim for root tuning and chuck/fixture allowance. |
| KAV-A3-7H | main body blank | Elder | 1 | 1.650 x 1.650 x 37.433 | OD 1.400, bore 0.875, length 35.433 | straight along bore axis | square, split or bore, route/drill, glue if split, turn/round, tune foot | Leave 2 in trim for root tuning and chuck/fixture allowance. |
| KAV-AS3-7H | main body blank | Dogwood or elder | 1 | 1.650 x 1.650 x 35.465 | OD 1.400, bore 0.875, length 33.465 | straight along bore axis | square, split or bore, route/drill, glue if split, turn/round, tune foot | Leave 2 in trim for root tuning and chuck/fixture allowance. |
| KAV-AS3-7H | joint tenon/socket allowance | Dogwood or elder plus cork/ferrule | 1 | extra 2.5 in distributed around joint | 1.250 in tenon engagement, 0.003-0.006 in cork-adjusted compression | same as body | turn tenon/socket after bore alignment is proven | Cut joint after body is acoustically proven on a sacrificial overlength blank. |
| KAV-B3-7H | main body blank | Elder | 1 | 1.562 x 1.562 x 29.165 | OD 1.312, bore 0.812, length 27.165 | straight along bore axis | square, split or bore, route/drill, glue if split, turn/round, tune foot | Leave 2 in trim for root tuning and chuck/fixture allowance. |
| ALG-AS3-J2 | main body blank | Ash | 1 | 1.625 x 1.625 x 34.283 | OD 1.375, bore 0.875, length 32.283 | straight along bore axis | square, split or bore, route/drill, glue if split, turn/round, tune foot | Leave 2 in trim for root tuning and chuck/fixture allowance. |
| ALG-AS3-J2 | joint tenon/socket allowance | Ash plus cork/ferrule | 1 | extra 2.5 in distributed around joint | 1.250 in tenon engagement, 0.003-0.006 in cork-adjusted compression | same as body | turn tenon/socket after bore alignment is proven | Cut joint after body is acoustically proven on a sacrificial overlength blank. |
| ALG-AS3-SOLID | main body blank | Locust | 1 | 1.625 x 1.625 x 35.465 | OD 1.375, bore 0.875, length 33.465 | straight along bore axis | square, split or bore, route/drill, glue if split, turn/round, tune foot | Leave 2 in trim for root tuning and chuck/fixture allowance. |
| ALG-A3-J3 | main body blank | Oak | 1 | 1.625 x 1.625 x 30.740 | OD 1.375, bore 0.875, length 28.740 | straight along bore axis | square, split or bore, route/drill, glue if split, turn/round, tune foot | Leave 2 in trim for root tuning and chuck/fixture allowance. |
| ALG-A3-J3 | joint tenon/socket allowance | Oak plus cork/ferrule | 1 | extra 2.5 in distributed around joint | 1.250 in tenon engagement, 0.003-0.006 in cork-adjusted compression | same as body | turn tenon/socket after bore alignment is proven | Cut joint after body is acoustically proven on a sacrificial overlength blank. |
| ALG-B3-SOLID | main body blank | Elder or maple | 1 | 1.562 x 1.562 x 29.559 | OD 1.312, bore 0.812, length 27.559 | straight along bore axis | square, split or bore, route/drill, glue if split, turn/round, tune foot | Leave 2 in trim for root tuning and chuck/fixture allowance. |

<div class="page-break"></div>

## drawing-brief.md

Manufacturing drawing and technical product sketch brief.

# Drawing Brief

## Required Views

- Family overview: each member as a scaled open-pipe body with bore ID and total length.
- Hole layout: kaval and Alghosazi separate, measured from labium and from foot.
- Fipple head section: end mouth inlet, windway, flue plug, true sound window, splitting edge, bore.
- Two-piece joint section: tenon, socket, cork wrap, ferrule/collar, bore continuity.
- Double-drone layout: two bores, independent windways, melody side, drone side, thumb vent.

## Datums

- Datum A: labium/splitting-edge plane.
- Datum B: tuned foot end.
- Datum C: bore centerline.
- Datum D: back thumb-hole centerline for Alghosazi.

## Tolerances

- Bore ID: +/-0.005 in after reaming/lapping.
- Hole center: +/-0.020 in before tuning; final pitch matters more than nominal center.
- Windway height: +/-0.002 in once a plug speaks.
- Joint bore step: less than 0.005 in.
- Noncritical exterior: +/-0.030 in.

## Drawing Outputs

Generated SVGs live in `drawings/`. Build-critical dimensions come from `Kaval-Alghosazi-Design.xlsx`, `family-spec.csv`, and `hole-schedule.csv`, not from raster images.

<div class="page-break"></div>

## assembly-manual.md

Shop-facing sequence, tools, fixtures, safety, tuning, finishing, and maintenance notes.

# Assembly Manual

## Safety And Setup

- Wear eye and lung protection when drilling, routing, sanding, or turning.
- Do not route a long round blank without a stable V-block or split-blank fixture.
- Keep the splitting edge protected until final voicing.
- Mark the labium datum, foot datum, bore centerline, and back thumb-hole line before any irreversible cut.

## Prototype Ladder

### P0: Fipple Head Tile

1. Cut a 4 in scrap block with the selected bore diameter or a half-bore test channel.
2. Cut the end mouth inlet.
3. Fit a removable flue plug with 0.033, 0.038, and 0.045 in shim trials.
4. Cut a side true sound window and splitting edge.
5. Blow through the end inlet and record which plug/window combination speaks cleanly.
6. Do not build a full flute until this tile produces stable tone.

### P1: First Kaval Body

1. Select `KAV-A3-5H`.
2. Mill the blank overlength by at least 2 in.
3. Split the blank, route the bore halves and registration pin holes, or deep-bore the solid blank after proving setup on scrap.
4. Create the fipple head and removable plug.
5. Prove the root tone with no finger holes.
6. Trim the foot to bring the all-closed root toward A3.
7. Transfer hole positions from `kaval-hole-schedule.csv`.
8. Drill each hole undersized.
9. Tune holes from the foot upward by reaming slowly.
10. Record every before/after pitch in `validation.csv`.

### P1: First Alghosazi Body

1. Select `ALG-AS3-J2`.
2. Build as a solid body first if joint risk feels high; otherwise cut the two-piece joint after the bore is proven.
3. Mark the rear thumb-hole line before drilling.
4. Drill the thumb hole undersized and validate reach with the actual player grip.
5. Tune the primary sequence and record whether the scale feels musically right.

### P2: Jointed Version

1. Cut the body overlength and prove tone before final jointing.
2. Locate the joint away from holes and away from the fipple head.
3. Turn tenon and socket with a 1.25 in engagement target.
4. Add cork or waxed thread until the joint seals without force.
5. Check bore step with a dowel, light, and feeler test.
6. Re-test root and all holes after the joint is fitted.

### P3: Double Drone

1. Build melody and drone tubes separately.
2. Tune the melody side alone.
3. Tune the drone side alone, including rear thumb vent if used.
4. Join the bodies temporarily with clamps or bands before permanent collars.
5. Test pressure sharing with both windways.
6. Only then commit to a permanent double-body fixture or decorative binding.

## Finishing

- Finish exterior after tuning.
- Keep heavy oil, shellac, and wax out of the windway and splitting edge.
- Seal bore lightly only after final measurements.
- Recheck pitch after finish cure.

## Maintenance

- Let the bore dry after playing.
- Remove the fipple plug only if the design uses a wax-sealed removable plug.
- Do not store jointed bodies assembled under high humidity swings.

<div class="page-break"></div>

## validation.csv

Target/measured values, tolerance, environment, result, and tuning/build action log.

| member_id | test_id | target | target_value | measured_value | tolerance | environment | pass_fail | action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| KAV-GS3-5H | VAL-ROOT | root G#3 | 207.652 Hz |  | +/-25 cents P1, +/-10 cents P2 | TBD temp/RH |  | Trim foot shorter to raise pitch; rebuild/extend foot if sharp. |
| KAV-GS3-5H | VAL-H1 | hole 1 offset +2 st | 233.082 Hz |  | +/-25 cents P1, +/-10 cents P2 | TBD temp/RH |  | Enlarge/undercut slowly to raise; wax or bushing recovery if sharp. |
| KAV-GS3-5H | VAL-H2 | hole 2 offset +3 st | 246.942 Hz |  | +/-25 cents P1, +/-10 cents P2 | TBD temp/RH |  | Enlarge/undercut slowly to raise; wax or bushing recovery if sharp. |
| KAV-GS3-5H | VAL-H3 | hole 3 offset +6 st | 293.665 Hz |  | +/-25 cents P1, +/-10 cents P2 | TBD temp/RH |  | Enlarge/undercut slowly to raise; wax or bushing recovery if sharp. |
| KAV-GS3-5H | VAL-H4 | hole 4 offset +7 st | 311.127 Hz |  | +/-25 cents P1, +/-10 cents P2 | TBD temp/RH |  | Enlarge/undercut slowly to raise; wax or bushing recovery if sharp. |
| KAV-GS3-5H | VAL-H5 | hole 5 offset +8 st | 329.628 Hz |  | +/-25 cents P1, +/-10 cents P2 | TBD temp/RH |  | Enlarge/undercut slowly to raise; wax or bushing recovery if sharp. |
| KAV-A3-5H | VAL-ROOT | root A3 | 220.000 Hz |  | +/-25 cents P1, +/-10 cents P2 | TBD temp/RH |  | Trim foot shorter to raise pitch; rebuild/extend foot if sharp. |
| KAV-A3-5H | VAL-H1 | hole 1 offset +2 st | 246.942 Hz |  | +/-25 cents P1, +/-10 cents P2 | TBD temp/RH |  | Enlarge/undercut slowly to raise; wax or bushing recovery if sharp. |
| KAV-A3-5H | VAL-H2 | hole 2 offset +3 st | 261.626 Hz |  | +/-25 cents P1, +/-10 cents P2 | TBD temp/RH |  | Enlarge/undercut slowly to raise; wax or bushing recovery if sharp. |
| KAV-A3-5H | VAL-H3 | hole 3 offset +6 st | 311.127 Hz |  | +/-25 cents P1, +/-10 cents P2 | TBD temp/RH |  | Enlarge/undercut slowly to raise; wax or bushing recovery if sharp. |
| KAV-A3-5H | VAL-H4 | hole 4 offset +7 st | 329.628 Hz |  | +/-25 cents P1, +/-10 cents P2 | TBD temp/RH |  | Enlarge/undercut slowly to raise; wax or bushing recovery if sharp. |
| KAV-A3-5H | VAL-H5 | hole 5 offset +8 st | 349.228 Hz |  | +/-25 cents P1, +/-10 cents P2 | TBD temp/RH |  | Enlarge/undercut slowly to raise; wax or bushing recovery if sharp. |
| KAV-B3-5H | VAL-ROOT | root B3 | 246.942 Hz |  | +/-25 cents P1, +/-10 cents P2 | TBD temp/RH |  | Trim foot shorter to raise pitch; rebuild/extend foot if sharp. |
| KAV-B3-5H | VAL-H1 | hole 1 offset +2 st | 277.183 Hz |  | +/-25 cents P1, +/-10 cents P2 | TBD temp/RH |  | Enlarge/undercut slowly to raise; wax or bushing recovery if sharp. |
| KAV-B3-5H | VAL-H2 | hole 2 offset +3 st | 293.665 Hz |  | +/-25 cents P1, +/-10 cents P2 | TBD temp/RH |  | Enlarge/undercut slowly to raise; wax or bushing recovery if sharp. |
| KAV-B3-5H | VAL-H3 | hole 3 offset +6 st | 349.228 Hz |  | +/-25 cents P1, +/-10 cents P2 | TBD temp/RH |  | Enlarge/undercut slowly to raise; wax or bushing recovery if sharp. |
| KAV-B3-5H | VAL-H4 | hole 4 offset +7 st | 369.994 Hz |  | +/-25 cents P1, +/-10 cents P2 | TBD temp/RH |  | Enlarge/undercut slowly to raise; wax or bushing recovery if sharp. |
| KAV-B3-5H | VAL-H5 | hole 5 offset +8 st | 391.995 Hz |  | +/-25 cents P1, +/-10 cents P2 | TBD temp/RH |  | Enlarge/undercut slowly to raise; wax or bushing recovery if sharp. |
| KAV-C4-5H | VAL-ROOT | root C4 | 261.626 Hz |  | +/-25 cents P1, +/-10 cents P2 | TBD temp/RH |  | Trim foot shorter to raise pitch; rebuild/extend foot if sharp. |
| KAV-C4-5H | VAL-H1 | hole 1 offset +2 st | 293.665 Hz |  | +/-25 cents P1, +/-10 cents P2 | TBD temp/RH |  | Enlarge/undercut slowly to raise; wax or bushing recovery if sharp. |
| KAV-C4-5H | VAL-H2 | hole 2 offset +3 st | 311.127 Hz |  | +/-25 cents P1, +/-10 cents P2 | TBD temp/RH |  | Enlarge/undercut slowly to raise; wax or bushing recovery if sharp. |
| KAV-C4-5H | VAL-H3 | hole 3 offset +6 st | 369.994 Hz |  | +/-25 cents P1, +/-10 cents P2 | TBD temp/RH |  | Enlarge/undercut slowly to raise; wax or bushing recovery if sharp. |
| KAV-C4-5H | VAL-H4 | hole 4 offset +7 st | 391.995 Hz |  | +/-25 cents P1, +/-10 cents P2 | TBD temp/RH |  | Enlarge/undercut slowly to raise; wax or bushing recovery if sharp. |
| KAV-C4-5H | VAL-H5 | hole 5 offset +8 st | 415.305 Hz |  | +/-25 cents P1, +/-10 cents P2 | TBD temp/RH |  | Enlarge/undercut slowly to raise; wax or bushing recovery if sharp. |
| KAV-A3-7H | VAL-ROOT | root A3 | 220.000 Hz |  | +/-25 cents P1, +/-10 cents P2 | TBD temp/RH |  | Trim foot shorter to raise pitch; rebuild/extend foot if sharp. |
| KAV-A3-7H | VAL-H1 | hole 1 offset +2 st | 246.942 Hz |  | +/-25 cents P1, +/-10 cents P2 | TBD temp/RH |  | Enlarge/undercut slowly to raise; wax or bushing recovery if sharp. |
| KAV-A3-7H | VAL-H2 | hole 2 offset +3 st | 261.626 Hz |  | +/-25 cents P1, +/-10 cents P2 | TBD temp/RH |  | Enlarge/undercut slowly to raise; wax or bushing recovery if sharp. |
| KAV-A3-7H | VAL-H3 | hole 3 offset +4 st | 277.183 Hz |  | +/-25 cents P1, +/-10 cents P2 | TBD temp/RH |  | Enlarge/undercut slowly to raise; wax or bushing recovery if sharp. |
| KAV-A3-7H | VAL-H4 | hole 4 offset +6 st | 311.127 Hz |  | +/-25 cents P1, +/-10 cents P2 | TBD temp/RH |  | Enlarge/undercut slowly to raise; wax or bushing recovery if sharp. |
| KAV-A3-7H | VAL-H5 | hole 5 offset +7 st | 329.628 Hz |  | +/-25 cents P1, +/-10 cents P2 | TBD temp/RH |  | Enlarge/undercut slowly to raise; wax or bushing recovery if sharp. |
| KAV-A3-7H | VAL-H6 | hole 6 offset +8 st | 349.228 Hz |  | +/-25 cents P1, +/-10 cents P2 | TBD temp/RH |  | Enlarge/undercut slowly to raise; wax or bushing recovery if sharp. |
| KAV-A3-7H | VAL-H7 | hole 7 offset +9 st | 369.994 Hz |  | +/-25 cents P1, +/-10 cents P2 | TBD temp/RH |  | Enlarge/undercut slowly to raise; wax or bushing recovery if sharp. |
| KAV-AS3-7H | VAL-ROOT | root A#3 | 233.082 Hz |  | +/-25 cents P1, +/-10 cents P2 | TBD temp/RH |  | Trim foot shorter to raise pitch; rebuild/extend foot if sharp. |
| KAV-AS3-7H | VAL-H1 | hole 1 offset +2 st | 261.626 Hz |  | +/-25 cents P1, +/-10 cents P2 | TBD temp/RH |  | Enlarge/undercut slowly to raise; wax or bushing recovery if sharp. |
| KAV-AS3-7H | VAL-H2 | hole 2 offset +3 st | 277.183 Hz |  | +/-25 cents P1, +/-10 cents P2 | TBD temp/RH |  | Enlarge/undercut slowly to raise; wax or bushing recovery if sharp. |
| KAV-AS3-7H | VAL-H3 | hole 3 offset +4 st | 293.665 Hz |  | +/-25 cents P1, +/-10 cents P2 | TBD temp/RH |  | Enlarge/undercut slowly to raise; wax or bushing recovery if sharp. |
| KAV-AS3-7H | VAL-H4 | hole 4 offset +6 st | 329.628 Hz |  | +/-25 cents P1, +/-10 cents P2 | TBD temp/RH |  | Enlarge/undercut slowly to raise; wax or bushing recovery if sharp. |
| KAV-AS3-7H | VAL-H5 | hole 5 offset +7 st | 349.228 Hz |  | +/-25 cents P1, +/-10 cents P2 | TBD temp/RH |  | Enlarge/undercut slowly to raise; wax or bushing recovery if sharp. |
| KAV-AS3-7H | VAL-H6 | hole 6 offset +8 st | 369.994 Hz |  | +/-25 cents P1, +/-10 cents P2 | TBD temp/RH |  | Enlarge/undercut slowly to raise; wax or bushing recovery if sharp. |
| KAV-AS3-7H | VAL-H7 | hole 7 offset +9 st | 391.995 Hz |  | +/-25 cents P1, +/-10 cents P2 | TBD temp/RH |  | Enlarge/undercut slowly to raise; wax or bushing recovery if sharp. |
| KAV-B3-7H | VAL-ROOT | root B3 | 246.942 Hz |  | +/-25 cents P1, +/-10 cents P2 | TBD temp/RH |  | Trim foot shorter to raise pitch; rebuild/extend foot if sharp. |
| KAV-B3-7H | VAL-H1 | hole 1 offset +2 st | 277.183 Hz |  | +/-25 cents P1, +/-10 cents P2 | TBD temp/RH |  | Enlarge/undercut slowly to raise; wax or bushing recovery if sharp. |
| KAV-B3-7H | VAL-H2 | hole 2 offset +3 st | 293.665 Hz |  | +/-25 cents P1, +/-10 cents P2 | TBD temp/RH |  | Enlarge/undercut slowly to raise; wax or bushing recovery if sharp. |
| KAV-B3-7H | VAL-H3 | hole 3 offset +4 st | 311.127 Hz |  | +/-25 cents P1, +/-10 cents P2 | TBD temp/RH |  | Enlarge/undercut slowly to raise; wax or bushing recovery if sharp. |
| KAV-B3-7H | VAL-H4 | hole 4 offset +6 st | 349.228 Hz |  | +/-25 cents P1, +/-10 cents P2 | TBD temp/RH |  | Enlarge/undercut slowly to raise; wax or bushing recovery if sharp. |
| KAV-B3-7H | VAL-H5 | hole 5 offset +7 st | 369.994 Hz |  | +/-25 cents P1, +/-10 cents P2 | TBD temp/RH |  | Enlarge/undercut slowly to raise; wax or bushing recovery if sharp. |
| KAV-B3-7H | VAL-H6 | hole 6 offset +8 st | 391.995 Hz |  | +/-25 cents P1, +/-10 cents P2 | TBD temp/RH |  | Enlarge/undercut slowly to raise; wax or bushing recovery if sharp. |
| KAV-B3-7H | VAL-H7 | hole 7 offset +9 st | 415.305 Hz |  | +/-25 cents P1, +/-10 cents P2 | TBD temp/RH |  | Enlarge/undercut slowly to raise; wax or bushing recovery if sharp. |
| ALG-AS3-J2 | VAL-ROOT | root A#3 | 233.082 Hz |  | +/-25 cents P1, +/-10 cents P2 | TBD temp/RH |  | Trim foot shorter to raise pitch; rebuild/extend foot if sharp. |
| ALG-AS3-J2 | VAL-H1 | hole 1 offset +2 st | 261.626 Hz |  | +/-25 cents P1, +/-10 cents P2 | TBD temp/RH |  | Enlarge/undercut slowly to raise; wax or bushing recovery if sharp. |
| ALG-AS3-J2 | VAL-H2 | hole 2 offset +4 st | 293.665 Hz |  | +/-25 cents P1, +/-10 cents P2 | TBD temp/RH |  | Enlarge/undercut slowly to raise; wax or bushing recovery if sharp. |
| ALG-AS3-J2 | VAL-H3 | hole 3 offset +7 st | 349.228 Hz |  | +/-25 cents P1, +/-10 cents P2 | TBD temp/RH |  | Enlarge/undercut slowly to raise; wax or bushing recovery if sharp. |
| ALG-AS3-J2 | VAL-H4 | hole 4 offset +9 st | 391.995 Hz |  | +/-25 cents P1, +/-10 cents P2 | TBD temp/RH |  | Enlarge/undercut slowly to raise; wax or bushing recovery if sharp. |
| ALG-AS3-J2 | VAL-H5 | hole 5 offset +11 st | 440.0 Hz |  | +/-25 cents P1, +/-10 cents P2 | TBD temp/RH |  | Enlarge/undercut slowly to raise; wax or bushing recovery if sharp. |
| ALG-AS3-J2 | VAL-H6 | hole 6 offset +12 st | 466.164 Hz |  | +/-25 cents P1, +/-10 cents P2 | TBD temp/RH |  | Enlarge/undercut slowly to raise; wax or bushing recovery if sharp. |
| ALG-AS3-SOLID | VAL-ROOT | root A#3 | 233.082 Hz |  | +/-25 cents P1, +/-10 cents P2 | TBD temp/RH |  | Trim foot shorter to raise pitch; rebuild/extend foot if sharp. |
| ALG-AS3-SOLID | VAL-H1 | hole 1 offset +2 st | 261.626 Hz |  | +/-25 cents P1, +/-10 cents P2 | TBD temp/RH |  | Enlarge/undercut slowly to raise; wax or bushing recovery if sharp. |
| ALG-AS3-SOLID | VAL-H2 | hole 2 offset +4 st | 293.665 Hz |  | +/-25 cents P1, +/-10 cents P2 | TBD temp/RH |  | Enlarge/undercut slowly to raise; wax or bushing recovery if sharp. |
| ALG-AS3-SOLID | VAL-H3 | hole 3 offset +7 st | 349.228 Hz |  | +/-25 cents P1, +/-10 cents P2 | TBD temp/RH |  | Enlarge/undercut slowly to raise; wax or bushing recovery if sharp. |
| ALG-AS3-SOLID | VAL-H4 | hole 4 offset +9 st | 391.995 Hz |  | +/-25 cents P1, +/-10 cents P2 | TBD temp/RH |  | Enlarge/undercut slowly to raise; wax or bushing recovery if sharp. |
| ALG-AS3-SOLID | VAL-H5 | hole 5 offset +11 st | 440.0 Hz |  | +/-25 cents P1, +/-10 cents P2 | TBD temp/RH |  | Enlarge/undercut slowly to raise; wax or bushing recovery if sharp. |
| ALG-AS3-SOLID | VAL-H6 | hole 6 offset +12 st | 466.164 Hz |  | +/-25 cents P1, +/-10 cents P2 | TBD temp/RH |  | Enlarge/undercut slowly to raise; wax or bushing recovery if sharp. |
| ALG-A3-J3 | VAL-ROOT | root A3 | 220.000 Hz |  | +/-25 cents P1, +/-10 cents P2 | TBD temp/RH |  | Trim foot shorter to raise pitch; rebuild/extend foot if sharp. |
| ALG-A3-J3 | VAL-H1 | hole 1 offset +2 st | 246.942 Hz |  | +/-25 cents P1, +/-10 cents P2 | TBD temp/RH |  | Enlarge/undercut slowly to raise; wax or bushing recovery if sharp. |
| ALG-A3-J3 | VAL-H2 | hole 2 offset +4 st | 277.183 Hz |  | +/-25 cents P1, +/-10 cents P2 | TBD temp/RH |  | Enlarge/undercut slowly to raise; wax or bushing recovery if sharp. |
| ALG-A3-J3 | VAL-H3 | hole 3 offset +7 st | 329.628 Hz |  | +/-25 cents P1, +/-10 cents P2 | TBD temp/RH |  | Enlarge/undercut slowly to raise; wax or bushing recovery if sharp. |
| ALG-A3-J3 | VAL-H4 | hole 4 offset +9 st | 369.994 Hz |  | +/-25 cents P1, +/-10 cents P2 | TBD temp/RH |  | Enlarge/undercut slowly to raise; wax or bushing recovery if sharp. |
| ALG-A3-J3 | VAL-H5 | hole 5 offset +11 st | 415.305 Hz |  | +/-25 cents P1, +/-10 cents P2 | TBD temp/RH |  | Enlarge/undercut slowly to raise; wax or bushing recovery if sharp. |
| ALG-A3-J3 | VAL-H6 | hole 6 offset +12 st | 440.0 Hz |  | +/-25 cents P1, +/-10 cents P2 | TBD temp/RH |  | Enlarge/undercut slowly to raise; wax or bushing recovery if sharp. |
| ALG-B3-SOLID | VAL-ROOT | root B3 | 246.942 Hz |  | +/-25 cents P1, +/-10 cents P2 | TBD temp/RH |  | Trim foot shorter to raise pitch; rebuild/extend foot if sharp. |
| ALG-B3-SOLID | VAL-H1 | hole 1 offset +2 st | 277.183 Hz |  | +/-25 cents P1, +/-10 cents P2 | TBD temp/RH |  | Enlarge/undercut slowly to raise; wax or bushing recovery if sharp. |
| ALG-B3-SOLID | VAL-H2 | hole 2 offset +4 st | 311.127 Hz |  | +/-25 cents P1, +/-10 cents P2 | TBD temp/RH |  | Enlarge/undercut slowly to raise; wax or bushing recovery if sharp. |
| ALG-B3-SOLID | VAL-H3 | hole 3 offset +7 st | 369.994 Hz |  | +/-25 cents P1, +/-10 cents P2 | TBD temp/RH |  | Enlarge/undercut slowly to raise; wax or bushing recovery if sharp. |
| ALG-B3-SOLID | VAL-H4 | hole 4 offset +9 st | 415.305 Hz |  | +/-25 cents P1, +/-10 cents P2 | TBD temp/RH |  | Enlarge/undercut slowly to raise; wax or bushing recovery if sharp. |
| ALG-B3-SOLID | VAL-H5 | hole 5 offset +11 st | 466.164 Hz |  | +/-25 cents P1, +/-10 cents P2 | TBD temp/RH |  | Enlarge/undercut slowly to raise; wax or bushing recovery if sharp. |
| ALG-B3-SOLID | VAL-H6 | hole 6 offset +12 st | 493.883 Hz |  | +/-25 cents P1, +/-10 cents P2 | TBD temp/RH |  | Enlarge/undercut slowly to raise; wax or bushing recovery if sharp. |
| ALL | VAL-FIPPLE | clean attack and stable octave jump | no choking at normal breath |  | subjective plus recording | TBD temp/RH |  | Adjust windway height, splitting edge sharpness, and window length. |
| DOUBLE | VAL-DRONE-BEAT | melody/drone pressure interaction | no severe stealing or beating unless intentional |  | recorded comparison | TBD temp/RH |  | Restrict windway, retune drone vent, or separate mouth inlets. |

<div class="page-break"></div>

## supplier-rfq.md

Supplier email/request-for-quote starter.

# Supplier RFQ Draft

Subject: Quote request for straight-grain woodwind blanks and optional ferrule stock

Hello,

I am building a small run of long fipple flutes and need stable straight-grain blanks suitable for bored woodwind bodies.

Please quote the following:

- 4 to 8 blanks, 1.25 to 1.50 in square or round, 30 to 38 in long.
- Species options: elder, locust, ash, maple, cherry, walnut, or similar stable hardwood.
- Moisture content and straightness/grain-runout information.
- Any longer stock suitable for 85-90 cm flute bodies.
- Optional thin-wall brass tube or hardwood ferrule stock around 1.25 to 1.40 in ID/OD range.

The blanks will be drilled or split-routed along the long axis, then turned and tuned, so straight grain and low checking risk matter more than figure.

Please include unit price, volume price, lead time, shipping estimate, and any recommended substitutes.

Thank you,
Tony Koop

<div class="page-break"></div>

## visual-bom-brief.md

Art direction for an image-forward visual BOM.

# Visual BOM Brief

Create one image-forward BOM plate with:

- hero view of a kaval, an Alghosazi, and the fipple-head section;
- item rows for body blank, fipple plug, cork/ferrule, drilling template, finish, and validation tools;
- callouts that distinguish make vs buy parts;
- source status labels: verified price, spec only, or shop stock.

Image sources:

- Use real shop photos after P0/P1 prototypes exist.
- Until then, use `images/hero.png` and the SVG drawings as concept placeholders.
- Do not use vendor or Fujara Flutes photos directly in the BOM without permission.

<div class="page-break"></div>

## wolfram-starter.wl

Wolfram starter for physics, optimization, visualization, and validation.

```wolfram
(* Kaval + Alghosazi starter. Full v4.2 packet source is in wolfram/instrument-model.wl after generation. *)
ClearAll["Global`*"];
cInPerSec = 13552;
freqFromMidi[midi_, a4_: 440] := a4*2^((midi - 69)/12);
openPipeLeff[f_] := cInPerSec/(2*f);
holeFromLabium[labiumToFoot_, semitoneOffset_] := labiumToFoot*2^(-semitoneOffset/12);
centsError[measured_, target_] := 1200*Log[2, measured/target];
```

<div class="page-break"></div>

## README.md

Project artifact.

# Kaval + Alghosazi Fipple Flutes

This repository is a build-ready design packet for two related long fipple flutes:

- a **Moldavian/Romanian-style fipple kaval** family, including 5-hole, 7-hole, two-piece, and double-drone options;
- a **fipple Alghosazi** family inspired by the Anasazi/Basketmaker long-flute lineage, with an easier fipple head and a rear thumb hole.

The head design intentionally borrows from Tony's `fujara` CAD: the player blows into an end mouth inlet, the air travels through a controlled internal flue, and sound is made at a side **true sound window** and splitting edge. The head is not copied from a commercial maker; it is a Tony-shop fujara/NAF hybrid that can be tuned and rebuilt.

## Build First

Start with these prototypes:

| Prototype | Why |
| --- | --- |
| `KAV-A3-5H` | Best first kaval: published 74 cm precedent, forgiving length, 5-hole pattern. |
| `ALG-AS3-J2` | Best first Alghosazi: published 82 cm two-piece precedent, thumb-hole layout. |
| `P0-FIPPLE-HEAD` | Scrap head tile that proves the mouth inlet, flue, window, and splitting edge before a full body. |

## File Map

| File | Use |
| --- | --- |
| `Kaval-Alghosazi-Design.xlsx` | Parametric workbook: family spec, formulas, hole schedules, fipple inputs. |
| `design.md` | Acoustic model, cultural/source notes, assumptions, and build intent. |
| `family-spec.csv` | Row-per-member design table used by drawing/CAD generators. |
| `hole-schedule.csv` | First-pass hole positions measured from labium and foot. |
| `bom.csv`, `sourcing.csv`, `cut-list.csv` | Procurement and stock prep. |
| `assembly-manual.md` | Shop sequence from fipple tile through tuning. |
| `drawings/` | SVG manufacturing drawings and head/joint details. |
| `cad/` | OpenSCAD and SolidWorks starter handoff files. |
| `cnc/` | v4.2 operation plan and setup sheet. |
| `validation.csv` | Tuning and empirical correction log. |
| `capstone-deck.pptx`, `print-packet.pdf`, `site/index.html` | Presentation, shop print, and build-log deliverables. |

## Status

This is a first-pass engineering packet. Dimensions are parametric and source-backed where possible, but the fipple/sound-window correction is marked as a measured-prototype variable, not a borrowed NAF K2 correction.

## Attribution

The kaval references come from Moldavian/Romanian shepherd-flute practice; the Alghosazi references point toward Anasazi/Basketmaker flute replicas and contemporary adaptations. This packet is a modern shop design by Tony Koop, built with respect for those lineages and explicit source notes in `sources.md`.

<div class="page-break"></div>

## alghosazi-hole-schedule.csv

Project artifact.

| member_id | instrument | hole_no_from_foot | offset_st | target_hz | x_from_labium_in | x_from_foot_in | starter_drill_in | target_final_dia_in | orientation | formula |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ALG-AS3-J2 | Fipple Alghosazi | 1 | 2 | 261.626 | 27.158 | 3.326 | 0.1875 | 0.2500 | front | x_from_labium = labium_to_foot * 2^(-offset_st/12); tune upward by enlarging |
| ALG-AS3-J2 | Fipple Alghosazi | 2 | 4 | 293.665 | 24.195 | 6.289 | 0.1875 | 0.2500 | front | x_from_labium = labium_to_foot * 2^(-offset_st/12); tune upward by enlarging |
| ALG-AS3-J2 | Fipple Alghosazi | 3 | 7 | 349.228 | 20.345 | 10.138 | 0.1875 | 0.2500 | front | x_from_labium = labium_to_foot * 2^(-offset_st/12); tune upward by enlarging |
| ALG-AS3-J2 | Fipple Alghosazi | 4 | 9 | 391.995 | 18.126 | 12.358 | 0.2188 | 0.3125 | front | x_from_labium = labium_to_foot * 2^(-offset_st/12); tune upward by enlarging |
| ALG-AS3-J2 | Fipple Alghosazi | 5 | 11 | 440.0 | 16.148 | 14.335 | 0.2188 | 0.3125 | front | x_from_labium = labium_to_foot * 2^(-offset_st/12); tune upward by enlarging |
| ALG-AS3-J2 | Fipple Alghosazi | 6 | 12 | 466.164 | 15.242 | 15.242 | 0.2188 | 0.3125 | back thumb | x_from_labium = labium_to_foot * 2^(-offset_st/12); tune upward by enlarging |
| ALG-AS3-SOLID | Fipple Alghosazi | 1 | 2 | 261.626 | 28.21 | 3.455 | 0.1875 | 0.2500 | front | x_from_labium = labium_to_foot * 2^(-offset_st/12); tune upward by enlarging |
| ALG-AS3-SOLID | Fipple Alghosazi | 2 | 4 | 293.665 | 25.132 | 6.532 | 0.1875 | 0.2500 | front | x_from_labium = labium_to_foot * 2^(-offset_st/12); tune upward by enlarging |
| ALG-AS3-SOLID | Fipple Alghosazi | 3 | 7 | 349.228 | 21.134 | 10.531 | 0.1875 | 0.2500 | front | x_from_labium = labium_to_foot * 2^(-offset_st/12); tune upward by enlarging |
| ALG-AS3-SOLID | Fipple Alghosazi | 4 | 9 | 391.995 | 18.828 | 12.837 | 0.2188 | 0.3125 | front | x_from_labium = labium_to_foot * 2^(-offset_st/12); tune upward by enlarging |
| ALG-AS3-SOLID | Fipple Alghosazi | 5 | 11 | 440.0 | 16.774 | 14.891 | 0.2188 | 0.3125 | front | x_from_labium = labium_to_foot * 2^(-offset_st/12); tune upward by enlarging |
| ALG-AS3-SOLID | Fipple Alghosazi | 6 | 12 | 466.164 | 15.832 | 15.832 | 0.2188 | 0.3125 | back thumb | x_from_labium = labium_to_foot * 2^(-offset_st/12); tune upward by enlarging |
| ALG-A3-J3 | Fipple Alghosazi | 1 | 2 | 246.942 | 24.045 | 2.945 | 0.1875 | 0.2500 | front | x_from_labium = labium_to_foot * 2^(-offset_st/12); tune upward by enlarging |
| ALG-A3-J3 | Fipple Alghosazi | 2 | 4 | 277.183 | 21.422 | 5.568 | 0.1875 | 0.2500 | front | x_from_labium = labium_to_foot * 2^(-offset_st/12); tune upward by enlarging |
| ALG-A3-J3 | Fipple Alghosazi | 3 | 7 | 329.628 | 18.014 | 8.976 | 0.1875 | 0.2500 | front | x_from_labium = labium_to_foot * 2^(-offset_st/12); tune upward by enlarging |
| ALG-A3-J3 | Fipple Alghosazi | 4 | 9 | 369.994 | 16.048 | 10.942 | 0.2188 | 0.3125 | front | x_from_labium = labium_to_foot * 2^(-offset_st/12); tune upward by enlarging |
| ALG-A3-J3 | Fipple Alghosazi | 5 | 11 | 415.305 | 14.298 | 12.693 | 0.2188 | 0.3125 | front | x_from_labium = labium_to_foot * 2^(-offset_st/12); tune upward by enlarging |
| ALG-A3-J3 | Fipple Alghosazi | 6 | 12 | 440.0 | 13.495 | 13.495 | 0.2188 | 0.3125 | back thumb | x_from_labium = labium_to_foot * 2^(-offset_st/12); tune upward by enlarging |
| ALG-B3-SOLID | Fipple Alghosazi | 1 | 2 | 277.183 | 23.082 | 2.827 | 0.1875 | 0.2500 | front | x_from_labium = labium_to_foot * 2^(-offset_st/12); tune upward by enlarging |
| ALG-B3-SOLID | Fipple Alghosazi | 2 | 4 | 311.127 | 20.564 | 5.345 | 0.1875 | 0.2500 | front | x_from_labium = labium_to_foot * 2^(-offset_st/12); tune upward by enlarging |
| ALG-B3-SOLID | Fipple Alghosazi | 3 | 7 | 369.994 | 17.292 | 8.617 | 0.1875 | 0.2500 | front | x_from_labium = labium_to_foot * 2^(-offset_st/12); tune upward by enlarging |
| ALG-B3-SOLID | Fipple Alghosazi | 4 | 9 | 415.305 | 15.406 | 10.503 | 0.2188 | 0.3125 | front | x_from_labium = labium_to_foot * 2^(-offset_st/12); tune upward by enlarging |
| ALG-B3-SOLID | Fipple Alghosazi | 5 | 11 | 466.164 | 13.725 | 12.184 | 0.2188 | 0.3125 | front | x_from_labium = labium_to_foot * 2^(-offset_st/12); tune upward by enlarging |
| ALG-B3-SOLID | Fipple Alghosazi | 6 | 12 | 493.883 | 12.955 | 12.955 | 0.2188 | 0.3125 | back thumb | x_from_labium = labium_to_foot * 2^(-offset_st/12); tune upward by enlarging |

<div class="page-break"></div>

## double-drone-spec.csv

Project artifact.

| assembly_id | melody_side | drone_side | windways | body_strategy | overall_length_in | validation |
| --- | --- | --- | --- | --- | --- | --- |
| KAVGH-A3-DOUBLE | KAV-A3-5H | A3 drone with rear thumb vent raising to B3 | 2 | two separate bores lashed or mechanically joined; melody kaval removable | 29.1 to 31.0 | Tune melody alone, drone alone, then both together for beating and pressure interaction. |
| DALG-AS3-DOUBLE | ALG-AS3-J2 or ALG-AS3-SOLID | reedy/natural-harmonic drone bore with independent windway | 2 | parallel-tube double flute with two mouth inlets; each side playable separately | 33.1 | Record both windways independently and together; check pressure stealing between ducts. |

<div class="page-break"></div>

## family-spec.csv

Project artifact.

| member_id | instrument | subtype | target_note | target_hz | midi | scale_label | hole_count | hole_offsets_st | bore_id_in | body_od_in | wall_in | total_length_cm | total_length_in | top_to_window_in | labium_to_foot_in | open_pipe_leff_in | estimated_sound_window_correction_in | tuning_delta_interpretation | chamber_to_bore | wood_species | construction | source_basis | done_bar_ref | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| KAV-GS3-5H | Fipple Kaval | 5-hole Moldavian/Romanian | G#3 | 207.652 | 56 | Kaval gypsy mode: 0,2,3,6,7,8 semitones | 5 | 2 3 6 7 8 | 0.8750 | 1.3750 | 0.2500 | 79.0 | 31.102 | 1.600 | 29.502 | 32.631 | 3.129 | positive: needs fipple/window end correction or added acoustic length | 33.7 | Locust or elder | solid or split blank; optional two-piece joint | Fujara Flutes observed G# kaval length 79 cm | fujara + flutes + pistalka | Longest 5-hole starter; use as low-voice reference. |
| KAV-A3-5H | Fipple Kaval | 5-hole Moldavian/Romanian | A3 | 220.000 | 57 | Kaval gypsy mode: 0,2,3,6,7,8 semitones | 5 | 2 3 6 7 8 | 0.8750 | 1.3750 | 0.2500 | 74.0 | 29.134 | 1.600 | 27.534 | 30.800 | 3.266 | positive: needs fipple/window end correction or added acoustic length | 31.5 | Elder | two-piece optional hand-cut joint | Fujara Flutes observed A kaval length 74 cm | fujara + flutes + pistalka | Recommended first kaval because length, bore, and hand span are forgiving. |
| KAV-B3-5H | Fipple Kaval | 5-hole Moldavian/Romanian | B3 | 246.942 | 59 | Kaval gypsy mode: 0,2,3,6,7,8 semitones | 5 | 2 3 6 7 8 | 0.8125 | 1.3125 | 0.2500 | 67.0 | 26.378 | 1.500 | 24.878 | 27.440 | 2.562 | positive: needs fipple/window end correction or added acoustic length | 30.6 | Elder | solid split blank | Fujara Flutes observed B kaval length 67 cm | fujara + flutes + pistalka | Compact 5-hole version; tighter fipple tolerances. |
| KAV-C4-5H | Fipple Kaval | 5-hole Moldavian/Romanian | C4 | 261.626 | 60 | Kaval gypsy mode: 0,2,3,6,7,8 semitones | 5 | 2 3 6 7 8 | 0.7500 | 1.2500 | 0.2500 | 62.0 | 24.409 | 1.450 | 22.959 | 25.900 | 2.940 | positive: needs fipple/window end correction or added acoustic length | 30.6 | Elder, maple, or cherry | solid split blank | Fujara Flutes observed C kaval length 62 cm | fujara + flutes + pistalka | Smallest 5-hole kaval; good for fipple/head trials. |
| KAV-A3-7H | Fipple Kaval | 7-hole expanded Moldavian | A3 | 220.000 | 57 | Expanded kaval: 0,2,3,4,6,7,8,9 semitones | 7 | 2 3 4 6 7 8 9 | 0.8750 | 1.4000 | 0.2625 | 90.0 | 35.433 | 1.650 | 33.783 | 30.800 | -2.983 | negative: observed source length is overlong for this nominal root; trim foot or reassess key naming | 38.6 | Elder | solid split blank | Fujara Flutes observed 7-hole A kaval length 90 cm | fujara + flutes + pistalka | Expanded note set; lower holes may be covered with finger bases. |
| KAV-AS3-7H | Fipple Kaval | 7-hole expanded Moldavian | A#3 | 233.082 | 58 | Expanded kaval: 0,2,3,4,6,7,8,9 semitones | 7 | 2 3 4 6 7 8 9 | 0.8750 | 1.4000 | 0.2625 | 85.0 | 33.465 | 1.650 | 31.815 | 29.071 | -2.743 | negative: observed source length is overlong for this nominal root; trim foot or reassess key naming | 36.4 | Dogwood or elder | two-piece optional hand-cut joint | Fujara Flutes observed 7-hole A# kaval length 85 cm | fujara + flutes + pistalka | Good two-piece test because the published example is collapsible. |
| KAV-B3-7H | Fipple Kaval | 7-hole expanded Moldavian | B3 | 246.942 | 59 | Expanded kaval: 0,2,3,4,6,7,8,9 semitones | 7 | 2 3 4 6 7 8 9 | 0.8125 | 1.3125 | 0.2500 | 69.0 | 27.165 | 1.500 | 25.665 | 27.440 | 1.774 | positive: needs fipple/window end correction or added acoustic length | 31.6 | Elder | solid split blank | Fujara Flutes observed 7-hole B kaval length 69 cm | fujara + flutes + pistalka | Compact 7-hole version; validate hand position before final hole diameters. |
| ALG-AS3-J2 | Fipple Alghosazi | Anasazi-derived with thumb hole | A#3 | 233.082 | 58 | Anasazi-derived: 0,2,4,7,9,11,12 semitones | 6 | 2 4 7 9 11 12 | 0.8750 | 1.3750 | 0.2500 | 82.0 | 32.283 | 1.800 | 30.483 | 29.071 | -1.412 | negative: observed source length is overlong for this nominal root; trim foot or reassess key naming | 34.8 | Ash | two-piece hand-cut joint | Fujara Flutes observed A# Alghosazi length 82 cm | fujara + flutes + pistalka | Recommended first Alghosazi; published example uses a collapsible joint. |
| ALG-AS3-SOLID | Fipple Alghosazi | Anasazi-derived with thumb hole | A#3 | 233.082 | 58 | Anasazi-derived: 0,2,4,7,9,11,12 semitones | 6 | 2 4 7 9 11 12 | 0.8750 | 1.3750 | 0.2500 | 85.0 | 33.465 | 1.800 | 31.665 | 29.071 | -2.593 | negative: observed source length is overlong for this nominal root; trim foot or reassess key naming | 36.2 | Locust | solid split blank | Fujara Flutes observed solid A# Alghosazi length 85 cm | fujara + flutes + pistalka | Solid-body alternate for comparing joint vs no-joint response. |
| ALG-A3-J3 | Fipple Alghosazi | Anasazi-derived with thumb hole | A3 | 220.000 | 57 | Anasazi-derived: 0,2,4,7,9,11,12 semitones | 6 | 2 4 7 9 11 12 | 0.8750 | 1.3750 | 0.2500 | 73.0 | 28.740 | 1.750 | 26.990 | 30.800 | 3.810 | positive: needs fipple/window end correction or added acoustic length | 30.8 | Oak | three-piece hand-cut joint | Fujara Flutes observed A Alghosazi length 73 cm | fujara + flutes + pistalka | Use as the modular joint stress test. |
| ALG-B3-SOLID | Fipple Alghosazi | Anasazi-derived with thumb hole | B3 | 246.942 | 59 | Anasazi-derived: 0,2,4,7,9,11,12 semitones | 6 | 2 4 7 9 11 12 | 0.8125 | 1.3125 | 0.2500 | 70.0 | 27.559 | 1.650 | 25.909 | 27.440 | 1.531 | positive: needs fipple/window end correction or added acoustic length | 31.9 | Elder or maple | solid split blank | Fujara Flutes observed B Alghosazi length 70 cm | fujara + flutes + pistalka | Compact Alghosazi; top thumb hole needs ergonomic mockup. |

<div class="page-break"></div>

## hole-schedule.csv

Project artifact.

| member_id | instrument | hole_no_from_foot | offset_st | target_hz | x_from_labium_in | x_from_foot_in | starter_drill_in | target_final_dia_in | orientation | formula |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| KAV-GS3-5H | Fipple Kaval | 1 | 2 | 233.082 | 26.284 | 3.219 | 0.1875 | 0.2500 | front | x_from_labium = labium_to_foot * 2^(-offset_st/12); tune upward by enlarging |
| KAV-GS3-5H | Fipple Kaval | 2 | 3 | 246.942 | 24.808 | 4.694 | 0.1875 | 0.2500 | front | x_from_labium = labium_to_foot * 2^(-offset_st/12); tune upward by enlarging |
| KAV-GS3-5H | Fipple Kaval | 3 | 6 | 293.665 | 20.861 | 8.641 | 0.2188 | 0.3000 | front | x_from_labium = labium_to_foot * 2^(-offset_st/12); tune upward by enlarging |
| KAV-GS3-5H | Fipple Kaval | 4 | 7 | 311.127 | 19.69 | 9.812 | 0.2188 | 0.3000 | front | x_from_labium = labium_to_foot * 2^(-offset_st/12); tune upward by enlarging |
| KAV-GS3-5H | Fipple Kaval | 5 | 8 | 329.628 | 18.585 | 10.917 | 0.2188 | 0.3000 | front | x_from_labium = labium_to_foot * 2^(-offset_st/12); tune upward by enlarging |
| KAV-A3-5H | Fipple Kaval | 1 | 2 | 246.942 | 24.53 | 3.004 | 0.1875 | 0.2500 | front | x_from_labium = labium_to_foot * 2^(-offset_st/12); tune upward by enlarging |
| KAV-A3-5H | Fipple Kaval | 2 | 3 | 261.626 | 23.153 | 4.381 | 0.1875 | 0.2500 | front | x_from_labium = labium_to_foot * 2^(-offset_st/12); tune upward by enlarging |
| KAV-A3-5H | Fipple Kaval | 3 | 6 | 311.127 | 19.469 | 8.064 | 0.2188 | 0.3000 | front | x_from_labium = labium_to_foot * 2^(-offset_st/12); tune upward by enlarging |
| KAV-A3-5H | Fipple Kaval | 4 | 7 | 329.628 | 18.377 | 9.157 | 0.2188 | 0.3000 | front | x_from_labium = labium_to_foot * 2^(-offset_st/12); tune upward by enlarging |
| KAV-A3-5H | Fipple Kaval | 5 | 8 | 349.228 | 17.345 | 10.189 | 0.2188 | 0.3000 | front | x_from_labium = labium_to_foot * 2^(-offset_st/12); tune upward by enlarging |
| KAV-B3-5H | Fipple Kaval | 1 | 2 | 277.183 | 22.164 | 2.714 | 0.1875 | 0.2500 | front | x_from_labium = labium_to_foot * 2^(-offset_st/12); tune upward by enlarging |
| KAV-B3-5H | Fipple Kaval | 2 | 3 | 293.665 | 20.92 | 3.958 | 0.1875 | 0.2500 | front | x_from_labium = labium_to_foot * 2^(-offset_st/12); tune upward by enlarging |
| KAV-B3-5H | Fipple Kaval | 3 | 6 | 349.228 | 17.591 | 7.287 | 0.2188 | 0.3000 | front | x_from_labium = labium_to_foot * 2^(-offset_st/12); tune upward by enlarging |
| KAV-B3-5H | Fipple Kaval | 4 | 7 | 369.994 | 16.604 | 8.274 | 0.2188 | 0.3000 | front | x_from_labium = labium_to_foot * 2^(-offset_st/12); tune upward by enlarging |
| KAV-B3-5H | Fipple Kaval | 5 | 8 | 391.995 | 15.672 | 9.206 | 0.2188 | 0.3000 | front | x_from_labium = labium_to_foot * 2^(-offset_st/12); tune upward by enlarging |
| KAV-C4-5H | Fipple Kaval | 1 | 2 | 293.665 | 20.455 | 2.505 | 0.1875 | 0.2500 | front | x_from_labium = labium_to_foot * 2^(-offset_st/12); tune upward by enlarging |
| KAV-C4-5H | Fipple Kaval | 2 | 3 | 311.127 | 19.307 | 3.653 | 0.1875 | 0.2500 | front | x_from_labium = labium_to_foot * 2^(-offset_st/12); tune upward by enlarging |
| KAV-C4-5H | Fipple Kaval | 3 | 6 | 369.994 | 16.235 | 6.725 | 0.2188 | 0.3000 | front | x_from_labium = labium_to_foot * 2^(-offset_st/12); tune upward by enlarging |
| KAV-C4-5H | Fipple Kaval | 4 | 7 | 391.995 | 15.324 | 7.636 | 0.2188 | 0.3000 | front | x_from_labium = labium_to_foot * 2^(-offset_st/12); tune upward by enlarging |
| KAV-C4-5H | Fipple Kaval | 5 | 8 | 415.305 | 14.464 | 8.496 | 0.2188 | 0.3000 | front | x_from_labium = labium_to_foot * 2^(-offset_st/12); tune upward by enlarging |
| KAV-A3-7H | Fipple Kaval | 1 | 2 | 246.942 | 30.097 | 3.686 | 0.1875 | 0.2500 | front | x_from_labium = labium_to_foot * 2^(-offset_st/12); tune upward by enlarging |
| KAV-A3-7H | Fipple Kaval | 2 | 3 | 261.626 | 28.408 | 5.375 | 0.1875 | 0.2500 | front | x_from_labium = labium_to_foot * 2^(-offset_st/12); tune upward by enlarging |
| KAV-A3-7H | Fipple Kaval | 3 | 4 | 277.183 | 26.814 | 6.969 | 0.2188 | 0.3000 | front | x_from_labium = labium_to_foot * 2^(-offset_st/12); tune upward by enlarging |
| KAV-A3-7H | Fipple Kaval | 4 | 6 | 311.127 | 23.888 | 9.895 | 0.2188 | 0.3000 | front | x_from_labium = labium_to_foot * 2^(-offset_st/12); tune upward by enlarging |
| KAV-A3-7H | Fipple Kaval | 5 | 7 | 329.628 | 22.547 | 11.236 | 0.2188 | 0.3000 | front | x_from_labium = labium_to_foot * 2^(-offset_st/12); tune upward by enlarging |
| KAV-A3-7H | Fipple Kaval | 6 | 8 | 349.228 | 21.282 | 12.501 | 0.2188 | 0.3000 | front | x_from_labium = labium_to_foot * 2^(-offset_st/12); tune upward by enlarging |
| KAV-A3-7H | Fipple Kaval | 7 | 9 | 369.994 | 20.088 | 13.696 | 0.2188 | 0.3000 | front | x_from_labium = labium_to_foot * 2^(-offset_st/12); tune upward by enlarging |
| KAV-AS3-7H | Fipple Kaval | 1 | 2 | 261.626 | 28.344 | 3.471 | 0.1875 | 0.2500 | front | x_from_labium = labium_to_foot * 2^(-offset_st/12); tune upward by enlarging |
| KAV-AS3-7H | Fipple Kaval | 2 | 3 | 277.183 | 26.753 | 5.062 | 0.1875 | 0.2500 | front | x_from_labium = labium_to_foot * 2^(-offset_st/12); tune upward by enlarging |
| KAV-AS3-7H | Fipple Kaval | 3 | 4 | 293.665 | 25.251 | 6.563 | 0.2188 | 0.3000 | front | x_from_labium = labium_to_foot * 2^(-offset_st/12); tune upward by enlarging |
| KAV-AS3-7H | Fipple Kaval | 4 | 6 | 329.628 | 22.496 | 9.318 | 0.2188 | 0.3000 | front | x_from_labium = labium_to_foot * 2^(-offset_st/12); tune upward by enlarging |
| KAV-AS3-7H | Fipple Kaval | 5 | 7 | 349.228 | 21.234 | 10.581 | 0.2188 | 0.3000 | front | x_from_labium = labium_to_foot * 2^(-offset_st/12); tune upward by enlarging |
| KAV-AS3-7H | Fipple Kaval | 6 | 8 | 369.994 | 20.042 | 11.773 | 0.2188 | 0.3000 | front | x_from_labium = labium_to_foot * 2^(-offset_st/12); tune upward by enlarging |
| KAV-AS3-7H | Fipple Kaval | 7 | 9 | 391.995 | 18.917 | 12.898 | 0.2188 | 0.3000 | front | x_from_labium = labium_to_foot * 2^(-offset_st/12); tune upward by enlarging |
| KAV-B3-7H | Fipple Kaval | 1 | 2 | 277.183 | 22.865 | 2.8 | 0.1875 | 0.2500 | front | x_from_labium = labium_to_foot * 2^(-offset_st/12); tune upward by enlarging |
| KAV-B3-7H | Fipple Kaval | 2 | 3 | 293.665 | 21.582 | 4.083 | 0.1875 | 0.2500 | front | x_from_labium = labium_to_foot * 2^(-offset_st/12); tune upward by enlarging |
| KAV-B3-7H | Fipple Kaval | 3 | 4 | 311.127 | 20.371 | 5.295 | 0.2188 | 0.3000 | front | x_from_labium = labium_to_foot * 2^(-offset_st/12); tune upward by enlarging |
| KAV-B3-7H | Fipple Kaval | 4 | 6 | 349.228 | 18.148 | 7.517 | 0.2188 | 0.3000 | front | x_from_labium = labium_to_foot * 2^(-offset_st/12); tune upward by enlarging |
| KAV-B3-7H | Fipple Kaval | 5 | 7 | 369.994 | 17.13 | 8.536 | 0.2188 | 0.3000 | front | x_from_labium = labium_to_foot * 2^(-offset_st/12); tune upward by enlarging |
| KAV-B3-7H | Fipple Kaval | 6 | 8 | 391.995 | 16.168 | 9.497 | 0.2188 | 0.3000 | front | x_from_labium = labium_to_foot * 2^(-offset_st/12); tune upward by enlarging |
| KAV-B3-7H | Fipple Kaval | 7 | 9 | 415.305 | 15.261 | 10.405 | 0.2188 | 0.3000 | front | x_from_labium = labium_to_foot * 2^(-offset_st/12); tune upward by enlarging |
| ALG-AS3-J2 | Fipple Alghosazi | 1 | 2 | 261.626 | 27.158 | 3.326 | 0.1875 | 0.2500 | front | x_from_labium = labium_to_foot * 2^(-offset_st/12); tune upward by enlarging |
| ALG-AS3-J2 | Fipple Alghosazi | 2 | 4 | 293.665 | 24.195 | 6.289 | 0.1875 | 0.2500 | front | x_from_labium = labium_to_foot * 2^(-offset_st/12); tune upward by enlarging |
| ALG-AS3-J2 | Fipple Alghosazi | 3 | 7 | 349.228 | 20.345 | 10.138 | 0.1875 | 0.2500 | front | x_from_labium = labium_to_foot * 2^(-offset_st/12); tune upward by enlarging |
| ALG-AS3-J2 | Fipple Alghosazi | 4 | 9 | 391.995 | 18.126 | 12.358 | 0.2188 | 0.3125 | front | x_from_labium = labium_to_foot * 2^(-offset_st/12); tune upward by enlarging |
| ALG-AS3-J2 | Fipple Alghosazi | 5 | 11 | 440.0 | 16.148 | 14.335 | 0.2188 | 0.3125 | front | x_from_labium = labium_to_foot * 2^(-offset_st/12); tune upward by enlarging |
| ALG-AS3-J2 | Fipple Alghosazi | 6 | 12 | 466.164 | 15.242 | 15.242 | 0.2188 | 0.3125 | back thumb | x_from_labium = labium_to_foot * 2^(-offset_st/12); tune upward by enlarging |
| ALG-AS3-SOLID | Fipple Alghosazi | 1 | 2 | 261.626 | 28.21 | 3.455 | 0.1875 | 0.2500 | front | x_from_labium = labium_to_foot * 2^(-offset_st/12); tune upward by enlarging |
| ALG-AS3-SOLID | Fipple Alghosazi | 2 | 4 | 293.665 | 25.132 | 6.532 | 0.1875 | 0.2500 | front | x_from_labium = labium_to_foot * 2^(-offset_st/12); tune upward by enlarging |
| ALG-AS3-SOLID | Fipple Alghosazi | 3 | 7 | 349.228 | 21.134 | 10.531 | 0.1875 | 0.2500 | front | x_from_labium = labium_to_foot * 2^(-offset_st/12); tune upward by enlarging |
| ALG-AS3-SOLID | Fipple Alghosazi | 4 | 9 | 391.995 | 18.828 | 12.837 | 0.2188 | 0.3125 | front | x_from_labium = labium_to_foot * 2^(-offset_st/12); tune upward by enlarging |
| ALG-AS3-SOLID | Fipple Alghosazi | 5 | 11 | 440.0 | 16.774 | 14.891 | 0.2188 | 0.3125 | front | x_from_labium = labium_to_foot * 2^(-offset_st/12); tune upward by enlarging |
| ALG-AS3-SOLID | Fipple Alghosazi | 6 | 12 | 466.164 | 15.832 | 15.832 | 0.2188 | 0.3125 | back thumb | x_from_labium = labium_to_foot * 2^(-offset_st/12); tune upward by enlarging |
| ALG-A3-J3 | Fipple Alghosazi | 1 | 2 | 246.942 | 24.045 | 2.945 | 0.1875 | 0.2500 | front | x_from_labium = labium_to_foot * 2^(-offset_st/12); tune upward by enlarging |
| ALG-A3-J3 | Fipple Alghosazi | 2 | 4 | 277.183 | 21.422 | 5.568 | 0.1875 | 0.2500 | front | x_from_labium = labium_to_foot * 2^(-offset_st/12); tune upward by enlarging |
| ALG-A3-J3 | Fipple Alghosazi | 3 | 7 | 329.628 | 18.014 | 8.976 | 0.1875 | 0.2500 | front | x_from_labium = labium_to_foot * 2^(-offset_st/12); tune upward by enlarging |
| ALG-A3-J3 | Fipple Alghosazi | 4 | 9 | 369.994 | 16.048 | 10.942 | 0.2188 | 0.3125 | front | x_from_labium = labium_to_foot * 2^(-offset_st/12); tune upward by enlarging |
| ALG-A3-J3 | Fipple Alghosazi | 5 | 11 | 415.305 | 14.298 | 12.693 | 0.2188 | 0.3125 | front | x_from_labium = labium_to_foot * 2^(-offset_st/12); tune upward by enlarging |
| ALG-A3-J3 | Fipple Alghosazi | 6 | 12 | 440.0 | 13.495 | 13.495 | 0.2188 | 0.3125 | back thumb | x_from_labium = labium_to_foot * 2^(-offset_st/12); tune upward by enlarging |
| ALG-B3-SOLID | Fipple Alghosazi | 1 | 2 | 277.183 | 23.082 | 2.827 | 0.1875 | 0.2500 | front | x_from_labium = labium_to_foot * 2^(-offset_st/12); tune upward by enlarging |
| ALG-B3-SOLID | Fipple Alghosazi | 2 | 4 | 311.127 | 20.564 | 5.345 | 0.1875 | 0.2500 | front | x_from_labium = labium_to_foot * 2^(-offset_st/12); tune upward by enlarging |
| ALG-B3-SOLID | Fipple Alghosazi | 3 | 7 | 369.994 | 17.292 | 8.617 | 0.1875 | 0.2500 | front | x_from_labium = labium_to_foot * 2^(-offset_st/12); tune upward by enlarging |
| ALG-B3-SOLID | Fipple Alghosazi | 4 | 9 | 415.305 | 15.406 | 10.503 | 0.2188 | 0.3125 | front | x_from_labium = labium_to_foot * 2^(-offset_st/12); tune upward by enlarging |
| ALG-B3-SOLID | Fipple Alghosazi | 5 | 11 | 466.164 | 13.725 | 12.184 | 0.2188 | 0.3125 | front | x_from_labium = labium_to_foot * 2^(-offset_st/12); tune upward by enlarging |
| ALG-B3-SOLID | Fipple Alghosazi | 6 | 12 | 493.883 | 12.955 | 12.955 | 0.2188 | 0.3125 | back thumb | x_from_labium = labium_to_foot * 2^(-offset_st/12); tune upward by enlarging |

<div class="page-break"></div>

## kaval-hole-schedule.csv

Project artifact.

| member_id | instrument | hole_no_from_foot | offset_st | target_hz | x_from_labium_in | x_from_foot_in | starter_drill_in | target_final_dia_in | orientation | formula |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| KAV-GS3-5H | Fipple Kaval | 1 | 2 | 233.082 | 26.284 | 3.219 | 0.1875 | 0.2500 | front | x_from_labium = labium_to_foot * 2^(-offset_st/12); tune upward by enlarging |
| KAV-GS3-5H | Fipple Kaval | 2 | 3 | 246.942 | 24.808 | 4.694 | 0.1875 | 0.2500 | front | x_from_labium = labium_to_foot * 2^(-offset_st/12); tune upward by enlarging |
| KAV-GS3-5H | Fipple Kaval | 3 | 6 | 293.665 | 20.861 | 8.641 | 0.2188 | 0.3000 | front | x_from_labium = labium_to_foot * 2^(-offset_st/12); tune upward by enlarging |
| KAV-GS3-5H | Fipple Kaval | 4 | 7 | 311.127 | 19.69 | 9.812 | 0.2188 | 0.3000 | front | x_from_labium = labium_to_foot * 2^(-offset_st/12); tune upward by enlarging |
| KAV-GS3-5H | Fipple Kaval | 5 | 8 | 329.628 | 18.585 | 10.917 | 0.2188 | 0.3000 | front | x_from_labium = labium_to_foot * 2^(-offset_st/12); tune upward by enlarging |
| KAV-A3-5H | Fipple Kaval | 1 | 2 | 246.942 | 24.53 | 3.004 | 0.1875 | 0.2500 | front | x_from_labium = labium_to_foot * 2^(-offset_st/12); tune upward by enlarging |
| KAV-A3-5H | Fipple Kaval | 2 | 3 | 261.626 | 23.153 | 4.381 | 0.1875 | 0.2500 | front | x_from_labium = labium_to_foot * 2^(-offset_st/12); tune upward by enlarging |
| KAV-A3-5H | Fipple Kaval | 3 | 6 | 311.127 | 19.469 | 8.064 | 0.2188 | 0.3000 | front | x_from_labium = labium_to_foot * 2^(-offset_st/12); tune upward by enlarging |
| KAV-A3-5H | Fipple Kaval | 4 | 7 | 329.628 | 18.377 | 9.157 | 0.2188 | 0.3000 | front | x_from_labium = labium_to_foot * 2^(-offset_st/12); tune upward by enlarging |
| KAV-A3-5H | Fipple Kaval | 5 | 8 | 349.228 | 17.345 | 10.189 | 0.2188 | 0.3000 | front | x_from_labium = labium_to_foot * 2^(-offset_st/12); tune upward by enlarging |
| KAV-B3-5H | Fipple Kaval | 1 | 2 | 277.183 | 22.164 | 2.714 | 0.1875 | 0.2500 | front | x_from_labium = labium_to_foot * 2^(-offset_st/12); tune upward by enlarging |
| KAV-B3-5H | Fipple Kaval | 2 | 3 | 293.665 | 20.92 | 3.958 | 0.1875 | 0.2500 | front | x_from_labium = labium_to_foot * 2^(-offset_st/12); tune upward by enlarging |
| KAV-B3-5H | Fipple Kaval | 3 | 6 | 349.228 | 17.591 | 7.287 | 0.2188 | 0.3000 | front | x_from_labium = labium_to_foot * 2^(-offset_st/12); tune upward by enlarging |
| KAV-B3-5H | Fipple Kaval | 4 | 7 | 369.994 | 16.604 | 8.274 | 0.2188 | 0.3000 | front | x_from_labium = labium_to_foot * 2^(-offset_st/12); tune upward by enlarging |
| KAV-B3-5H | Fipple Kaval | 5 | 8 | 391.995 | 15.672 | 9.206 | 0.2188 | 0.3000 | front | x_from_labium = labium_to_foot * 2^(-offset_st/12); tune upward by enlarging |
| KAV-C4-5H | Fipple Kaval | 1 | 2 | 293.665 | 20.455 | 2.505 | 0.1875 | 0.2500 | front | x_from_labium = labium_to_foot * 2^(-offset_st/12); tune upward by enlarging |
| KAV-C4-5H | Fipple Kaval | 2 | 3 | 311.127 | 19.307 | 3.653 | 0.1875 | 0.2500 | front | x_from_labium = labium_to_foot * 2^(-offset_st/12); tune upward by enlarging |
| KAV-C4-5H | Fipple Kaval | 3 | 6 | 369.994 | 16.235 | 6.725 | 0.2188 | 0.3000 | front | x_from_labium = labium_to_foot * 2^(-offset_st/12); tune upward by enlarging |
| KAV-C4-5H | Fipple Kaval | 4 | 7 | 391.995 | 15.324 | 7.636 | 0.2188 | 0.3000 | front | x_from_labium = labium_to_foot * 2^(-offset_st/12); tune upward by enlarging |
| KAV-C4-5H | Fipple Kaval | 5 | 8 | 415.305 | 14.464 | 8.496 | 0.2188 | 0.3000 | front | x_from_labium = labium_to_foot * 2^(-offset_st/12); tune upward by enlarging |
| KAV-A3-7H | Fipple Kaval | 1 | 2 | 246.942 | 30.097 | 3.686 | 0.1875 | 0.2500 | front | x_from_labium = labium_to_foot * 2^(-offset_st/12); tune upward by enlarging |
| KAV-A3-7H | Fipple Kaval | 2 | 3 | 261.626 | 28.408 | 5.375 | 0.1875 | 0.2500 | front | x_from_labium = labium_to_foot * 2^(-offset_st/12); tune upward by enlarging |
| KAV-A3-7H | Fipple Kaval | 3 | 4 | 277.183 | 26.814 | 6.969 | 0.2188 | 0.3000 | front | x_from_labium = labium_to_foot * 2^(-offset_st/12); tune upward by enlarging |
| KAV-A3-7H | Fipple Kaval | 4 | 6 | 311.127 | 23.888 | 9.895 | 0.2188 | 0.3000 | front | x_from_labium = labium_to_foot * 2^(-offset_st/12); tune upward by enlarging |
| KAV-A3-7H | Fipple Kaval | 5 | 7 | 329.628 | 22.547 | 11.236 | 0.2188 | 0.3000 | front | x_from_labium = labium_to_foot * 2^(-offset_st/12); tune upward by enlarging |
| KAV-A3-7H | Fipple Kaval | 6 | 8 | 349.228 | 21.282 | 12.501 | 0.2188 | 0.3000 | front | x_from_labium = labium_to_foot * 2^(-offset_st/12); tune upward by enlarging |
| KAV-A3-7H | Fipple Kaval | 7 | 9 | 369.994 | 20.088 | 13.696 | 0.2188 | 0.3000 | front | x_from_labium = labium_to_foot * 2^(-offset_st/12); tune upward by enlarging |
| KAV-AS3-7H | Fipple Kaval | 1 | 2 | 261.626 | 28.344 | 3.471 | 0.1875 | 0.2500 | front | x_from_labium = labium_to_foot * 2^(-offset_st/12); tune upward by enlarging |
| KAV-AS3-7H | Fipple Kaval | 2 | 3 | 277.183 | 26.753 | 5.062 | 0.1875 | 0.2500 | front | x_from_labium = labium_to_foot * 2^(-offset_st/12); tune upward by enlarging |
| KAV-AS3-7H | Fipple Kaval | 3 | 4 | 293.665 | 25.251 | 6.563 | 0.2188 | 0.3000 | front | x_from_labium = labium_to_foot * 2^(-offset_st/12); tune upward by enlarging |
| KAV-AS3-7H | Fipple Kaval | 4 | 6 | 329.628 | 22.496 | 9.318 | 0.2188 | 0.3000 | front | x_from_labium = labium_to_foot * 2^(-offset_st/12); tune upward by enlarging |
| KAV-AS3-7H | Fipple Kaval | 5 | 7 | 349.228 | 21.234 | 10.581 | 0.2188 | 0.3000 | front | x_from_labium = labium_to_foot * 2^(-offset_st/12); tune upward by enlarging |
| KAV-AS3-7H | Fipple Kaval | 6 | 8 | 369.994 | 20.042 | 11.773 | 0.2188 | 0.3000 | front | x_from_labium = labium_to_foot * 2^(-offset_st/12); tune upward by enlarging |
| KAV-AS3-7H | Fipple Kaval | 7 | 9 | 391.995 | 18.917 | 12.898 | 0.2188 | 0.3000 | front | x_from_labium = labium_to_foot * 2^(-offset_st/12); tune upward by enlarging |
| KAV-B3-7H | Fipple Kaval | 1 | 2 | 277.183 | 22.865 | 2.8 | 0.1875 | 0.2500 | front | x_from_labium = labium_to_foot * 2^(-offset_st/12); tune upward by enlarging |
| KAV-B3-7H | Fipple Kaval | 2 | 3 | 293.665 | 21.582 | 4.083 | 0.1875 | 0.2500 | front | x_from_labium = labium_to_foot * 2^(-offset_st/12); tune upward by enlarging |
| KAV-B3-7H | Fipple Kaval | 3 | 4 | 311.127 | 20.371 | 5.295 | 0.2188 | 0.3000 | front | x_from_labium = labium_to_foot * 2^(-offset_st/12); tune upward by enlarging |
| KAV-B3-7H | Fipple Kaval | 4 | 6 | 349.228 | 18.148 | 7.517 | 0.2188 | 0.3000 | front | x_from_labium = labium_to_foot * 2^(-offset_st/12); tune upward by enlarging |
| KAV-B3-7H | Fipple Kaval | 5 | 7 | 369.994 | 17.13 | 8.536 | 0.2188 | 0.3000 | front | x_from_labium = labium_to_foot * 2^(-offset_st/12); tune upward by enlarging |
| KAV-B3-7H | Fipple Kaval | 6 | 8 | 391.995 | 16.168 | 9.497 | 0.2188 | 0.3000 | front | x_from_labium = labium_to_foot * 2^(-offset_st/12); tune upward by enlarging |
| KAV-B3-7H | Fipple Kaval | 7 | 9 | 415.305 | 15.261 | 10.405 | 0.2188 | 0.3000 | front | x_from_labium = labium_to_foot * 2^(-offset_st/12); tune upward by enlarging |

<div class="page-break"></div>

## photo-shotlist.md

Project artifact.

# Photo Shotlist

Follow the repo-level photo pipeline style: real process photos replace concept placeholders as soon as shop work begins.

## P0 Fipple Head

- End mouth inlet before plug install.
- Removable flue plugs with shim labels.
- Side true sound window and splitting edge closeup.
- Tuner screenshot or phone photo during first tone.

## P1 Bodies

- Blank selection with grain orientation marked.
- Split blank or deep-bore setup.
- Routed/bored bore before glue-up.
- Hole template wrapped around body.
- First drilled undersized hole.
- Final tuned flute full length.

## Jointed/Double Options

- Tenon/socket before cork.
- Cork/ferrule fit closeup.
- Double-body temporary clamp test.
- Independent windways at the mouth end.

## Finished Portfolio

- Kaval and Alghosazi side by side.
- Player hand reach shot.
- Fipple head detail.
- Validation/tuning bench shot.

<div class="page-break"></div>

## risks.md

Project artifact.

# Risks

## Acoustic

- **Fipple/sound-window correction is unknown.** Test: build `P0-FIPPLE-HEAD`, record root prediction vs measured, and update `estimated_sound_window_correction_in`.
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

<div class="page-break"></div>

## sources.md

Project artifact.

# Sources And Provenance

## External Pages Checked

- Fujara Flutes Kaval page: https://www.fujaraflutes.com/moldavian-kaval-flutes
- Fujara Flutes Alghosazi page: https://www.fujaraflutes.com/alghosazi
- Flutopedia Native American flute tunings / Anasazi note: https://www.flutopedia.com/naf_tunings.htm

## Local Sources Used

- `../fujara/README.md`
- `../fujara/design-table/fujara_equations.md`
- `../fujara/CAD/fujara-body/G2Fujara_Assembly.SLDASM_dimensions.csv`
- `../drone-flutes/design.md`
- `../flutes/skills/parametric-design-table.md`
- `../pistalka/docs/build-packet/design.md`

## Source-Backed Facts Used

- The kaval reference page presents fipple-style kavals and gives 5-hole and 7-hole pitch sets.
- The same page documents examples in G#, A, B, C and a double Kaval/Kavalghoza drone concept.
- The Alghosazi reference page frames the instrument as an easier fipple adaptation of an Anasazi-style flute and notes the rear thumb-hole idea.
- Tony's fujara CAD records a fipple/flue plug system with narrow windway, removable plug logic, and splitting-edge KPI values.

## Assumptions Needing Prototype Data

- Exact fipple sound-window end correction.
- Final hole diameters and undercutting.
- Alghosazi mode preference after listening/playing.
- Joint effect on tuning and response.
