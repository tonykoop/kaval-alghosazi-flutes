(* instrument-maker-v4.2 Wolfram packet source *)
ClearAll["Global`*"];

packetDir = "/mnt/c/Users/Tony/Documents/GitHub/kaval-alghosazi-flutes";
metadata = <|
  "PacketName" -> "Kaval + Alghosazi Fipple Flutes",
  "PacketPath" -> ".",
  "GeneratedOn" -> "2026-05-05",
  "Model" -> "OpenPipe",
  "HasFamilySpec" -> True,
  "HasValidation" -> True,
  "HasCncPlan" -> True
|>;

familySpecPath = FileNameJoin[{packetDir, "family-spec.csv"}];
validationPath = FileNameJoin[{packetDir, "validation.csv"}];
cncPlanPath = FileNameJoin[{packetDir, "cnc", "cnc-plan.json"}];

familySpec = If[FileExistsQ[familySpecPath],
  Import[familySpecPath, "Dataset"],
  Dataset[ImportString["[{\"member_id\": \"KAV-GS3-5H\", \"instrument\": \"Fipple Kaval\", \"subtype\": \"5-hole Moldavian/Romanian\", \"target_note\": \"G#3\", \"target_hz\": \"207.652\", \"midi\": \"56\", \"scale_label\": \"Kaval gypsy mode: 0,2,3,6,7,8 semitones\", \"hole_count\": \"5\", \"hole_offsets_st\": \"2 3 6 7 8\", \"bore_id_in\": \"0.8750\", \"body_od_in\": \"1.3750\", \"wall_in\": \"0.2500\", \"total_length_cm\": \"79.0\", \"total_length_in\": \"31.102\", \"top_to_window_in\": \"1.600\", \"labium_to_foot_in\": \"29.502\", \"open_pipe_leff_in\": \"32.631\", \"estimated_sound_window_correction_in\": \"3.129\", \"tuning_delta_interpretation\": \"positive: needs fipple/window end correction or added acoustic length\", \"chamber_to_bore\": \"33.7\", \"wood_species\": \"Locust or elder\", \"construction\": \"solid or split blank; optional two-piece joint\", \"source_basis\": \"Fujara Flutes observed G# kaval length 79 cm\", \"done_bar_ref\": \"fujara + flutes + pistalka\", \"notes\": \"Longest 5-hole starter; use as low-voice reference.\"}, {\"member_id\": \"KAV-A3-5H\", \"instrument\": \"Fipple Kaval\", \"subtype\": \"5-hole Moldavian/Romanian\", \"target_note\": \"A3\", \"target_hz\": \"220.000\", \"midi\": \"57\", \"scale_label\": \"Kaval gypsy mode: 0,2,3,6,7,8 semitones\", \"hole_count\": \"5\", \"hole_offsets_st\": \"2 3 6 7 8\", \"bore_id_in\": \"0.8750\", \"body_od_in\": \"1.3750\", \"wall_in\": \"0.2500\", \"total_length_cm\": \"74.0\", \"total_length_in\": \"29.134\", \"top_to_window_in\": \"1.600\", \"labium_to_foot_in\": \"27.534\", \"open_pipe_leff_in\": \"30.800\", \"estimated_sound_window_correction_in\": \"3.266\", \"tuning_delta_interpretation\": \"positive: needs fipple/window end correction or added acoustic length\", \"chamber_to_bore\": \"31.5\", \"wood_species\": \"Elder\", \"construction\": \"two-piece optional hand-cut joint\", \"source_basis\": \"Fujara Flutes observed A kaval length 74 cm\", \"done_bar_ref\": \"fujara + flutes + pistalka\", \"notes\": \"Recommended first kaval because length, bore, and hand span are forgiving.\"}, {\"member_id\": \"KAV-B3-5H\", \"instrument\": \"Fipple Kaval\", \"subtype\": \"5-hole Moldavian/Romanian\", \"target_note\": \"B3\", \"target_hz\": \"246.942\", \"midi\": \"59\", \"scale_label\": \"Kaval gypsy mode: 0,2,3,6,7,8 semitones\", \"hole_count\": \"5\", \"hole_offsets_st\": \"2 3 6 7 8\", \"bore_id_in\": \"0.8125\", \"body_od_in\": \"1.3125\", \"wall_in\": \"0.2500\", \"total_length_cm\": \"67.0\", \"total_length_in\": \"26.378\", \"top_to_window_in\": \"1.500\", \"labium_to_foot_in\": \"24.878\", \"open_pipe_leff_in\": \"27.440\", \"estimated_sound_window_correction_in\": \"2.562\", \"tuning_delta_interpretation\": \"positive: needs fipple/window end correction or added acoustic length\", \"chamber_to_bore\": \"30.6\", \"wood_species\": \"Elder\", \"construction\": \"solid split blank\", \"source_basis\": \"Fujara Flutes observed B kaval length 67 cm\", \"done_bar_ref\": \"fujara + flutes + pistalka\", \"notes\": \"Compact 5-hole version; tighter fipple tolerances.\"}, {\"member_id\": \"KAV-C4-5H\", \"instrument\": \"Fipple Kaval\", \"subtype\": \"5-hole Moldavian/Romanian\", \"target_note\": \"C4\", \"target_hz\": \"261.626\", \"midi\": \"60\", \"scale_label\": \"Kaval gypsy mode: 0,2,3,6,7,8 semitones\", \"hole_count\": \"5\", \"hole_offsets_st\": \"2 3 6 7 8\", \"bore_id_in\": \"0.7500\", \"body_od_in\": \"1.2500\", \"wall_in\": \"0.2500\", \"total_length_cm\": \"62.0\", \"total_length_in\": \"24.409\", \"top_to_window_in\": \"1.450\", \"labium_to_foot_in\": \"22.959\", \"open_pipe_leff_in\": \"25.900\", \"estimated_sound_window_correction_in\": \"2.940\", \"tuning_delta_interpretation\": \"positive: needs fipple/window end correction or added acoustic length\", \"chamber_to_bore\": \"30.6\", \"wood_species\": \"Elder, maple, or cherry\", \"construction\": \"solid split blank\", \"source_basis\": \"Fujara Flutes observed C kaval length 62 cm\", \"done_bar_ref\": \"fujara + flutes + pistalka\", \"notes\": \"Smallest 5-hole kaval; good for fipple/head trials.\"}, {\"member_id\": \"KAV-A3-7H\", \"instrument\": \"Fipple Kaval\", \"subtype\": \"7-hole expanded Moldavian\", \"target_note\": \"A3\", \"target_hz\": \"220.000\", \"midi\": \"57\", \"scale_label\": \"Expanded kaval: 0,2,3,4,6,7,8,9 semitones\", \"hole_count\": \"7\", \"hole_offsets_st\": \"2 3 4 6 7 8 9\", \"bore_id_in\": \"0.8750\", \"body_od_in\": \"1.4000\", \"wall_in\": \"0.2625\", \"total_length_cm\": \"90.0\", \"total_length_in\": \"35.433\", \"top_to_window_in\": \"1.650\", \"labium_to_foot_in\": \"33.783\", \"open_pipe_leff_in\": \"30.800\", \"estimated_sound_window_correction_in\": \"-2.983\", \"tuning_delta_interpretation\": \"negative: observed source length is overlong for this nominal root; trim foot or reassess key naming\", \"chamber_to_bore\": \"38.6\", \"wood_species\": \"Elder\", \"construction\": \"solid split blank\", \"source_basis\": \"Fujara Flutes observed 7-hole A kaval length 90 cm\", \"done_bar_ref\": \"fujara + flutes + pistalka\", \"notes\": \"Expanded note set; lower holes may be covered with finger bases.\"}, {\"member_id\": \"KAV-AS3-7H\", \"instrument\": \"Fipple Kaval\", \"subtype\": \"7-hole expanded Moldavian\", \"target_note\": \"A#3\", \"target_hz\": \"233.082\", \"midi\": \"58\", \"scale_label\": \"Expanded kaval: 0,2,3,4,6,7,8,9 semitones\", \"hole_count\": \"7\", \"hole_offsets_st\": \"2 3 4 6 7 8 9\", \"bore_id_in\": \"0.8750\", \"body_od_in\": \"1.4000\", \"wall_in\": \"0.2625\", \"total_length_cm\": \"85.0\", \"total_length_in\": \"33.465\", \"top_to_window_in\": \"1.650\", \"labium_to_foot_in\": \"31.815\", \"open_pipe_leff_in\": \"29.071\", \"estimated_sound_window_correction_in\": \"-2.743\", \"tuning_delta_interpretation\": \"negative: observed source length is overlong for this nominal root; trim foot or reassess key naming\", \"chamber_to_bore\": \"36.4\", \"wood_species\": \"Dogwood or elder\", \"construction\": \"two-piece optional hand-cut joint\", \"source_basis\": \"Fujara Flutes observed 7-hole A# kaval length 85 cm\", \"done_bar_ref\": \"fujara + flutes + pistalka\", \"notes\": \"Good two-piece test because the published example is collapsible.\"}, {\"member_id\": \"KAV-B3-7H\", \"instrument\": \"Fipple Kaval\", \"subtype\": \"7-hole expanded Moldavian\", \"target_note\": \"B3\", \"target_hz\": \"246.942\", \"midi\": \"59\", \"scale_label\": \"Expanded kaval: 0,2,3,4,6,7,8,9 semitones\", \"hole_count\": \"7\", \"hole_offsets_st\": \"2 3 4 6 7 8 9\", \"bore_id_in\": \"0.8125\", \"body_od_in\": \"1.3125\", \"wall_in\": \"0.2500\", \"total_length_cm\": \"69.0\", \"total_length_in\": \"27.165\", \"top_to_window_in\": \"1.500\", \"labium_to_foot_in\": \"25.665\", \"open_pipe_leff_in\": \"27.440\", \"estimated_sound_window_correction_in\": \"1.774\", \"tuning_delta_interpretation\": \"positive: needs fipple/window end correction or added acoustic length\", \"chamber_to_bore\": \"31.6\", \"wood_species\": \"Elder\", \"construction\": \"solid split blank\", \"source_basis\": \"Fujara Flutes observed 7-hole B kaval length 69 cm\", \"done_bar_ref\": \"fujara + flutes + pistalka\", \"notes\": \"Compact 7-hole version; validate hand position before final hole diameters.\"}, {\"member_id\": \"ALG-AS3-J2\", \"instrument\": \"Fipple Alghosazi\", \"subtype\": \"Anasazi-derived with thumb hole\", \"target_note\": \"A#3\", \"target_hz\": \"233.082\", \"midi\": \"58\", \"scale_label\": \"Anasazi-derived: 0,2,4,7,9,11,12 semitones\", \"hole_count\": \"6\", \"hole_offsets_st\": \"2 4 7 9 11 12\", \"bore_id_in\": \"0.8750\", \"body_od_in\": \"1.3750\", \"wall_in\": \"0.2500\", \"total_length_cm\": \"82.0\", \"total_length_in\": \"32.283\", \"top_to_window_in\": \"1.800\", \"labium_to_foot_in\": \"30.483\", \"open_pipe_leff_in\": \"29.071\", \"estimated_sound_window_correction_in\": \"-1.412\", \"tuning_delta_interpretation\": \"negative: observed source length is overlong for this nominal root; trim foot or reassess key naming\", \"chamber_to_bore\": \"34.8\", \"wood_species\": \"Ash\", \"construction\": \"two-piece hand-cut joint\", \"source_basis\": \"Fujara Flutes observed A# Alghosazi length 82 cm\", \"done_bar_ref\": \"fujara + flutes + pistalka\", \"notes\": \"Recommended first Alghosazi; published example uses a collapsible joint.\"}]", "JSON"]]
];

