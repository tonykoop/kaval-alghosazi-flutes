#!/usr/bin/env python3
"""Generate the Kaval + Alghosazi flute build packet.

The packet intentionally keeps two layers visible:
- source-observed proportions from Fujara Flutes and local Tony flute work;
- first-pass shop dimensions that must be tuned by measured prototypes.
"""

from __future__ import annotations

import csv
import json
import math
import os
import struct
import textwrap
import zlib
import zipfile
from dataclasses import dataclass
from pathlib import Path
from xml.sax.saxutils import escape


ROOT = Path(__file__).resolve().parents[1]
DATE = "2026-05-06"
C_IN_PER_SEC = 13552.0
A4 = 440.0


def midi_to_hz(midi: int) -> float:
    return A4 * 2 ** ((midi - 69) / 12)


@dataclass(frozen=True)
class Member:
    member_id: str
    instrument: str
    subtype: str
    key: str
    midi: int
    scale_label: str
    hole_offsets: tuple[int, ...]
    total_length_cm: float
    bore_id_in: float
    body_od_in: float
    top_to_window_in: float
    material: str
    construction: str
    source_basis: str
    notes: str

    @property
    def target_hz(self) -> float:
        return midi_to_hz(self.midi)

    @property
    def total_length_in(self) -> float:
        return self.total_length_cm / 2.54

    @property
    def labium_to_foot_in(self) -> float:
        return self.total_length_in - self.top_to_window_in

    @property
    def wall_in(self) -> float:
        return (self.body_od_in - self.bore_id_in) / 2

    @property
    def open_pipe_leff_in(self) -> float:
        return C_IN_PER_SEC / (2 * self.target_hz)

    @property
    def estimated_sound_window_correction_in(self) -> float:
        # This is deliberately not Tony's NAF K2 table. The head is a
        # fujara-style sound window/fipple system and must get its own
        # measured correction.
        return self.open_pipe_leff_in - self.labium_to_foot_in

    @property
    def chamber_to_bore(self) -> float:
        return self.labium_to_foot_in / self.bore_id_in


MEMBERS: list[Member] = [
    Member(
        "KAV-GS3-5H", "Fipple Kaval", "5-hole Moldavian/Romanian",
        "G#3", 56, "Kaval gypsy mode: 0,2,3,6,7,8 semitones",
        (2, 3, 6, 7, 8), 79.0, 0.875, 1.375, 1.60,
        "Locust or elder", "solid or split blank; optional two-piece joint",
        "Fujara Flutes observed G# kaval length 79 cm",
        "Longest 5-hole starter; use as low-voice reference.",
    ),
    Member(
        "KAV-A3-5H", "Fipple Kaval", "5-hole Moldavian/Romanian",
        "A3", 57, "Kaval gypsy mode: 0,2,3,6,7,8 semitones",
        (2, 3, 6, 7, 8), 74.0, 0.875, 1.375, 1.60,
        "Elder", "two-piece optional hand-cut joint",
        "Fujara Flutes observed A kaval length 74 cm",
        "Recommended first kaval because length, bore, and hand span are forgiving.",
    ),
    Member(
        "KAV-B3-5H", "Fipple Kaval", "5-hole Moldavian/Romanian",
        "B3", 59, "Kaval gypsy mode: 0,2,3,6,7,8 semitones",
        (2, 3, 6, 7, 8), 67.0, 0.8125, 1.3125, 1.50,
        "Elder", "solid split blank",
        "Fujara Flutes observed B kaval length 67 cm",
        "Compact 5-hole version; tighter fipple tolerances.",
    ),
    Member(
        "KAV-C4-5H", "Fipple Kaval", "5-hole Moldavian/Romanian",
        "C4", 60, "Kaval gypsy mode: 0,2,3,6,7,8 semitones",
        (2, 3, 6, 7, 8), 62.0, 0.750, 1.250, 1.45,
        "Elder, maple, or cherry", "solid split blank",
        "Fujara Flutes observed C kaval length 62 cm",
        "Smallest 5-hole kaval; good for fipple/head trials.",
    ),
    Member(
        "KAV-A3-7H", "Fipple Kaval", "7-hole expanded Moldavian",
        "A3", 57, "Expanded kaval: 0,2,3,4,6,7,8,9 semitones",
        (2, 3, 4, 6, 7, 8, 9), 90.0, 0.875, 1.400, 1.65,
        "Elder", "solid split blank",
        "Fujara Flutes observed 7-hole A kaval length 90 cm",
        "Expanded note set; lower holes may be covered with finger bases.",
    ),
    Member(
        "KAV-AS3-7H", "Fipple Kaval", "7-hole expanded Moldavian",
        "A#3", 58, "Expanded kaval: 0,2,3,4,6,7,8,9 semitones",
        (2, 3, 4, 6, 7, 8, 9), 85.0, 0.875, 1.400, 1.65,
        "Dogwood or elder", "two-piece optional hand-cut joint",
        "Fujara Flutes observed 7-hole A# kaval length 85 cm",
        "Good two-piece test because the published example is collapsible.",
    ),
    Member(
        "KAV-B3-7H", "Fipple Kaval", "7-hole expanded Moldavian",
        "B3", 59, "Expanded kaval: 0,2,3,4,6,7,8,9 semitones",
        (2, 3, 4, 6, 7, 8, 9), 69.0, 0.8125, 1.3125, 1.50,
        "Elder", "solid split blank",
        "Fujara Flutes observed 7-hole B kaval length 69 cm",
        "Compact 7-hole version; validate hand position before final hole diameters.",
    ),
    Member(
        "ALG-AS3-J2", "Fipple Alghosazi", "Anasazi-derived with thumb hole",
        "A#3", 58, "Anasazi-derived: 0,2,4,7,9,11,12 semitones",
        (2, 4, 7, 9, 11, 12), 82.0, 0.875, 1.375, 1.80,
        "Ash", "two-piece hand-cut joint",
        "Fujara Flutes observed A# Alghosazi length 82 cm",
        "Recommended first Alghosazi; published example uses a collapsible joint.",
    ),
    Member(
        "ALG-AS3-SOLID", "Fipple Alghosazi", "Anasazi-derived with thumb hole",
        "A#3", 58, "Anasazi-derived: 0,2,4,7,9,11,12 semitones",
        (2, 4, 7, 9, 11, 12), 85.0, 0.875, 1.375, 1.80,
        "Locust", "solid split blank",
        "Fujara Flutes observed solid A# Alghosazi length 85 cm",
        "Solid-body alternate for comparing joint vs no-joint response.",
    ),
    Member(
        "ALG-A3-J3", "Fipple Alghosazi", "Anasazi-derived with thumb hole",
        "A3", 57, "Anasazi-derived: 0,2,4,7,9,11,12 semitones",
        (2, 4, 7, 9, 11, 12), 73.0, 0.875, 1.375, 1.75,
        "Oak", "three-piece hand-cut joint",
        "Fujara Flutes observed A Alghosazi length 73 cm",
        "Use as the modular joint stress test.",
    ),
    Member(
        "ALG-B3-SOLID", "Fipple Alghosazi", "Anasazi-derived with thumb hole",
        "B3", 59, "Anasazi-derived: 0,2,4,7,9,11,12 semitones",
        (2, 4, 7, 9, 11, 12), 70.0, 0.8125, 1.3125, 1.65,
        "Elder or maple", "solid split blank",
        "Fujara Flutes observed B Alghosazi length 70 cm",
        "Compact Alghosazi; top thumb hole needs ergonomic mockup.",
    ),
]


def ensure_dirs() -> None:
    for path in [
        "cad", "cnc", "data", "drawings", "images", "site", "wolfram",
        "scripts", "docs", "sw-reference", "inlay-patterns"
    ]:
        (ROOT / path).mkdir(parents=True, exist_ok=True)


def write_text(rel: str, text: str) -> None:
    path = ROOT / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(textwrap.dedent(text).lstrip(), encoding="utf-8")


def write_csv(rel: str, rows: list[dict[str, object]], fieldnames: list[str]) -> None:
    path = ROOT / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow({key: row.get(key, "") for key in fieldnames})


def hole_schedule(member: Member) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for idx, offset in enumerate(member.hole_offsets, start=1):
        target_hz = member.target_hz * 2 ** (offset / 12)
        x_from_labium = member.labium_to_foot_in * 2 ** (-offset / 12)
        x_from_foot = member.labium_to_foot_in - x_from_labium
        if member.instrument == "Fipple Kaval":
            drill = 0.1875 if idx <= 2 else 0.21875
            final = 0.250 if idx <= 2 else 0.300
        else:
            drill = 0.1875 if idx <= 3 else 0.21875
            final = 0.250 if idx <= 3 else 0.3125
        rows.append({
            "member_id": member.member_id,
            "instrument": member.instrument,
            "hole_no_from_foot": idx,
            "offset_st": offset,
            "target_hz": round(target_hz, 3),
            "x_from_labium_in": round(x_from_labium, 3),
            "x_from_foot_in": round(x_from_foot, 3),
            "starter_drill_in": f"{drill:.4f}",
            "target_final_dia_in": f"{final:.4f}",
            "orientation": "back thumb" if member.instrument == "Fipple Alghosazi" and idx == len(member.hole_offsets) else "front",
            "formula": "starter pre-P0: x_from_labium = labium_to_foot * 2^(-offset_st/12); rerun after measured sound-window correction",
        })
    return rows


