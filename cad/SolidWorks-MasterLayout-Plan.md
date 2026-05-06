# SolidWorks Master Layout Plan

## Master Sketch

- `g_body_L_total`
- `g_labium_to_foot`
- `g_top_to_window`
- `g_bore_ID`
- `g_body_OD`
- `g_wall`
- `g_windway_height`
- `g_windway_width`
- `g_window_length`
- `g_window_width`
- `g_splitting_edge_offset`
- `g_joint_tenon_length`
- `g_joint_cork_allowance`

## Configurations

Use `cad/design-table-inputs.csv` as the row-per-member design table. Each configuration should suppress or enable:

- 5-hole vs 7-hole pattern.
- Alghosazi back thumb hole.
- Solid vs jointed body.
- Double-drone assembly reference geometry.

## Critical CAD Checks

- Bore centerline stays continuous across joint.
- Hole center coordinates match `hole-schedule.csv`.
- Windway height is equation-driven, not a sketch accident.
- Splitting-edge offset is measured as a driven KPI.