validationData = If[FileExistsQ[validationPath],
  Import[validationPath, "Dataset"],
  Dataset[ImportString["[{\"member_id\": \"KAV-GS3-5H\", \"test_id\": \"VAL-ROOT\", \"target\": \"root G#3\", \"target_value\": \"207.652 Hz\", \"measured_value\": \"\", \"tolerance\": \"+/-25 cents P1, +/-10 cents P2\", \"environment\": \"TBD temp/RH\", \"pass_fail\": \"\", \"action\": \"Trim foot shorter to raise pitch; rebuild/extend foot if sharp.\"}, {\"member_id\": \"KAV-GS3-5H\", \"test_id\": \"VAL-H1\", \"target\": \"hole 1 offset +2 st\", \"target_value\": \"233.082 Hz\", \"measured_value\": \"\", \"tolerance\": \"+/-25 cents P1, +/-10 cents P2\", \"environment\": \"TBD temp/RH\", \"pass_fail\": \"\", \"action\": \"Enlarge/undercut slowly to raise; wax or bushing recovery if sharp.\"}, {\"member_id\": \"KAV-GS3-5H\", \"test_id\": \"VAL-H2\", \"target\": \"hole 2 offset +3 st\", \"target_value\": \"246.942 Hz\", \"measured_value\": \"\", \"tolerance\": \"+/-25 cents P1, +/-10 cents P2\", \"environment\": \"TBD temp/RH\", \"pass_fail\": \"\", \"action\": \"Enlarge/undercut slowly to raise; wax or bushing recovery if sharp.\"}, {\"member_id\": \"KAV-GS3-5H\", \"test_id\": \"VAL-H3\", \"target\": \"hole 3 offset +6 st\", \"target_value\": \"293.665 Hz\", \"measured_value\": \"\", \"tolerance\": \"+/-25 cents P1, +/-10 cents P2\", \"environment\": \"TBD temp/RH\", \"pass_fail\": \"\", \"action\": \"Enlarge/undercut slowly to raise; wax or bushing recovery if sharp.\"}, {\"member_id\": \"KAV-GS3-5H\", \"test_id\": \"VAL-H4\", \"target\": \"hole 4 offset +7 st\", \"target_value\": \"311.127 Hz\", \"measured_value\": \"\", \"tolerance\": \"+/-25 cents P1, +/-10 cents P2\", \"environment\": \"TBD temp/RH\", \"pass_fail\": \"\", \"action\": \"Enlarge/undercut slowly to raise; wax or bushing recovery if sharp.\"}, {\"member_id\": \"KAV-GS3-5H\", \"test_id\": \"VAL-H5\", \"target\": \"hole 5 offset +8 st\", \"target_value\": \"329.628 Hz\", \"measured_value\": \"\", \"tolerance\": \"+/-25 cents P1, +/-10 cents P2\", \"environment\": \"TBD temp/RH\", \"pass_fail\": \"\", \"action\": \"Enlarge/undercut slowly to raise; wax or bushing recovery if sharp.\"}, {\"member_id\": \"KAV-A3-5H\", \"test_id\": \"VAL-ROOT\", \"target\": \"root A3\", \"target_value\": \"220.000 Hz\", \"measured_value\": \"\", \"tolerance\": \"+/-25 cents P1, +/-10 cents P2\", \"environment\": \"TBD temp/RH\", \"pass_fail\": \"\", \"action\": \"Trim foot shorter to raise pitch; rebuild/extend foot if sharp.\"}, {\"member_id\": \"KAV-A3-5H\", \"test_id\": \"VAL-H1\", \"target\": \"hole 1 offset +2 st\", \"target_value\": \"246.942 Hz\", \"measured_value\": \"\", \"tolerance\": \"+/-25 cents P1, +/-10 cents P2\", \"environment\": \"TBD temp/RH\", \"pass_fail\": \"\", \"action\": \"Enlarge/undercut slowly to raise; wax or bushing recovery if sharp.\"}]", "JSON"]]
];