def member_rows() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for m in MEMBERS:
        rows.append({
            "member_id": m.member_id,
            "instrument": m.instrument,
            "subtype": m.subtype,
            "target_note": m.key,
            "target_hz": f"{m.target_hz:.3f}",
            "midi": m.midi,
            "scale_label": m.scale_label,
            "hole_count": len(m.hole_offsets),
            "hole_offsets_st": " ".join(str(o) for o in m.hole_offsets),
            "bore_id_in": f"{m.bore_id_in:.4f}",
            "body_od_in": f"{m.body_od_in:.4f}",
            "wall_in": f"{m.wall_in:.4f}",
            "total_length_cm": f"{m.total_length_cm:.1f}",
            "total_length_in": f"{m.total_length_in:.3f}",
            "top_to_window_in": f"{m.top_to_window_in:.3f}",
            "labium_to_foot_in": f"{m.labium_to_foot_in:.3f}",
            "open_pipe_leff_in": f"{m.open_pipe_leff_in:.3f}",
            "estimated_sound_window_correction_in": f"{m.estimated_sound_window_correction_in:.3f}",
            "tuning_delta_interpretation": (
                "positive: needs fipple/window end correction or added acoustic length"
                if m.estimated_sound_window_correction_in >= 0
                else "negative: observed source length is overlong for this nominal root; trim foot or reassess key naming"
            ),
            "chamber_to_bore": f"{m.chamber_to_bore:.1f}",
            "wood_species": m.material,
            "construction": m.construction,
            "source_basis": m.source_basis,
            "done_bar_ref": "fujara + flutes + pistalka",
            "notes": m.notes,
        })
    return rows


def write_data_files() -> None:
    write_csv(
        "family-spec.csv",
        member_rows(),
        [
            "member_id", "instrument", "subtype", "target_note", "target_hz",
            "midi", "scale_label", "hole_count", "hole_offsets_st",
            "bore_id_in", "body_od_in", "wall_in", "total_length_cm",
            "total_length_in", "top_to_window_in", "labium_to_foot_in",
            "open_pipe_leff_in", "estimated_sound_window_correction_in",
            "tuning_delta_interpretation", "chamber_to_bore", "wood_species", "construction",
            "source_basis", "done_bar_ref", "notes",
        ],
    )
    holes = [row for m in MEMBERS for row in hole_schedule(m)]
    write_csv(
        "hole-schedule.csv",
        holes,
        [
            "member_id", "instrument", "hole_no_from_foot", "offset_st",
            "target_hz", "x_from_labium_in", "x_from_foot_in",
            "starter_drill_in", "target_final_dia_in", "orientation", "formula",
        ],
    )
    write_csv(
        "kaval-hole-schedule.csv",
        [row for m in MEMBERS if m.instrument == "Fipple Kaval" for row in hole_schedule(m)],
        [
            "member_id", "instrument", "hole_no_from_foot", "offset_st",
            "target_hz", "x_from_labium_in", "x_from_foot_in",
            "starter_drill_in", "target_final_dia_in", "orientation", "formula",
        ],
    )
    write_csv(
        "alghosazi-hole-schedule.csv",
        [row for m in MEMBERS if m.instrument == "Fipple Alghosazi" for row in hole_schedule(m)],
        [
            "member_id", "instrument", "hole_no_from_foot", "offset_st",
            "target_hz", "x_from_labium_in", "x_from_foot_in",
            "starter_drill_in", "target_final_dia_in", "orientation", "formula",
        ],
    )
    write_csv(
        "data/source-observations.csv",
        [
            {
                "source": "Fujara Flutes Kaval page",
                "url": "https://www.fujaraflutes.com/moldavian-kaval-flutes",
                "observation": "Fipple kavals, 5-hole gypsy scale, 7-hole expanded version, optional collapsible joints, double kaval/kavalghoza drone option.",
                "used_for": "Member lengths, scale offsets, double-drone concept, two-piece option.",
            },
            {
                "source": "Fujara Flutes Alghosazi page",
                "url": "https://www.fujaraflutes.com/alghosazi",
                "observation": "Fipple adaptation of Anasazi-style flute, top hole moved to back thumb, examples in A#, A, B, and double drone form.",
                "used_for": "Alghosazi family, thumb-hole assumption, length precedents, two/three-piece options.",
            },
            {
                "source": "Local fujara CAD and equations",
                "url": "../fujara/design-table/fujara_equations.md",
                "observation": "Fujara-style flue plug, 0.033 to 0.040 in windway height, 0.005 to 0.015 in splitting-edge KPI, removable wax-sealed plug.",
                "used_for": "End-mouth to flue to true-sound-window head architecture.",
            },
            {
                "source": "Local flutes and drone-flutes packets",
                "url": "../flutes/README.md; ../drone-flutes/design.md",
                "observation": "Open-pipe formulas, Tony's shop workflow, split blank CNC plus lathe method.",
                "used_for": "Acoustic formulas, validation loop, CNC/lathe workflow.",
            },
            {
                "source": "Flutopedia Anasazi tuning note",
                "url": "https://www.flutopedia.com/naf_tunings.htm",
                "observation": "Anasazi-tuned six-hole instruments are commonly modeled with a diatonic-major-without-fourth primary sequence.",
                "used_for": "Starter Alghosazi offsets 0,2,4,7,9,11,12 pending measured validation.",
            },
        ],
        ["source", "url", "observation", "used_for"],
    )
    write_csv(
        "double-drone-spec.csv",
        [
            {
                "assembly_id": "KAVGH-A3-DOUBLE",
                "melody_side": "KAV-A3-5H",
                "drone_side": "A3 drone with rear thumb vent raising to B3",
                "windways": 2,
                "body_strategy": "two separate bores lashed or mechanically joined; melody kaval removable",
                "overall_length_in": "29.1 to 31.0",
                "validation": "Tune melody alone, drone alone, then both together for beating and pressure interaction.",
            },
            {
                "assembly_id": "DALG-AS3-DOUBLE",
                "melody_side": "ALG-AS3-J2 or ALG-AS3-SOLID",
                "drone_side": "reedy/natural-harmonic drone bore with independent windway",
                "windways": 2,
                "body_strategy": "parallel-tube double flute with two mouth inlets; each side playable separately",
                "overall_length_in": "33.1",
                "validation": "Record both windways independently and together; check pressure stealing between ducts.",
            },
        ],
        ["assembly_id", "melody_side", "drone_side", "windways", "body_strategy", "overall_length_in", "validation"],
    )


def bom_rows() -> list[dict[str, object]]:
    return [
        {
            "item": "BOM-001", "assembly": "all", "part": "Primary body blank",
            "qty": "1 per flute", "spec": "Straight-grain elder, locust, ash, maple, cherry, or walnut; length per family-spec plus 2 in trim",
            "make_buy": "buy", "est_cost_usd": "25-90", "source_status": "spec only",
            "drawing_ref": "drawings/*-body.svg", "notes": "Avoid runout through tone holes and joint tenons.",
        },
        {
            "item": "BOM-002", "assembly": "head", "part": "Removable fipple/flue plug",
            "qty": "1 plus 2 test plugs", "spec": "Hard maple, pear, or dense straight-grain scrap; 0.033-0.045 in windway height trials",
            "make_buy": "make", "est_cost_usd": "5", "source_status": "shop scrap ok",
            "drawing_ref": "drawings/fipple-head-section.svg", "notes": "Wax-sealed removable plug makes voicing iteration survivable.",
        },
        {
            "item": "BOM-003", "assembly": "joint", "part": "Cork sheet or natural cork rings",
            "qty": "1 strip per joint", "spec": "1/32 to 1/16 in cork, sanded to airtight slip fit",
            "make_buy": "buy", "est_cost_usd": "8-15", "source_status": "verify before purchase",
            "drawing_ref": "drawings/two-piece-joint.svg", "notes": "Use only on removable joints; permanent split bodies use glue.",
        },
        {
            "item": "BOM-004", "assembly": "joint", "part": "Brass or hardwood ferrule sleeve",
            "qty": "optional", "spec": "Thin brass tube or hardwood collar sized to body OD",
            "make_buy": "buy/make", "est_cost_usd": "10-25", "source_status": "verify diameter",
            "drawing_ref": "drawings/two-piece-joint.svg", "notes": "Recommended for long A/A# bodies and double-flute assemblies.",
        },
        {
            "item": "BOM-005", "assembly": "finish", "part": "Exterior finish",
            "qty": "1", "spec": "Shellac, polymerized oil, or oil/wax; keep windway and bore lightly sealed only after tuning",
            "make_buy": "buy", "est_cost_usd": "10-30", "source_status": "shop stock likely",
            "drawing_ref": "assembly-manual.md", "notes": "No heavy finish on splitting edge.",
        },
        {
            "item": "BOM-006", "assembly": "fixture", "part": "V-block and drilling template stock",
            "qty": "1 set", "spec": "MDF/plywood V-block, laser-cut paper/acrylic hole templates, 1/4 in dowel pins",
            "make_buy": "make", "est_cost_usd": "10-20", "source_status": "shop stock likely",
            "drawing_ref": "cnc/setup-sheet.md", "notes": "Template holes should be undersized pilots.",
        },
        {
            "item": "BOM-007", "assembly": "validation", "part": "Tuning/measurement kit",
            "qty": "1", "spec": "Chromatic tuner, thermometer/hygrometer, calipers, small round files, recording device",
            "make_buy": "use shop kit", "est_cost_usd": "0-60", "source_status": "existing kit likely",
            "drawing_ref": "validation.csv", "notes": "Record temperature with every tuning pass.",
        },
    ]


