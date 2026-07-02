# Kaval + Alghosazi Fipple Flutes

This repository is a prototype design packet for two related long fipple flutes. It is not build-ready for a final instrument until the P0 fipple-head and sound-window correction measurements below are recorded:

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
| `hole-schedule.csv` | First-pass hole positions computed from labium-to-foot length (pre-P0; rerun after measured sound-window correction). |
| `bom.csv`, `sourcing.csv`, `cut-list.csv` | Procurement and stock prep. |
| `assembly-manual.md` | Shop sequence from fipple tile through tuning. |
| `docs/p0-fipple-head-measurement.md` | P0 fipple-head build and measurement procedure. |
| `sound-window-correction-log.csv` | Back-solve log for the measured fipple/sound-window correction. |
| `validation-loop.csv` | Prototype validation-loop scaffold with measurement-required gates. |
| `drawings/` | SVG manufacturing drawings and head/joint details. |
| `cad/` | OpenSCAD and SolidWorks starter handoff files. |
| `cnc/` | v4.2 operation plan and setup sheet. |
| `validation.csv` | Tuning and empirical correction log. |
| `capstone-deck.pptx`, `print-packet.pdf`, `site/index.html` | Presentation, shop print, and build-log deliverables. |
| `wolfram/kaval-alghosazi-flutes-wolfram-model.wl` | Existing acoustic model source; pending P0 measured correction. |
| `evolution/` | Evolution-pipeline Stage 0 intake: master manifest, design-intent, revision register (Gate A not yet run). |

## Status

**Status:** L1 concept packet

This is a first-pass engineering packet. Dimensions are parametric and source-backed where possible, but the fipple/sound-window correction is marked as a measured-prototype variable, not a borrowed NAF K2 correction.

Current readiness is `L1_packet`: fabrication drawings and schedules are starter artifacts, while the fipple/head correction, final hole locations, and production readiness remain measurement-required.

V5 migration status: `L1_packet`. Existing SVGs, OpenSCAD, CNC plans, renders, and print/site artifacts are registered in `visual-output-register.csv`; CAD/DXF authority, MCP provenance, sound-window correction, and measured tuning remain pending measurement.

## Attribution

The kaval references come from Moldavian/Romanian shepherd-flute practice; the Alghosazi references point toward Anasazi/Basketmaker flute replicas and contemporary adaptations. This packet is a modern shop design by Tony Koop, built with respect for those lineages and explicit source notes in `sources.md`.