frequencyFromMidi[midi_, a4_: 440] := a4*2^((midi - 69)/12);
centsError[measured_, target_] := 1200*Log[2, measured/target];
openPipeLengthIn[freq_, c_: 13552, radius_: 0] := c/(2*freq) - 2*0.6*radius;
stoppedPipeLengthIn[freq_, c_: 13552, radius_: 0] := c/(4*freq) - 0.6*radius;
helmholtzFrequency[area_, volume_, leff_, c_: 13552] :=
  (c/(2*Pi))*Sqrt[area/(volume*leff)];
cantileverFrequency[k_, thickness_, length_] := k*thickness/length^2;
stringFrequency[length_, tension_, linearDensity_] :=
  1/(2*length)*Sqrt[tension/linearDensity];

modelExplorer = Switch[metadata["Model"],
  "Helmholtz",
    Manipulate[
      helmholtzFrequency[portArea, chamberVolume, effectiveLength],
      {{portArea, 0.4, "port area (in^2)"}, 0.05, 4},
      {{chamberVolume, 40, "volume (in^3)"}, 5, 400},
      {{effectiveLength, 0.6, "effective length (in)"}, 0.05, 3}
    ],
  "OpenPipe",
    Manipulate[
      openPipeLengthIn[f, 13552, radius],
      {{f, 440, "target Hz"}, 80, 1200},
      {{radius, 0.375, "bore radius (in)"}, 0, 1.5}
    ],
  "StoppedPipe",
    Manipulate[
      stoppedPipeLengthIn[f, 13552, radius],
      {{f, 220, "target Hz"}, 40, 1000},
      {{radius, 0.375, "bore radius (in)"}, 0, 1.5}
    ],
  "CantileverBeam",
    Manipulate[
      cantileverFrequency[k, thickness, length],
      {{k, 24000, "K constant"}, 1000, 80000},
      {{thickness, 0.25, "thickness (in)"}, 0.05, 1},
      {{length, 4.5, "length (in)"}, 0.5, 24}
    ],
  _,
    Manipulate[
      frequencyFromMidi[midi],
      {{midi, 69, "MIDI note"}, 24, 96, 1}
    ]
];