def write_packet_docs() -> None:
    write_csv(
        "bom.csv", bom_rows(),
        ["item", "assembly", "part", "qty", "spec", "make_buy", "est_cost_usd", "source_status", "drawing_ref", "notes"],
    )
    write_csv(
        "sourcing.csv",
        [
            {
                "component": "straight-grain hardwood blanks", "required_spec": "1.25-1.50 in square or round, 28-38 in long, stable and dry",
                "search_terms": "elder wood blank, locust spindle blank, ash turning blank, maple turning blank",
                "candidate_supplier": "local hardwood dealer / Woodcraft / Rockler / Global Wood Source",
                "price_each": "TBD", "date_checked": "TBD", "lead_time": "TBD", "substitutes": "maple/cherry/walnut for prototype",
                "risk": "Species and grain affect cracking and tone; verify straight grain before purchase.",
            },
            {
                "component": "cork joint material", "required_spec": "thin sheet or rings, sandable, airtight",
                "search_terms": "woodwind tenon cork sheet 1/32 1/16",
                "candidate_supplier": "music repair supplier / Amazon / McMaster",
                "price_each": "TBD", "date_checked": "TBD", "lead_time": "TBD", "substitutes": "waxed hemp thread for tests",
                "risk": "Loose joint leaks; tight joint cracks socket.",
            },
            {
                "component": "brass ferrule sleeve", "required_spec": "ID/OD matched to selected body, thin wall",
                "search_terms": "brass tube 1.25 inch 1.375 inch thin wall",
                "candidate_supplier": "K&S, McMaster, OnlineMetals",
                "price_each": "TBD", "date_checked": "TBD", "lead_time": "TBD", "substitutes": "hardwood collar turned on lathe",
                "risk": "Metal sleeve changes exterior feel and may buzz if poorly fitted.",
            },
            {
                "component": "small brad point drill bits and reamers", "required_spec": "1/8 to 3/8 in, sharp, clean entry",
                "search_terms": "brad point drill bit set small reamer",
                "candidate_supplier": "Woodcraft / Rockler / McMaster",
                "price_each": "TBD", "date_checked": "TBD", "lead_time": "TBD", "substitutes": "number drill bits plus tapered reamer",
                "risk": "Tearout around holes shifts tuning and looks sloppy.",
            },
        ],
        ["component", "required_spec", "search_terms", "candidate_supplier", "price_each", "date_checked", "lead_time", "substitutes", "risk"],
    )
    cut_rows = []
    for m in MEMBERS:
        cut_rows.append({
            "member_id": m.member_id,
            "blank_part": "main body blank",
            "material": m.material,
            "qty": 1,
            "rough_size_in": f"{m.body_od_in + 0.25:.3f} x {m.body_od_in + 0.25:.3f} x {m.total_length_in + 2.0:.3f}",
            "final_size_in": f"OD {m.body_od_in:.3f}, bore {m.bore_id_in:.3f}, length {m.total_length_in:.3f}",
            "grain_orientation": "straight along bore axis",
            "operation": "square, split or bore, route/drill, glue if split, turn/round, tune foot",
            "yield_notes": "Leave 2 in trim for root tuning and chuck/fixture allowance.",
        })
        if "two-piece" in m.construction or "three-piece" in m.construction:
            cut_rows.append({
                "member_id": m.member_id,
                "blank_part": "joint tenon/socket allowance",
                "material": m.material + " plus cork/ferrule",
                "qty": 1,
                "rough_size_in": "extra 2.5 in distributed around joint",
                "final_size_in": "1.250 in tenon engagement, 0.003-0.006 in cork-adjusted compression",
                "grain_orientation": "same as body",
                "operation": "turn tenon/socket after bore alignment is proven",
                "yield_notes": "Cut joint after body is acoustically proven on a sacrificial overlength blank.",
            })
    write_csv(
        "cut-list.csv", cut_rows,
        ["member_id", "blank_part", "material", "qty", "rough_size_in", "final_size_in", "grain_orientation", "operation", "yield_notes"],
    )
    validation_rows = []
    for m in MEMBERS:
        validation_rows.append({
            "member_id": m.member_id,
            "test_id": "VAL-ROOT",
            "target": f"root {m.key}",
            "target_value": f"{m.target_hz:.3f} Hz",
            "measured_value": "",
            "tolerance": "+/-25 cents P1, +/-10 cents P2",
            "environment": "TBD temp/RH",
            "pass_fail": "",
            "action": "Trim foot shorter to raise pitch; rebuild/extend foot if sharp.",
        })
        for h in hole_schedule(m):
            validation_rows.append({
                "member_id": m.member_id,
                "test_id": f"VAL-H{h['hole_no_from_foot']}",
                "target": f"hole {h['hole_no_from_foot']} offset +{h['offset_st']} st",
                "target_value": f"{h['target_hz']} Hz",
                "measured_value": "",
                "tolerance": "+/-25 cents P1, +/-10 cents P2",
                "environment": "TBD temp/RH",
                "pass_fail": "",
                "action": "Enlarge/undercut slowly to raise; wax or bushing recovery if sharp.",
            })
    validation_rows.extend([
        {
            "member_id": "P0-FIPPLE-HEAD", "test_id": "VAL-P0-SPEAK",
            "target": "head tile speaks before full body",
            "target_value": "stable tone with 0.033/0.038/0.045 in plug trials",
            "measured_value": "", "tolerance": "measurement_required",
            "environment": "TBD temp/RH", "pass_fail": "",
            "action": "Record plug shim, window length/width, splitting-edge offset, and tuner capture in docs/p0-fipple-head-measurement.md.",
        },
        {
            "member_id": "P0-FIPPLE-HEAD", "test_id": "VAL-SW-CORR",
            "target": "measured sound-window correction",
            "target_value": "L_eff(measured root) - labium_to_foot - foot_end_correction",
            "measured_value": "", "tolerance": "measurement_required",
            "environment": "TBD temp/RH", "pass_fail": "",
            "action": "Add the back-solved correction to sound-window-correction-log.csv before promoting hole positions beyond starter status.",
        },
        {
            "member_id": "ALL", "test_id": "VAL-FIPPLE",
            "target": "clean attack and stable octave jump", "target_value": "no choking at normal breath",
            "measured_value": "", "tolerance": "subjective plus recording",
            "environment": "TBD temp/RH", "pass_fail": "",
            "action": "Adjust windway height, splitting edge sharpness, and window length.",
        },
        {
            "member_id": "DOUBLE", "test_id": "VAL-DRONE-BEAT",
            "target": "melody/drone pressure interaction", "target_value": "no severe stealing or beating unless intentional",
            "measured_value": "", "tolerance": "recorded comparison",
            "environment": "TBD temp/RH", "pass_fail": "",
            "action": "Restrict windway, retune drone vent, or separate mouth inlets.",
        },
    ])
    write_csv(
        "validation.csv", validation_rows,
        ["member_id", "test_id", "target", "target_value", "measured_value", "tolerance", "environment", "pass_fail", "action"],
    )
    write_csv(
        "sound-window-correction-log.csv",
        [
            {
                "iteration": "P0",
                "member_id": "P0-FIPPLE-HEAD",
                "reference_body": "KAV-A3-5H unholed test body or matching half-bore tile",
                "labium_to_foot_in": "TBD",
                "bore_id_in": "0.8750",
                "foot_end_correction_in": "0.2625",
                "target_root_hz": "220.000",
                "measured_root_hz": "TBD",
                "environment": "TBD temp/RH",
                "backsolve_formula": "L_eff = c/(2*measured_root_hz); sound_window_correction = L_eff - labium_to_foot - foot_end_correction",
                "measured_sound_window_correction_in": "TBD",
                "status": "measurement_required",
                "next_action": "Build P0, capture tuner result, then update workbook/family-spec/hole schedules if the correction shifts holes by more than 0.100 in.",
            }
        ],
        [
            "iteration", "member_id", "reference_body", "labium_to_foot_in",
            "bore_id_in", "foot_end_correction_in", "target_root_hz",
            "measured_root_hz", "environment", "backsolve_formula",
            "measured_sound_window_correction_in", "status", "next_action",
        ],
    )
    write_csv(
        "validation-loop.csv",
        [
            {
                "check_id": "vl001",
                "packet_artifact": "docs/p0-fipple-head-measurement.md",
                "readiness_before": "L1_packet",
                "prediction_source": "fujara-style head starter dimensions",
                "target": "P0 head tile speaks cleanly with recorded windway/window setup",
                "tolerance": "measurement_required",
                "method": "Build scrap P0 tile; test three plug shims; record audio/tuner and physical settings.",
                "measured_result": "TBD",
                "status": "measurement_required",
                "next_action": "Do not commit full-body hole schedule until one speaking head setup is logged.",
                "evidence": "future tuner capture, photo set, and shop log",
            },
            {
                "check_id": "vl002",
                "packet_artifact": "sound-window-correction-log.csv",
                "readiness_before": "L1_packet",
                "prediction_source": "open-open model plus source-observed body lengths",
                "target": "Back-solved sound-window correction for KAV-A3-5H or matched P0 body",
                "tolerance": "measurement_required",
                "method": "Measure unholed root, compute L_eff=c/(2f), subtract labium-to-foot and foot end correction.",
                "measured_result": "TBD",
                "status": "measurement_required",
                "next_action": "Update workbook, family-spec, and hole schedules only after this row has measured data.",
                "evidence": "future sound-window-correction-log.csv measured row",
            },
        ],
        [
            "check_id", "packet_artifact", "readiness_before", "prediction_source",
            "target", "tolerance", "method", "measured_result", "status",
            "next_action", "evidence",
        ],
    )

    write_text("README.md", README_MD)
    write_text("design.md", DESIGN_MD)
    write_text("assembly-manual.md", ASSEMBLY_MD)
    write_text("drawing-brief.md", DRAWING_BRIEF_MD)
    write_text("visual-bom-brief.md", VISUAL_BOM_MD)
    write_text("supplier-rfq.md", SUPPLIER_RFQ_MD)
    write_text("risks.md", RISKS_MD)
    write_text("photo-shotlist.md", PHOTO_SHOTLIST_MD)
    write_text("sources.md", SOURCES_MD)
    write_text("wolfram-starter.wl", WOLFRAM_STARTER)
    write_text("cad/SolidWorks-MasterLayout-Plan.md", SW_PLAN_MD)
    write_text("cad/sw-global-variables.csv", SW_GLOBALS_CSV)
    write_text("cad/design-table-inputs.csv", SW_DESIGN_INPUTS_CSV)
    write_text("cad/kaval_alghosazi_body.scad", OPENSCAD_SCAD)
    write_text("docs/repo-structure.md", REPO_STRUCTURE_MD)
    write_text("docs/v4.2-validation-notes.md", VALIDATION_NOTES_MD)
    write_text("docs/p0-fipple-head-measurement.md", P0_FIPPLE_HEAD_MEASUREMENT_MD)
    write_text("LICENSE", LICENSE_MD)
    write_text(".gitignore", "*.tmp\n*.bak\n.~lock.*\n.DS_Store\n__pycache__/\n")


