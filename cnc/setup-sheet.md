# CNC / Manufacturing Setup Sheet

- Packet: `.`
- Family: `woodwind`
- Generated: 2026-05-05
- Machine note: Maker Nexus/home shop; verify exact machine before CAM.

## Assumptions

- This is a pre-CAM operation graph, not verified G-code.
- Verify feeds, speeds, work envelope, hold-down, and tool clearance at the machine.
- Run air-cut or simulation before cutting instrument material.

## Operation Graph

### OP-010 - Review design package and mark datums

- Machine: Bench
- Tool: Calipers, square, marking knife, center punch
- Workholding: Flat bench, drawing packet
- Datum: Primary centerline / face A
- Inputs: design.md, drawing-brief.md, cut-list.csv
- Outputs: shop-marked blank, datum checklist
- Checks:
  - All stock dimensions exceed finished dimensions plus allowance
  - Units match drawings

### OP-110 - Prepare bore blank

- Machine: Table saw / jointer / planer
- Tool: Rip blade, jointer knives, planer
- Workholding: Push blocks, featherboard
- Datum: Face A and centerline
- Inputs: cut-list.csv
- Outputs: square bore blank
- Checks:
  - Blank straightness checked
  - Grain direction marked

### OP-210 - Create bore

- Machine: Lathe or CNC router
- Tool: Long brad-point bit, reamer, or ball/end mill for split blank
- Workholding: Tailstock vise/carrier or flip jig with datum pins
- Datum: Centerline A-B
- Inputs: drawing-brief.md, family-spec.csv
- Outputs: bored or routed body half
- Checks:
  - Bore wander checked on scrap
  - Bore diameter measured at both ends
- Notes: Use the deep-bore technique reference when the bore is long and straight.

### OP-310 - Cut tone features

- Machine: CNC router / drill press / laser template
- Tool: 1/8 in upcut spiral, brad-point bits, or printed drill guide
- Workholding: V-block, centerline fence, registration pins
- Datum: Embouchure end datum
- Inputs: scale table, drawing-brief.md
- Outputs: tone holes / windows
- Checks:
  - Hole spacing matches scale table
  - Undercut/tuning allowance left

### OP-900 - Validation and tuning pass

- Machine: Bench
- Tool: Chromatic tuner, calipers, scale, recording device
- Workholding: Padded bench
- Datum: Same acoustic datum used in design.md
- Inputs: validation.csv, finished part
- Outputs: updated validation.csv, process photo
- Checks:
  - Measured frequency recorded
  - Cents error computed
  - Tuning trim notes written

## Release Checks

- [ ] Every operation has a datum and workholding method.
- [ ] Every tool has a real machine available or an escalation note.
- [ ] All tuning-critical features include trim allowance.
- [ ] Validation.csv receives measured data after the first prototype.
