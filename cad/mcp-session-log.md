# Kaval + Alghosazi Flutes MCP Session Log

Current status: no MCP, CAD, DXF, render, CAM, or measurement sessions were run
or verified in this V5 migration lane.

This log is a provenance stub for future V5 work. Existing packet content is
grounded in `README.md`, `design.md`, `family-spec.csv`, the hole schedules,
`docs/p0-fipple-head-measurement.md`, `docs/sound-window-correction-model.md`,
and the validation logs. This file does not claim that native CAD, measured
sound-window correction, measured tuning, or CAM-ready toolpaths already exist.

| timestamp_utc | tool | session_id | artifact | parent_artifact | role | authority | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| TBD | SolidWorks MCP | TBD | native CAD layout | `cad/SolidWorks-MasterLayout-Plan.md`; `cad/design-table-inputs.csv` | native CAD master | pending_measurement | Future session must preserve fipple-head and hole-position measurement gates. |
| TBD | OpenSCAD review | TBD | `cad/kaval_alghosazi_master.scad` | `family-spec.csv`; `hole-schedule.csv`; `cad/design-table-inputs.csv` | parametric CAD starter | pending_measurement | Existing OpenSCAD is not native CAD or CAM authority. |
| TBD | DXF export | TBD | hole and body templates under `drawings/` | reviewed CAD/table source | fabrication template | pending_measurement | Future DXF exports must wait for measured sound-window correction and reviewed hole schedules. |
| TBD | CNC/CAM review | TBD | shop toolpaths | `cnc/cnc-plan.json`; reviewed CAD/DXF | CAM setup | pending_measurement | Current CNC files are operation plans only, not G-code or release-ready toolpaths. |
| TBD | Wolfram/acoustic analysis | TBD | corrected acoustic model | `docs/sound-window-correction-model.md`; measured `sound-window-correction-log.csv` | acoustic validation | pending_measurement | Model estimates are not cut authority until P0 measurement exists. |
| TBD | Camera/render tool | TBD | `images/hero.png` or replacement render | reviewed CAD or concept brief | visual support | concept_only | Visuals must not control fipple geometry, bore, hole centers, or tuning. |