README_MD = """
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
| `hole-schedule.csv` | First-pass hole positions measured from labium and foot. |
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

## Status

This is a first-pass engineering packet. Dimensions are parametric and source-backed where possible, but the fipple/sound-window correction is marked as a measured-prototype variable, not a borrowed NAF K2 correction.

Current readiness is `L1_packet`: fabrication drawings and schedules are starter artifacts, while the fipple/head correction, final hole locations, and production readiness remain measurement-required.

## Attribution

The kaval references come from Moldavian/Romanian shepherd-flute practice; the Alghosazi references point toward Anasazi/Basketmaker flute replicas and contemporary adaptations. This packet is a modern shop design by Tony Koop, built with respect for those lineages and explicit source notes in `sources.md`.
"""


DESIGN_MD = """
# Kaval + Alghosazi Fipple Flutes

**Packet ID:** KAV-ALG-FAM-001  
**Family:** open-pipe woodwind / duct-fipple flute  
**Pipeline:** cnc-lathe hybrid: split blank or deep bore, fipple head, lathe rounding, optional two-piece joint  
**Date:** 2026-05-06  
**Done-bar references:** `fujara`, `flutes`, `drone-flutes`, `pistalka`, `transverse-flute`

## Project Intent

Design a buildable family of long fipple kavals and Alghosazi flutes that feel close to the Fujara Flutes references while using Tony's existing fujara/flute workshop logic: parametric dimensions, a controllable fipple sound-window head, split-blank CNC or deep-bore construction, validation tables, and documented tuning loops.

The first physical goal is not a perfect production run. It is a controlled prototype ladder: prove the fipple head, build one A3 5-hole kaval, build one A#3 Alghosazi with a thumb hole, then decide whether the two-piece and double-drone versions deserve full CAD.

## Source And Scope

External reference pages checked:

- Fujara Flutes Kaval page: 5-hole fipple kavals, 7-hole expanded kavals, lengths from about 62-90 cm, and double Kaval/Kavalghoza drone concept.
- Fujara Flutes Alghosazi page: fipple adaptation of Anasazi-style flute, top hole moved to the back as a thumb hole, lengths from about 70-85 cm, and a double-drone option.
- Flutopedia Anasazi tuning notes: used only to justify the Alghosazi starter offset set as an Anasazi-derived primary sequence.

Local source artifacts inspected:

- `fujara/design-table/fujara_equations.md` and SolidWorks dimension extracts for fipple/flue plug geometry.
- `drone-flutes/design.md` and `flutes/skills/parametric-design-table.md` for open-pipe, shop, and validation workflow.
- `pistalka/docs/build-packet/design.md` for a compact fipple-flute build sequence.

## Governing Model

These flutes are modeled as **open-open cylindrical fipple flutes** with a non-NAF fujara-style sound-window end correction.

```text
f = c / (2 * L_eff)
c = 13552 in/s at about 68 F
L_eff = physical_labium_to_foot + foot_end_correction + sound_window_correction
foot_end_correction ~= 0.6 * bore_radius
sound_window_correction = measured prototype value, not Tony's NAF K2 table
```

For first-pass hole placement, the packet uses a proportional open-pipe layout:

```text
x_from_labium = labium_to_foot * 2^(-semitone_offset / 12)
x_from_foot = labium_to_foot - x_from_labium
```

The hole schedule is intentionally a **starter drill schedule**. The builder drills undersized, tunes the root by trimming the foot, then opens each hole upward by careful reaming/undercutting. If a hole goes sharp, the recovery is wax test, bushing, or a rebuilt body.

`family-spec.csv` includes `estimated_sound_window_correction_in`. Positive values mean the fipple/window system or added acoustic path must make the instrument behave longer than the visible labium-to-foot length. Negative values mean the source-observed body length is overlong for the nominal root under a simple open-pipe model; treat those as overlength blanks to trim or as evidence that the commercial key naming may not equal the all-closed root.

The first-pass schedules do not yet include a measured sound-window correction. Back-solve it after P0 with:

```text
L_eff_measured = c / (2 * measured_root_hz)
sound_window_correction = L_eff_measured - labium_to_foot - foot_end_correction
foot_end_correction ~= 0.6 * bore_radius
```

Record the result in `sound-window-correction-log.csv`. Only then update `Kaval-Alghosazi-Design.xlsx`, `family-spec.csv`, and the hole schedules.

## Scale Plans

### 5-Hole Fipple Kaval

The 5-hole kaval follows the published C-reference pitch set:

```text
0, +2, +3, +6, +7, +8 semitones
Example in C: C D D# F# G G#
```

### 7-Hole Fipple Kaval

The expanded kaval adds the two half-step options described by the reference page:

```text
0, +2, +3, +4, +6, +7, +8, +9 semitones
Example in C: C D D# E F# G G# A
```

### Alghosazi

The Alghosazi starter scale uses an Anasazi-derived primary sequence. The top hole is placed on the back as a thumb hole, matching the design note from the reference page.

```text
0, +2, +4, +7, +9, +11, +12 semitones
Example in A#: A# C D F G A A#
```

This is marked as a musical-design assumption. If Tony wants a different Alghosazi mode after listening to examples, change the offsets in `Kaval-Alghosazi-Design.xlsx` and regenerate `hole-schedule.csv`.

## Fujara-Style Fipple Head

The requested head architecture is:

```text
mouth at end -> rectangular inlet -> internal windway/flue -> side true sound window -> splitting edge -> main bore
```

Starter dimensions:

| Feature | Kaval Starter | Alghosazi Starter | Notes |
| --- | ---: | ---: | --- |
| Top end to true window datum | 1.45-1.65 in | 1.65-1.80 in | Adjust for comfort and joint location. |
| Windway height | 0.033-0.045 in | 0.035-0.048 in | Start with removable flue plug trials. |
| Windway width | 0.45-0.55 in | 0.45-0.58 in | About 55-65 percent of bore. |
| Window length | 0.25-0.38 in | 0.28-0.42 in | Widen/lengthen only after tone test. |
| Splitting edge offset KPI | 0.005-0.015 in | 0.005-0.015 in | Borrowed from Tony's fujara canary, not a final law. |
| Plug fit | wax-sealed slip | wax-sealed slip | Removable until final voicing. |

### P0 Measurement Loop

Build `P0-FIPPLE-HEAD` before a full flute body. Use scrap stock or a short half-bore test channel matching the selected bore, cut the end mouth inlet, test removable plug shims at 0.033, 0.038, and 0.045 in, and vary only one window or splitting-edge parameter between trials.

For each speaking trial, log the measured windway height, window length, window width, splitting-edge offset, blow-pressure note, temperature/RH, measured root pitch, and whether the tone chokes, overblows, or stabilizes. The geometry stays inferred until that log exists.

## Two-Piece And Double Options

The two-piece option is a **shop convenience and tuning risk**, not a decorative afterthought. Use it only after a solid prototype speaks well.

- Tenon engagement: 1.25 in minimum.
- Cork compression: fit by sanding; no forced assembly.
- Joint location: avoid placing the joint within 0.75 in of a tone hole.
- Bore step: less than 0.005 in at the joint after final sanding.
- Ferrule: recommended for A/A# bodies and double-flute assemblies.

Double-drone versions are documented in `double-drone-spec.csv` and `drawings/double-drone-layout.svg`. Each side gets its own windway so the melody flute can be played alone and the drone can be tuned independently.

## Family Table

See `family-spec.csv` for the source of truth. The core starter members are:

| Member | Role |
| --- | --- |
| `KAV-A3-5H` | First kaval prototype. |
| `KAV-AS3-7H` | Two-piece expanded kaval prototype. |
| `ALG-AS3-J2` | First Alghosazi prototype. |
| `ALG-A3-J3` | Three-piece Alghosazi joint stress test. |

## Manufacturing Path

Preferred path for the first two prototypes:

1. Make a removable fipple-head test tile from scrap.
2. Record the speaking head settings and back-solve the sound-window correction in `sound-window-correction-log.csv`.
3. Build a split-blank body so the bore, windway, and window are visible and correctable.
4. Glue and turn only after the fipple speaks.
5. Drill holes undersized from a laser/CNC template or V-block setup.
6. Tune root first, then holes from foot upward.
7. Record measurements in `validation.csv` and `validation-loop.csv`, then update the next prototype.

Deep-bore drilling is allowed for later solid-body builds. Use the skill reference `headstock-driven-deep-bore-drilling.md` before attempting a long solid blank.

## Assumptions

- A4 = 440 Hz.
- 68 F speed-of-sound baseline.
- Website lengths are used as precedent dimensions, not guaranteed acoustic formulas.
- Alghosazi tuning is a starter interpretation based on contemporary Anasazi-tuned six-hole practice.
- Tone hole positions ignore final hole-diameter perturbation until measured prototype data exists.
- The fipple head is Tony's derived design and must be validated by physical tests.
- The P0 correction is unknown until measured; do not promote this packet above `L1_packet` from source observations alone.
"""


