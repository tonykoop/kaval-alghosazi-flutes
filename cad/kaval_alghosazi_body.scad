// Kaval + Alghosazi fipple flute starter, units = inches.
$fn = 96;

member = "KAV-A3-5H";
total_length = 29.134;
bore_id = 0.875;
body_od = 1.375;
top_to_window = 1.60;
windway_h = 0.038;
windway_w = 0.500;
window_l = 0.320;
window_w = 0.500;

module body_blank() {
  difference() {
    cylinder(h = total_length, d = body_od);
    translate([0,0,-0.02]) cylinder(h = total_length + 0.04, d = bore_id);
  }
}

module true_sound_window() {
  translate([-window_w/2, body_od/2 - 0.02, total_length - top_to_window])
    cube([window_w, 0.12, window_l], center=false);
}

module end_mouth_inlet() {
  translate([-windway_w/2, body_od/2 - 0.08, total_length - 0.32])
    cube([windway_w, 0.18, 0.28], center=false);
}

module flute_body_preview() {
  difference() {
    body_blank();
    true_sound_window();
    end_mouth_inlet();
  }
}

flute_body_preview();
