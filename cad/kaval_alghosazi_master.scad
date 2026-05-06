// =============================================================
// Kaval_Alghosazi — OpenSCAD Master-Shape Starter
// =============================================================
// Generated 2026-05-05 by generate_openscad_starter.py.
// Units: inches.
//
// This is a master-shape STARTER — captures bore profile + tone-hole
// positions to first order.  Voicing/embouchure/labium geometry must
// be refined by hand because it's tuning-sensitive.
//
// Governing model: Open pipe (or stopped pipe; see design.md)
//     f_n = n·v / (2·L_eff)            (open-open)
//     f_n = (2n-1)·v / (4·L_eff)       (open-stopped)
// with L_eff = L + end-correction(s) and Tony's NAF K2 bore correction
// applied where the bore diameter falls in the K2 lookup range.
// =============================================================

$fn = 96;

// --------- INPUT PARAMETERS (edit these) ---------------------

c_in_per_sec   = 13510;     // speed of sound (in/s @ ~68F)
bore_dia       = 0.005;       // bore inside diameter
total_length   = 5;      // overall length
wall_in        = 0.20;        // wall thickness

// Tone holes: [position_from_top_in, diameter_in, note_label]
holes = [
    // Edit for actual fingering chart from design.md
    [total_length*0.55, 0.30, "low"],
    [total_length*0.65, 0.31, "+1"],
    [total_length*0.74, 0.30, "+2"],
    [total_length*0.83, 0.32, "+3"],
    [total_length*0.92, 0.30, "+4"],
];

module open_pipe_body() {
    difference() {
        cylinder(h=total_length, d=bore_dia + 2*wall_in);
        translate([0, 0, -0.01])
            cylinder(h=total_length+0.02, d=bore_dia);
        for (h = holes) {
            translate([bore_dia/2 + wall_in, 0, h[0]])
                rotate([0, 90, 0])
                    cylinder(h=wall_in*3, d=h[1], center=true);
        }
    }
}

open_pipe_body();
echo(str("Bore: ", bore_dia, " in;  Length: ", total_length, " in;  Holes: ", len(holes)));