ASSEMBLY_MD = """
# Assembly Manual

## Safety And Setup

- Wear eye and lung protection when drilling, routing, sanding, or turning.
- Do not route a long round blank without a stable V-block or split-blank fixture.
- Keep the splitting edge protected until final voicing.
- Mark the labium datum, foot datum, bore centerline, and back thumb-hole line before any irreversible cut.

## Prototype Ladder

### P0: Fipple Head Tile

1. Cut a 4 in scrap block with the selected bore diameter or a half-bore test channel.
2. Cut the end mouth inlet.
3. Fit a removable flue plug with 0.033, 0.038, and 0.045 in shim trials.
4. Cut a side true sound window and splitting edge.
5. Blow through the end inlet and record which plug/window combination speaks cleanly.
6. Do not build a full flute until this tile produces stable tone.

### P1: First Kaval Body

1. Select `KAV-A3-5H`.
2. Mill the blank overlength by at least 2 in.
3. Split the blank, route the bore halves and registration pin holes, or deep-bore the solid blank after proving setup on scrap.
4. Create the fipple head and removable plug.
5. Prove the root tone with no finger holes.
6. Trim the foot to bring the all-closed root toward A3.
7. Transfer hole positions from `kaval-hole-schedule.csv`.
8. Drill each hole undersized.
9. Tune holes from the foot upward by reaming slowly.
10. Record every before/after pitch in `validation.csv`.

### P1: First Alghosazi Body

1. Select `ALG-AS3-J2`.
2. Build as a solid body first if joint risk feels high; otherwise cut the two-piece joint after the bore is proven.
3. Mark the rear thumb-hole line before drilling.
4. Drill the thumb hole undersized and validate reach with the actual player grip.
5. Tune the primary sequence and record whether the scale feels musically right.

### P2: Jointed Version

1. Cut the body overlength and prove tone before final jointing.
2. Locate the joint away from holes and away from the fipple head.
3. Turn tenon and socket with a 1.25 in engagement target.
4. Add cork or waxed thread until the joint seals without force.
5. Check bore step with a dowel, light, and feeler test.
6. Re-test root and all holes after the joint is fitted.

### P3: Double Drone

1. Build melody and drone tubes separately.
2. Tune the melody side alone.
3. Tune the drone side alone, including rear thumb vent if used.
4. Join the bodies temporarily with clamps or bands before permanent collars.
5. Test pressure sharing with both windways.
6. Only then commit to a permanent double-body fixture or decorative binding.

## Finishing

- Finish exterior after tuning.
- Keep heavy oil, shellac, and wax out of the windway and splitting edge.
- Seal bore lightly only after final measurements.
- Recheck pitch after finish cure.

## Maintenance

- Let the bore dry after playing.
- Remove the fipple plug only if the design uses a wax-sealed removable plug.
- Do not store jointed bodies assembled under high humidity swings.
"""


DRAWING_BRIEF_MD = """
# Drawing Brief

## Required Views

- Family overview: each member as a scaled open-pipe body with bore ID and total length.
- Hole layout: kaval and Alghosazi separate, measured from labium and from foot.
- Fipple head section: end mouth inlet, windway, flue plug, true sound window, splitting edge, bore.
- Two-piece joint section: tenon, socket, cork wrap, ferrule/collar, bore continuity.
- Double-drone layout: two bores, independent windways, melody side, drone side, thumb vent.

## Datums

- Datum A: labium/splitting-edge plane.
- Datum B: tuned foot end.
- Datum C: bore centerline.
- Datum D: back thumb-hole centerline for Alghosazi.

## Tolerances

- Bore ID: +/-0.005 in after reaming/lapping.
- Hole center: +/-0.020 in before tuning; final pitch matters more than nominal center.
- Windway height: +/-0.002 in once a plug speaks.
- Joint bore step: less than 0.005 in.
- Noncritical exterior: +/-0.030 in.

## Drawing Outputs

Generated SVGs live in `drawings/`. Build-critical dimensions come from `Kaval-Alghosazi-Design.xlsx`, `family-spec.csv`, and `hole-schedule.csv`, not from raster images.
"""


VISUAL_BOM_MD = """
# Visual BOM Brief

Create one image-forward BOM plate with:

- hero view of a kaval, an Alghosazi, and the fipple-head section;
- item rows for body blank, fipple plug, cork/ferrule, drilling template, finish, and validation tools;
- callouts that distinguish make vs buy parts;
- source status labels: verified price, spec only, or shop stock.

Image sources:

- Use real shop photos after P0/P1 prototypes exist.
- Until then, use `images/hero.png` and the SVG drawings as concept placeholders.
- Do not use vendor or Fujara Flutes photos directly in the BOM without permission.
"""


SUPPLIER_RFQ_MD = """
# Supplier RFQ Draft

Subject: Quote request for straight-grain woodwind blanks and optional ferrule stock

Hello,

I am building a small run of long fipple flutes and need stable straight-grain blanks suitable for bored woodwind bodies.

Please quote the following:

- 4 to 8 blanks, 1.25 to 1.50 in square or round, 30 to 38 in long.
- Species options: elder, locust, ash, maple, cherry, walnut, or similar stable hardwood.
- Moisture content and straightness/grain-runout information.
- Any longer stock suitable for 85-90 cm flute bodies.
- Optional thin-wall brass tube or hardwood ferrule stock around 1.25 to 1.40 in ID/OD range.

The blanks will be drilled or split-routed along the long axis, then turned and tuned, so straight grain and low checking risk matter more than figure.

Please include unit price, volume price, lead time, shipping estimate, and any recommended substitutes.

Thank you,
Tony Koop
"""


RISKS_MD = """
# Risks

## Acoustic

- **Fipple/sound-window correction is unknown.** Test: build `P0-FIPPLE-HEAD`, record root prediction vs measured, and update `sound-window-correction-log.csv` before trusting final hole locations.
- **Hole positions are first-pass proportional.** Test: drill undersized and record before/after cents for every hole in `validation.csv`.
- **Double-drone windways may steal pressure from each other.** Test: record each windway alone and together; compare attack and cents drift.

## Structural

- **Long solid blanks can wander while drilling.** Test: bore scrap first and measure exit offset; use split-blank CNC if wander exceeds 0.050 in.
- **Two-piece joints can leak or crack.** Test: vacuum/leak check and dry assembly force check before finishing.
- **Splitting edge is fragile.** Test: inspect under magnification after each voicing change.

## Ergonomic

- **7-hole kaval lower holes may require base-of-finger coverage.** Test: paper wrap mockup before drilling final diameters.
- **Alghosazi thumb hole may not fit all hands.** Test: mark with tape, play air-grip, then drill undersized.

## Supply

- **Elder and locust blanks may be hard to source in required lengths.** Test: verify supplier stock before committing scale/key; use ash/maple/cherry for prototypes.
- **Ferrule dimensions may not match body OD.** Test: choose ferrule after body OD is turned, not before.

## Fit And Finish

- **Finish can clog the windway.** Test: mask windway and splitting edge; recheck attack after cure.
- **Cork compression changes with humidity.** Test: assemble/disassemble after overnight humidity change and record fit.
"""


