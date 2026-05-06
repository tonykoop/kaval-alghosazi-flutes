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
