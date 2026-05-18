# P0 Fipple Head Measurement Procedure

## Purpose

Build `P0-FIPPLE-HEAD` before committing a full kaval or Alghosazi body. The goal is to measure whether the end mouth inlet, internal windway, true side sound window, and splitting edge produce a stable tone, then back-solve the sound-window correction that the current hole schedules only estimate.

## Geometry Authority

- Measured: none yet in this repository.
- Inferred: starter windway/window values from Tony's fujara-style CAD notes and source-observed flute lengths.
- Unknown: final sound-window correction, production plug setting, final hole centers, and final hole diameters.

Generated images and SVG previews are layout aids. Fabrication authority comes from the workbook, `family-spec.csv`, `hole-schedule.csv`, CAD/design-table files, and future measured P0 rows.

## Build Setup

1. Use a scrap block or short split-blank section with a 0.875 in bore or half-bore test channel.
2. Mark the bore centerline, labium/splitting-edge datum, and top-to-window datum.
3. Cut the end mouth inlet and fit a removable flue plug.
4. Prepare plug shim trials at 0.033, 0.038, and 0.045 in windway height.
5. Start with a 0.320 in long by 0.500 in wide side sound window.
6. Keep the splitting-edge offset in the 0.005-0.015 in starter range.

## Measurement Pass

For each trial, change only one variable and log:

- plug shim height;
- window length and width;
- splitting-edge offset;
- bore ID and labium-to-foot length;
- temperature and relative humidity;
- measured root pitch from a tuner;
- attack quality, choking, overblow behavior, and recorder/phone audio file name.

## Back-Solve

Use the first stable tone to compute:

```text
L_eff_measured = c / (2 * measured_root_hz)
foot_end_correction = 0.6 * bore_radius
sound_window_correction = L_eff_measured - labium_to_foot - foot_end_correction
```

Record the result in `sound-window-correction-log.csv`. If the correction shifts any hole center by more than 0.100 in, update the workbook and regenerate `hole-schedule.csv`, `kaval-hole-schedule.csv`, and `alghosazi-hole-schedule.csv`.

## Promotion Gate

Do not mark the packet L2, build-ready, validated, or production-ready until the P0 log contains measured geometry, measured pitch, environment, and the resulting correction. Until then the packet remains `L1_packet` with measurement-required gates.
