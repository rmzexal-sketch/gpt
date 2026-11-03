#!/usr/bin/env python3
"""Extract DOIs from PDFs in a selected folder and save to Excel.

Usage:
  python extract_pdf_doi_gui.py

Dependencies:
  - pypdf (preferred) or PyPDF2
  - pandas
  - openpyxl (for Excel output)
"""

from __future__ import annotations

import re
import sys
from dataclasses import dataclass
from pathlib import Path
from tkinter import Tk
from tkinter import filedialog, messagebox

import pandas as pd

try:
    from pypdf import PdfReader  # type: ignore
except ImportError:  # pragma: no cover - fallback for environments without pypdf
    try:
        from PyPDF2 import PdfReader  # type: ignore
    except ImportError as exc:  # pragma: no cover
        raise SystemExit(
            "Missing dependency: install 'pypdf' (or 'PyPDF2') to read PDFs."
        ) from exc


DOI_REGEX = re.compile(
    r"10\.\d{4,9}/[-._;()/:A-Z0-9]+", re.IGNORECASE
)


@dataclass
class PdfDoiResult:
    filename: str
    doi: str | None


def extract_text_from_pdf(pdf_path: Path) -> str:
    reader = PdfReader(str(pdf_path))
    text_parts: list[str] = []
    for page in reader.pages:
        page_text = page.extract_text() or ""
        text_parts.append(page_text)
    return "\n".join(text_parts)


def find_doi(text: str) -> str | None:
    match = DOI_REGEX.search(text)
    if not match:
        return None
    doi = match.group(0).strip()
    doi = doi.rstrip(".,;:)")
    if doi.lower().endswith("doi"):
        doi = doi[:-3].rstrip(".,;:)")
    return doi or None


def extract_dois_from_folder(folder: Path) -> list[PdfDoiResult]:
    results: list[PdfDoiResult] = []
    for pdf_path in sorted(folder.glob("*.pdf")):
        try:
            text = extract_text_from_pdf(pdf_path)
            doi = find_doi(text)
            results.append(PdfDoiResult(filename=pdf_path.name, doi=doi))
        except Exception as exc:  # pragma: no cover - log and continue
            results.append(PdfDoiResult(filename=pdf_path.name, doi=f"ERROR: {exc}"))
    return results


def select_folder() -> Path | None:
    root = Tk()
    root.withdraw()
    folder_selected = filedialog.askdirectory(title="Select folder containing PDFs")
    root.destroy()
    if not folder_selected:
        return None
    return Path(folder_selected)


def save_results_to_excel(results: list[PdfDoiResult], output_path: Path) -> None:
    df = pd.DataFrame(
        [{"filename": r.filename, "doi": r.doi} for r in results]
    )
    df.to_excel(output_path, index=False)


def main() -> int:
    folder = select_folder()
    if folder is None:
        messagebox.showinfo("Cancelled", "No folder selected. Exiting.")
        return 0

    if not folder.exists():
        messagebox.showerror("Error", "Selected folder does not exist.")
        return 1

    results = extract_dois_from_folder(folder)

    default_output = folder / "pdf_doi_results.xlsx"
    root = Tk()
    root.withdraw()
    output_file = filedialog.asksaveasfilename(
        title="Save Excel file",
        defaultextension=".xlsx",
        filetypes=[("Excel files", "*.xlsx")],
        initialfile=default_output.name,
        initialdir=str(folder),
    )
    root.destroy()

    if not output_file:
        messagebox.showinfo("Cancelled", "No output file selected. Exiting.")
        return 0

    save_results_to_excel(results, Path(output_file))
    messagebox.showinfo(
        "Done", f"Saved DOI results for {len(results)} PDFs to {output_file}."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