PHOTO_SHOTLIST_MD = """
# Photo Shotlist

Follow the repo-level photo pipeline style: real process photos replace concept placeholders as soon as shop work begins.

## P0 Fipple Head

- End mouth inlet before plug install.
- Removable flue plugs with shim labels.
- Side true sound window and splitting edge closeup.
- Tuner screenshot or phone photo during first tone.

## P1 Bodies

- Blank selection with grain orientation marked.
- Split blank or deep-bore setup.
- Routed/bored bore before glue-up.
- Hole template wrapped around body.
- First drilled undersized hole.
- Final tuned flute full length.

## Jointed/Double Options

- Tenon/socket before cork.
- Cork/ferrule fit closeup.
- Double-body temporary clamp test.
- Independent windways at the mouth end.

## Finished Portfolio

- Kaval and Alghosazi side by side.
- Player hand reach shot.
- Fipple head detail.
- Validation/tuning bench shot.
"""


SOURCES_MD = """
# Sources And Provenance

## External Pages Checked

- Fujara Flutes Kaval page: https://www.fujaraflutes.com/moldavian-kaval-flutes
- Fujara Flutes Alghosazi page: https://www.fujaraflutes.com/alghosazi
- Flutopedia Native American flute tunings / Anasazi note: https://www.flutopedia.com/naf_tunings.htm

## Local Sources Used

- `../fujara/README.md`
- `../fujara/design-table/fujara_equations.md`
- `../fujara/CAD/fujara-body/G2Fujara_Assembly.SLDASM_dimensions.csv`
- `../drone-flutes/design.md`
- `../flutes/skills/parametric-design-table.md`
- `../pistalka/docs/build-packet/design.md`

## Source-Backed Facts Used

- The kaval reference page presents fipple-style kavals and gives 5-hole and 7-hole pitch sets.
- The same page documents examples in G#, A, B, C and a double Kaval/Kavalghoza drone concept.
- The Alghosazi reference page frames the instrument as an easier fipple adaptation of an Anasazi-style flute and notes the rear thumb-hole idea.
- Tony's fujara CAD records a fipple/flue plug system with narrow windway, removable plug logic, and splitting-edge KPI values.

## Assumptions Needing Prototype Data

- Exact fipple sound-window end correction.
- Measured P0 windway/window/splitting-edge setting that speaks without choking.
- Final hole diameters and undercutting.
- Alghosazi mode preference after listening/playing.
- Joint effect on tuning and response.
"""


WOLFRAM_STARTER = """
(* Kaval + Alghosazi starter. Full v4.2 packet source is in wolfram/instrument-model.wl after generation. *)
ClearAll["Global`*"];
cInPerSec = 13552;
freqFromMidi[midi_, a4_: 440] := a4*2^((midi - 69)/12);
openPipeLeff[f_] := cInPerSec/(2*f);
holeFromLabium[labiumToFoot_, semitoneOffset_] := labiumToFoot*2^(-semitoneOffset/12);
centsError[measured_, target_] := 1200*Log[2, measured/target];
"""


SW_PLAN_MD = """
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
"""


SW_GLOBALS_CSV = """name,value_in,scope,notes
g_speed_of_sound,13552,global,in/s at about 68 F
g_a4_reference,440,global,Hz
g_windway_height,0.038,head,start with removable plug shims 0.033-0.045
g_windway_width,0.500,head,adjust per bore
g_window_length,0.320,head,starter true sound window length
g_window_width,0.500,head,about 55-65 percent of bore
g_splitting_edge_offset,0.009,head,driven KPI target from fujara-style canary
g_joint_tenon_length,1.250,joint,min engagement
g_joint_cork_allowance,0.006,joint,sand to fit
c_glue_gap,0.003,fit,permanent split blank glue line target
c_wax_seal_fit,0.003,fit,removable flue plug wax seal target
"""


SW_DESIGN_INPUTS_CSV = "member_id,target_note,total_length_in,bore_id_in,body_od_in,top_to_window_in,hole_count,construction\n" + "\n".join(
    f"{m.member_id},{m.key},{m.total_length_in:.3f},{m.bore_id_in:.4f},{m.body_od_in:.4f},{m.top_to_window_in:.3f},{len(m.hole_offsets)},{m.construction}"
    for m in MEMBERS
) + "\n"


OPENSCAD_SCAD = r"""
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
"""


REPO_STRUCTURE_MD = """
# Repository Structure

This is a root-level project-repo packet with build-packet artifacts at the top level, matching Tony's existing `drone-flutes`, `gemshorn`, and `transverse-flute` style.

Generated directories:

- `cad/` - OpenSCAD, SolidWorks design table inputs, global variables.
- `cnc/` - v4.2 pre-CAM operation plan.
- `data/` - guided intake and source observations.
- `drawings/` - manufacturing SVG drawings.
- `images/` - concept placeholder and future build photos.
- `site/` - static build-log site.
- `wolfram/` - generated Wolfram model package.
"""


VALIDATION_NOTES_MD = """
# v4.2 Validation Notes

The packet intentionally does not apply Tony's Native American flute K2 correction table to this head. These instruments use a fujara-style true sound window and internal flue, so the sound-window correction must be measured.

Measured, inferred, and unknown geometry are separated as follows:

- Measured: none yet for the P0 fipple head in this repository.
- Inferred: fujara-style windway/window starter dimensions and source-observed body lengths.
- Unknown: the actual sound-window correction, final hole perturbation, and production-ready fipple setting.

Before final CAD:

1. Build `P0-FIPPLE-HEAD` from scrap or a short matching-bore tile.
2. Record the root pitch of an unholed body or matched test channel with temperature/RH.
3. Back-solve the sound-window correction with `L_eff = c/(2 * measured_root_hz)` and `sound_window_correction = L_eff - labium_to_foot - foot_end_correction`.
4. Record the result in `sound-window-correction-log.csv`.
5. Update `Kaval-Alghosazi-Design.xlsx`.
6. Regenerate `hole-schedule.csv` if offsets move more than 0.100 in.
7. Keep readiness at `L1_packet` until the measured correction and tuning rows exist.
"""


P0_FIPPLE_HEAD_MEASUREMENT_MD = """
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
"""


LICENSE_MD = """
CC-BY 4.0 summary for project documentation.

You may share and adapt this engineering documentation with attribution to Tony Koop. Cultural lineages and referenced makers are credited in sources.md; this packet is not a claim to own those traditions.
"""


def write_guided_intake() -> None:
    intake = {
        "instrument_id": "KAV-ALG-FAM-001",
        "family": "open-pipe duct/fipple flute",
        "instrument_type": "Kaval and Alghosazi fipple flute family",
        "variant_size": "5-hole kaval, 7-hole kaval, Alghosazi, double-drone options",
        "key_scale": "Kaval gypsy mode and Anasazi-derived Alghosazi mode",
        "target_fundamental_hz": "207.652-261.626 Hz family range",
        "primary_material": "elder/locust/ash/maple/cherry/walnut",
        "construction_pipeline": "cnc-lathe hybrid, split blank or deep bore, fujara-style fipple head",
        "design_workbook": "Kaval-Alghosazi-Design.xlsx",
        "design_sheet": "Family_Spec",
        "master_workbook": "../Instrument Workshop Master v3.xlsx (not edited)",
        "done_bar_repo": "fujara, flutes, drone-flutes, pistalka",
        "notes": "Fuzzy user request converted to explicit family packet; unknowns remain in validation notes.",
        "generated_on": DATE,
    }
    write_text("data/design-intake.json", json.dumps(intake, indent=2) + "\n")
    write_csv(
        "data/design-input-row.csv",
        [intake],
        [
            "instrument_id", "family", "instrument_type", "variant_size",
            "key_scale", "target_fundamental_hz", "primary_material",
            "construction_pipeline", "design_workbook", "design_sheet",
            "master_workbook", "done_bar_repo", "notes",
        ],
    )


def xlsx_col(n: int) -> str:
    out = ""
    while n:
        n, r = divmod(n - 1, 26)
        out = chr(65 + r) + out
    return out


def cell_xml(row: int, col: int, value: object) -> str:
    ref = f"{xlsx_col(col)}{row}"
    if isinstance(value, tuple) and value and value[0] == "formula":
        formula = escape(str(value[1]))
        cached = escape(str(value[2] if len(value) > 2 else ""))
        return f'<c r="{ref}"><f>{formula}</f><v>{cached}</v></c>'
    if isinstance(value, (int, float)):
        return f'<c r="{ref}"><v>{value}</v></c>'
    return f'<c r="{ref}" t="inlineStr"><is><t>{escape(str(value))}</t></is></c>'


