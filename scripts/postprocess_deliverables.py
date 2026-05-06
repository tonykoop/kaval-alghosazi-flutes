#!/usr/bin/env python3
"""Create local binary handoff artifacts that do not need external Python libs."""

from __future__ import annotations

import json
import re
import textwrap
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def pdf_escape(text: str) -> str:
    return text.replace("\\", "\\\\").replace("(", "\\(").replace(")", "\\)")


def clean_markdown_line(line: str) -> str:
    line = re.sub(r"!\[[^\]]*\]\([^)]+\)", "[image]", line)
    line = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r"\1 (\2)", line)
    line = line.replace("`", "")
    line = line.replace("|", " | ")
    return line.strip()


def make_pdf_from_markdown(src: Path, dst: Path) -> None:
    raw_lines = src.read_text(encoding="utf-8", errors="replace").splitlines()
    logical: list[str] = []
    for line in raw_lines:
        stripped = clean_markdown_line(line)
        if not stripped:
            logical.append("")
            continue
        if stripped.startswith("#"):
            stripped = stripped.lstrip("# ").upper()
        for wrapped in textwrap.wrap(stripped, width=94, replace_whitespace=False) or [""]:
            logical.append(wrapped)

    pages: list[list[str]] = []
    page: list[str] = []
    for line in logical:
        page.append(line)
        if len(page) >= 58:
            pages.append(page)
            page = []
    if page:
        pages.append(page)

    objects: list[bytes] = []

    def add(obj: str | bytes) -> int:
        objects.append(obj.encode("latin-1") if isinstance(obj, str) else obj)
        return len(objects)

    # Reserve object numbers.
    catalog_id = add("")
    pages_id = add("")
    font_id = add("<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>")
    page_ids: list[int] = []
    content_ids: list[int] = []

    for lines in pages:
        content = ["BT", "/F1 10 Tf", "50 760 Td", "12 TL"]
        for line in lines:
            content.append(f"({pdf_escape(line[:120])}) Tj")
            content.append("T*")
        content.append("ET")
        stream = "\n".join(content).encode("latin-1", errors="replace")
        content_id = add(b"<< /Length " + str(len(stream)).encode("ascii") + b" >>\nstream\n" + stream + b"\nendstream")
        page_id = add("")
        content_ids.append(content_id)
        page_ids.append(page_id)

    objects[catalog_id - 1] = f"<< /Type /Catalog /Pages {pages_id} 0 R >>".encode("latin-1")
    kids = " ".join(f"{pid} 0 R" for pid in page_ids)
    objects[pages_id - 1] = f"<< /Type /Pages /Kids [{kids}] /Count {len(page_ids)} >>".encode("latin-1")

    for idx, page_id in enumerate(page_ids):
        content_id = content_ids[idx]
        page_obj = (
            f"<< /Type /Page /Parent {pages_id} 0 R /MediaBox [0 0 612 792] "
            f"/Resources << /Font << /F1 {font_id} 0 R >> >> "
            f"/Contents {content_id} 0 R >>"
        )
        objects[page_id - 1] = page_obj.encode("latin-1")

    out = bytearray(b"%PDF-1.4\n%\xe2\xe3\xcf\xd3\n")
    offsets = [0]
    for i, obj in enumerate(objects, start=1):
        offsets.append(len(out))
        out.extend(f"{i} 0 obj\n".encode("ascii"))
        out.extend(obj)
        out.extend(b"\nendobj\n")
    xref_start = len(out)
    out.extend(f"xref\n0 {len(objects)+1}\n".encode("ascii"))
    out.extend(b"0000000000 65535 f \n")
    for off in offsets[1:]:
        out.extend(f"{off:010d} 00000 n \n".encode("ascii"))
    out.extend(
        f"trailer\n<< /Size {len(objects)+1} /Root {catalog_id} 0 R >>\n"
        f"startxref\n{xref_start}\n%%EOF\n".encode("ascii")
    )
    dst.write_bytes(out)


def update_manifest() -> None:
    manifest_path = ROOT / "capstone-manifest.json"
    if not manifest_path.exists():
        return
    data = json.loads(manifest_path.read_text(encoding="utf-8"))
    outputs = data.setdefault("outputs", {})
    pptx = ROOT / "capstone-deck.pptx"
    pdf = ROOT / "print-packet.pdf"
    docx = ROOT / "print-packet.docx"
    bom_docx = ROOT / "Kaval-Alghosazi-BOM-Build-Method.docx"
    if pptx.exists():
        outputs["capstone_deck_pptx"] = str(pptx)
    if pdf.exists():
        outputs["print_packet_pdf"] = str(pdf)
    if docx.exists():
        outputs["print_packet_docx"] = str(docx)
    if bom_docx.exists():
        outputs["bom_build_method_docx"] = str(bom_docx)
    notes = [n for n in data.get("notes", []) if "PDF is created when" not in n and "PPTX is created when" not in n]
    notes.append("PPTX/DOCX were produced with pandoc; PDF was produced with the local simple PDF writer.")
    data["notes"] = notes
    manifest_path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")


def main() -> None:
    make_pdf_from_markdown(ROOT / "print-packet.md", ROOT / "print-packet.pdf")
    update_manifest()


if __name__ == "__main__":
    main()
