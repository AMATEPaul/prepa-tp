"""Aperçu d'une préparation Word, page par page, en images PNG (Windows + Word).

    uv run --no-project --with pymupdf python -I <skill>/outils/apercu.py prepa.docx <dossier>

Word exporte le document en PDF, puis chaque page est enregistrée en PNG
dans <dossier> pour pouvoir la regarder avec Read.
"""

import pathlib
import subprocess
import sys

import fitz

sys.stdout.reconfigure(encoding="utf-8")

EXPORT = r"""
$w = New-Object -ComObject Word.Application
$w.Visible = $false
try {{
  $d = $w.Documents.Open("{docx}", $false, $true)
  $d.ExportAsFixedFormat("{pdf}", 17)
  $d.Close($false)
}} finally {{ $w.Quit() }}
"""


def main():
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    docx = pathlib.Path(sys.argv[1]).resolve()
    dossier = pathlib.Path(sys.argv[2]).resolve()
    dossier.mkdir(parents=True, exist_ok=True)
    pdf = dossier / (docx.stem + ".pdf")

    subprocess.run(["powershell", "-NoProfile", "-Command", EXPORT.format(docx=docx, pdf=pdf)], check=True)
    doc = fitz.open(pdf)
    for i, page in enumerate(doc, 1):
        page.get_pixmap(dpi=110).save(dossier / f"page_{i:02d}.png")
    print(f"{len(doc)} pages dans {dossier}")


if __name__ == "__main__":
    main()