def sheet_xml(rows: list[list[object]]) -> str:
    data = []
    for r_idx, row in enumerate(rows, start=1):
        cells = "".join(cell_xml(r_idx, c_idx, value) for c_idx, value in enumerate(row, start=1))
        data.append(f'<row r="{r_idx}">{cells}</row>')
    return (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<worksheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" '
        'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">'
        '<sheetData>' + "".join(data) + '</sheetData></worksheet>'
    )


def write_xlsx() -> None:
    sheets: list[tuple[str, list[list[object]]]] = []
    sheets.append((
        "Master_Inputs",
        [
            ["name", "value", "units", "notes"],
            ["speed_of_sound", C_IN_PER_SEC, "in/s", "68 F baseline"],
            ["A4_reference", A4, "Hz", "concert pitch"],
            ["windway_height_min", 0.033, "in", "fipple plug trial"],
            ["windway_height_nom", 0.038, "in", "starter"],
            ["windway_height_max", 0.045, "in", "fipple plug trial"],
            ["splitting_edge_offset_min", 0.005, "in", "target KPI"],
            ["splitting_edge_offset_nom", 0.009, "in", "Tony fujara-style canary"],
            ["splitting_edge_offset_max", 0.015, "in", "target KPI"],
            ["joint_tenon_length", 1.25, "in", "minimum engagement"],
        ],
    ))
    family_header = [
        "member_id", "instrument", "key", "midi", "target_hz_formula",
        "target_hz_cached", "total_length_in", "bore_id_in", "body_od_in",
        "labium_to_foot_in", "open_pipe_leff_formula", "sound_window_corr_formula",
        "hole_offsets_st", "source_basis",
    ]
    family_rows: list[list[object]] = [family_header]
    for idx, m in enumerate(MEMBERS, start=2):
        family_rows.append([
            m.member_id, m.instrument, m.key, m.midi,
            ("formula", f"Master_Inputs!$B$3*2^((D{idx}-69)/12)", round(m.target_hz, 3)),
            round(m.target_hz, 3), round(m.total_length_in, 3), m.bore_id_in, m.body_od_in,
            round(m.labium_to_foot_in, 3),
            ("formula", f"Master_Inputs!$B$2/(2*F{idx})", round(m.open_pipe_leff_in, 3)),
            ("formula", f"K{idx}-J{idx}", round(m.estimated_sound_window_correction_in, 3)),
            " ".join(str(o) for o in m.hole_offsets), m.source_basis,
        ])
    sheets.append(("Family_Spec", family_rows))
    hole_rows: list[list[object]] = [[
        "member_id", "hole_no_from_foot", "offset_st", "target_hz",
        "x_from_labium_in", "x_from_foot_in", "starter_drill_in",
        "target_final_dia_in", "orientation", "formula",
    ]]
    for m in MEMBERS:
        for h in hole_schedule(m):
            hole_rows.append([
                h["member_id"], h["hole_no_from_foot"], h["offset_st"],
                h["target_hz"], h["x_from_labium_in"], h["x_from_foot_in"],
                h["starter_drill_in"], h["target_final_dia_in"],
                h["orientation"], h["formula"],
            ])
    sheets.append(("Hole_Schedules", hole_rows))
    sheets.append((
        "Fipple_Head",
        [
            ["feature", "starter_value_in", "range_or_formula", "notes"],
            ["top_to_window", 1.6, "see family-spec", "end mouth inlet to true sound window datum"],
            ["windway_height", 0.038, "0.033-0.045", "use removable plugs"],
            ["windway_width", 0.5, "0.55-0.65*bore_id", "adjust after P0"],
            ["window_length", 0.32, "0.25-0.42", "length along body"],
            ["window_width", 0.5, "0.55-0.65*bore_id", "start narrow"],
            ["splitting_edge_offset", 0.009, "0.005-0.015", "driven KPI"],
        ],
    ))
    sheets.append((
        "Validation_Template",
        [
            ["field", "formula_or_note"],
            ["cents_error", "=1200*LOG(measured_hz/target_hz,2)"],
            ["root tuning", "trim foot to raise; rebuild or sleeve if sharp"],
            ["hole tuning", "enlarge to raise; wax/bush if sharp"],
        ],
    ))

    path = ROOT / "Kaval-Alghosazi-Design.xlsx"
    with zipfile.ZipFile(path, "w", compression=zipfile.ZIP_DEFLATED) as z:
        z.writestr("[Content_Types].xml", CONTENT_TYPES_XML.format(
            overrides="\n".join(
                f'<Override PartName="/xl/worksheets/sheet{i}.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"/>'
                for i in range(1, len(sheets) + 1)
            )
        ))
        z.writestr("_rels/.rels", ROOT_RELS_XML)
        z.writestr("docProps/core.xml", CORE_XML)
        z.writestr("docProps/app.xml", APP_XML)
        z.writestr("xl/workbook.xml", WORKBOOK_XML.format(
            sheets="\n".join(
                f'<sheet name="{escape(name)}" sheetId="{i}" r:id="rId{i}"/>'
                for i, (name, _) in enumerate(sheets, start=1)
            )
        ))
        z.writestr("xl/_rels/workbook.xml.rels", WORKBOOK_RELS_XML.format(
            rels="\n".join(
                f'<Relationship Id="rId{i}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet" Target="worksheets/sheet{i}.xml"/>'
                for i in range(1, len(sheets) + 1)
            )
        ))
        z.writestr("xl/styles.xml", STYLES_XML)
        for i, (_, rows) in enumerate(sheets, start=1):
            z.writestr(f"xl/worksheets/sheet{i}.xml", sheet_xml(rows))


CONTENT_TYPES_XML = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
<Default Extension="xml" ContentType="application/xml"/>
<Override PartName="/xl/workbook.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet.main+xml"/>
{overrides}
<Override PartName="/xl/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.styles+xml"/>
<Override PartName="/docProps/core.xml" ContentType="application/vnd.openxmlformats-package.core-properties+xml"/>
<Override PartName="/docProps/app.xml" ContentType="application/vnd.openxmlformats-officedocument.extended-properties+xml"/>
</Types>"""

ROOT_RELS_XML = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="xl/workbook.xml"/>
<Relationship Id="rId2" Type="http://schemas.openxmlformats.org/package/2006/relationships/metadata/core-properties" Target="docProps/core.xml"/>
<Relationship Id="rId3" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/extended-properties" Target="docProps/app.xml"/>
</Relationships>"""

WORKBOOK_XML = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<workbook xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">
<sheets>{sheets}</sheets>
</workbook>"""

WORKBOOK_RELS_XML = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
{rels}
<Relationship Id="rId100" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/>
</Relationships>"""

STYLES_XML = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<styleSheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main">
<fonts count="1"><font><sz val="11"/><name val="Calibri"/></font></fonts>
<fills count="1"><fill><patternFill patternType="none"/></fill></fills>
<borders count="1"><border><left/><right/><top/><bottom/><diagonal/></border></borders>
<cellStyleXfs count="1"><xf numFmtId="0" fontId="0" fillId="0" borderId="0"/></cellStyleXfs>
<cellXfs count="1"><xf numFmtId="0" fontId="0" fillId="0" borderId="0" xfId="0"/></cellXfs>
</styleSheet>"""

CORE_XML = f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<cp:coreProperties xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:dcmitype="http://purl.org/dc/dcmitype/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
<dc:title>Kaval-Alghosazi-Design</dc:title><dc:creator>Tony Koop</dc:creator>
<dcterms:created xsi:type="dcterms:W3CDTF">{DATE}T00:00:00Z</dcterms:created>
</cp:coreProperties>"""

APP_XML = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Properties xmlns="http://schemas.openxmlformats.org/officeDocument/2006/extended-properties">
<Application>instrument-maker-v4.2</Application>
</Properties>"""


def svg_header(width: int, height: int) -> str:
    return f'<?xml version="1.0" encoding="UTF-8"?><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}" font-family="Arial, Helvetica, sans-serif">'


def write_custom_drawings() -> None:
    head = svg_header(1000, 540) + """
<rect width="1000" height="540" fill="white" stroke="black"/>
<text x="40" y="45" font-size="24" font-weight="bold">Fujara-Style End-Mouth Fipple Head Section</text>
<text x="40" y="72" font-size="13">Air path: end mouth inlet -> windway/flue plug -> true sound window -> splitting edge -> main bore</text>
<rect x="120" y="170" width="720" height="130" rx="18" fill="#f3c37d" stroke="#4a2a10" stroke-width="3"/>
<rect x="120" y="210" width="720" height="50" fill="#fff8e8" stroke="#4a2a10" stroke-width="2"/>
<rect x="120" y="210" width="105" height="50" fill="#111"/>
<text x="92" y="200" font-size="13">end mouth inlet</text>
<rect x="240" y="198" width="380" height="18" fill="#d89a4a" stroke="#4a2a10"/>
<text x="335" y="188" font-size="13">removable flue plug / windway 0.033-0.045 in</text>
<rect x="620" y="160" width="95" height="68" fill="white" stroke="#4a2a10" stroke-width="2"/>
<polygon points="715,228 780,170 780,245" fill="#be7d36" stroke="#4a2a10" stroke-width="2"/>
<text x="615" y="145" font-size="13">true sound window</text>
<text x="745" y="160" font-size="13">splitting edge</text>
<line x1="120" y1="235" x2="840" y2="235" stroke="#555" stroke-dasharray="8,6"/>
<text x="400" y="330" font-size="13">main bore continues to tuned foot</text>
<line x1="225" y1="360" x2="620" y2="360" stroke="black" marker-end="url(#arrow)"/>
<text x="330" y="385" font-size="13">controlled air jet</text>
<defs><marker id="arrow" markerWidth="10" markerHeight="10" refX="6" refY="3" orient="auto"><path d="M0,0 L0,6 L7,3 z" fill="black"/></marker></defs>
<text x="40" y="480" font-size="12">Build note: prove this geometry as P0 before drilling a full flute body. Keep the plug removable until final voicing.</text>
</svg>
"""
    write_text("drawings/fipple-head-section.svg", head)

    joint = svg_header(1000, 460) + """
