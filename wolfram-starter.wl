(* Kaval + Alghosazi starter. Full v4.2 packet source is in wolfram/instrument-model.wl after generation. *)
ClearAll["Global`*"];
cInPerSec = 13552;
freqFromMidi[midi_, a4_: 440] := a4*2^((midi - 69)/12);
openPipeLeff[f_] := cInPerSec/(2*f);
holeFromLabium[labiumToFoot_, semitoneOffset_] := labiumToFoot*2^(-semitoneOffset/12);
centsError[measured_, target_] := 1200*Log[2, measured/target];