audioPreview[f_: 440, seconds_: 1.5] :=
  AudioNormalize[
    AudioAdd[
      AudioGenerator[{"Sin", f}, seconds],
      .35 AudioGenerator[{"Sin", 2 f}, seconds],
      .18 AudioGenerator[{"Sin", 3 f}, seconds]
    ]
  ];

validationRows = Normal[validationData];
validationPlot = Quiet@Check[
  ListPlot[
    DeleteMissing[
      ToExpression /@ Lookup[validationRows, "Cents Error", Missing[]]
    ],
    PlotTheme -> "Scientific",
    Frame -> True,
    FrameLabel -> {{"Cents error", None}, {"Measurement row", metadata["PacketName"]}}
  ],
  "No numeric validation cents-error values yet."
];

packetNotebook[] := CreateDocument[
  {
    TextCell[metadata["PacketName"], "Title"],
    TextCell["instrument-maker v4.2 computational packet", "Subtitle"],
    TextCell["Metadata", "Section"],
    ExpressionCell[metadata, "Input"],
    TextCell["Family/design data", "Section"],
    ExpressionCell[familySpec, "Input"],
    TextCell["Model explorer", "Section"],
    ExpressionCell[modelExplorer, "Input"],
    TextCell["Audio preview", "Section"],
    ExpressionCell[audioPreview[440], "Input"],
    TextCell["Validation", "Section"],
    ExpressionCell[validationPlot, "Input"]
  },
  WindowTitle -> metadata["PacketName"]
];

packetNotebook[];