<rect width="1000" height="460" fill="white" stroke="black"/>
<text x="40" y="45" font-size="24" font-weight="bold">Two-Piece Joint Section</text>
<rect x="90" y="170" width="360" height="95" fill="#f3c37d" stroke="#4a2a10" stroke-width="3"/>
<rect x="450" y="188" width="190" height="58" fill="#f3c37d" stroke="#4a2a10" stroke-width="3"/>
<rect x="640" y="170" width="270" height="95" fill="#f3c37d" stroke="#4a2a10" stroke-width="3"/>
<rect x="90" y="205" width="820" height="25" fill="#fff8e8" stroke="#4a2a10"/>
<rect x="445" y="181" width="200" height="72" fill="none" stroke="#b8860b" stroke-width="8"/>
<text x="475" y="160" font-size="13">cork/ferrule zone</text>
<line x1="450" y1="282" x2="640" y2="282" stroke="black"/>
<text x="485" y="305" font-size="13">1.25 in min engagement</text>
<text x="90" y="330" font-size="13">Checks: airtight slip fit, bore step less than 0.005 in, joint at least 0.75 in away from any tone hole.</text>
</svg>
"""
    write_text("drawings/two-piece-joint.svg", joint)

    double = svg_header(1100, 520) + """
<rect width="1100" height="520" fill="white" stroke="black"/>
<text x="40" y="45" font-size="24" font-weight="bold">Double Drone Layout</text>
<rect x="90" y="150" width="850" height="70" rx="28" fill="#f3c37d" stroke="#4a2a10" stroke-width="3"/>
<rect x="90" y="275" width="850" height="70" rx="28" fill="#e8b86d" stroke="#4a2a10" stroke-width="3"/>
<text x="110" y="140" font-size="14">melody flute side (Kaval or Alghosazi)</text>
<text x="110" y="265" font-size="14">drone side, independent windway</text>
<rect x="90" y="165" width="70" height="40" fill="#111"/>
<rect x="90" y="290" width="70" height="40" fill="#111"/>
<circle cx="725" cy="310" r="13" fill="#111"/>
<text x="755" y="315" font-size="13">optional rear thumb vent shifts drone up one tone</text>
<line x1="230" y1="220" x2="230" y2="275" stroke="#444" stroke-dasharray="6,6"/>
<line x1="620" y1="220" x2="620" y2="275" stroke="#444" stroke-dasharray="6,6"/>
<text x="260" y="250" font-size="13">temporary bands/collars before permanent joinery</text>
<text x="90" y="410" font-size="13">Tune each tube separately before coupling. If both sides are blown together, record pressure stealing and beating.</text>
</svg>
"""
    write_text("drawings/double-drone-layout.svg", double)

    write_hole_layout_svg("drawings/kaval-hole-layout.svg", [m for m in MEMBERS if m.instrument == "Fipple Kaval"], "Kaval Hole Layout")
    write_hole_layout_svg("drawings/alghosazi-hole-layout.svg", [m for m in MEMBERS if m.instrument == "Fipple Alghosazi"], "Alghosazi Hole Layout")


def write_hole_layout_svg(rel: str, members: list[Member], title: str) -> None:
    width = 1200
    row_h = 78
    height = 110 + row_h * len(members)
    parts = [svg_header(width, height), f'<rect width="{width}" height="{height}" fill="white" stroke="black"/>']
    parts.append(f'<text x="40" y="42" font-size="24" font-weight="bold">{escape(title)}</text>')
    parts.append('<text x="40" y="68" font-size="13">Holes are starter positions. Drill undersized and tune by measured pitch.</text>')
    max_len = max(m.labium_to_foot_in for m in members)
    x0, x1 = 210, 1080
    scale = (x1 - x0) / max_len
    for i, m in enumerate(members):
        y = 110 + i * row_h
        parts.append(f'<text x="40" y="{y+20}" font-size="13" font-weight="bold">{m.member_id}</text>')
        parts.append(f'<text x="40" y="{y+40}" font-size="11">{m.key}, {m.total_length_cm:.0f} cm</text>')
        parts.append(f'<line x1="{x0}" y1="{y+25}" x2="{x0 + m.labium_to_foot_in*scale:.1f}" y2="{y+25}" stroke="#4a2a10" stroke-width="12" stroke-linecap="round"/>')
        parts.append(f'<text x="{x0-12}" y="{y+55}" font-size="10" text-anchor="end">labium</text>')
        parts.append(f'<text x="{x0 + m.labium_to_foot_in*scale + 8:.1f}" y="{y+55}" font-size="10">foot</text>')
        for h in hole_schedule(m):
            cx = x0 + float(h["x_from_labium_in"]) * scale
            cy = y + 25
            fill = "#111" if h["orientation"] == "front" else "#1d4f91"
            parts.append(f'<circle cx="{cx:.1f}" cy="{cy}" r="8" fill="{fill}"/>')
            parts.append(f'<text x="{cx:.1f}" y="{cy-16}" font-size="9" text-anchor="middle">{h["hole_no_from_foot"]}</text>')
        parts.append(f'<text x="{x1-160}" y="{y+58}" font-size="10">blue = back thumb</text>' if i == 0 and title.startswith("Alghosazi") else "")
    parts.append("</svg>")
    write_text(rel, "\n".join(parts))


def write_png(path: Path, width: int, height: int, draw_fn) -> None:
    pixels = bytearray([255, 251, 244] * width * height)

    def set_px(x: int, y: int, rgb: tuple[int, int, int]) -> None:
        if 0 <= x < width and 0 <= y < height:
            off = (y * width + x) * 3
            pixels[off:off+3] = bytes(rgb)

    def rect(x0: int, y0: int, x1: int, y1: int, rgb: tuple[int, int, int]) -> None:
        for y in range(max(0, y0), min(height, y1)):
            for x in range(max(0, x0), min(width, x1)):
                set_px(x, y, rgb)

    def circle(cx: int, cy: int, r: int, rgb: tuple[int, int, int]) -> None:
        rr = r * r
        for y in range(cy - r, cy + r + 1):
            for x in range(cx - r, cx + r + 1):
                if (x - cx) ** 2 + (y - cy) ** 2 <= rr:
                    set_px(x, y, rgb)

    draw_fn(rect, circle, set_px)
    raw = bytearray()
    stride = width * 3
    for y in range(height):
        raw.append(0)
        raw.extend(pixels[y*stride:(y+1)*stride])
    png = b"\x89PNG\r\n\x1a\n"

    def chunk(tag: bytes, data: bytes) -> bytes:
        return struct.pack(">I", len(data)) + tag + data + struct.pack(">I", zlib.crc32(tag + data) & 0xffffffff)

    png += chunk(b"IHDR", struct.pack(">IIBBBBB", width, height, 8, 2, 0, 0, 0))
    png += chunk(b"IDAT", zlib.compress(bytes(raw), 9))
    png += chunk(b"IEND", b"")
    path.write_bytes(png)


def write_images() -> None:
    def draw(rect, circle, set_px):
        # simple warm-wood portfolio placeholder showing two long flutes.
        rect(0, 0, 1200, 675, (250, 243, 232))
        rect(100, 210, 1090, 280, (207, 125, 52))
        rect(100, 385, 1090, 455, (226, 167, 82))
        rect(100, 220, 170, 270, (18, 14, 12))
        rect(100, 395, 170, 445, (18, 14, 12))
        rect(245, 198, 310, 238, (245, 235, 214))
        rect(245, 372, 310, 412, (245, 235, 214))
        for x in [620, 690, 760, 830, 900]:
            circle(x, 245, 13, (12, 10, 8))
        for x in [565, 665, 765, 865, 965]:
            circle(x, 420, 13, (12, 10, 8))
        circle(1010, 390, 13, (34, 80, 145))
        for x in range(100, 1090):
            if x % 21 == 0:
                rect(x, 210, x+2, 455, (154, 86, 40))
    write_png(ROOT / "images/hero.png", 1200, 675, draw)


def main() -> None:
    ensure_dirs()
    write_guided_intake()
    write_data_files()
    write_packet_docs()
    write_xlsx()
    write_custom_drawings()
    write_images()


if __name__ == "__main__":
    main()
