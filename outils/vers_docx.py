"""Convertit une préparation de TP (Markdown) en document Word.

    uv run --no-project --with pypandoc_binary python -I <skill>/outils/vers_docx.py prepa.md [prepa.docx]

Les formules $...$ deviennent de vraies équations Word (modifiables).
"""

import pathlib
import re
import shutil
import subprocess
import sys
import zipfile

sys.stdout.reconfigure(encoding="utf-8")

SKILL = pathlib.Path(__file__).resolve().parent.parent


def trouver_pandoc():
    if shutil.which("pandoc"):
        return "pandoc"
    try:
        import pypandoc
    except ImportError:
        sys.exit("pandoc introuvable : lancer ce script avec `uv run --no-project --with pypandoc_binary python -I ...`")
    return pypandoc.get_pandoc_path()


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    source = pathlib.Path(sys.argv[1]).resolve()
    sortie = pathlib.Path(sys.argv[2]).resolve() if len(sys.argv) > 2 else source.with_suffix(".docx")
    if sortie.exists():
        try:
            sortie.open("r+b").close()
        except PermissionError:
            sys.exit(f"{sortie.name} est ouvert dans Word : le fermer puis relancer.")

    subprocess.run(
        [
            trouver_pandoc(), str(source),
            "-f", "markdown",
            "-o", str(sortie),
            "--reference-doc", str(SKILL / "modele" / "reference.docx"),
            "--lua-filter", str(SKILL / "outils" / "prepa.lua"),
            "--resource-path", str(source.parent),
        ],
        check=True,
    )
    retoucher(sortie)
    print(f"Préparation écrite : {sortie}")


ROUGE = '<w:rPr><w:color w:val="C00000"/></w:rPr>'
ESPACE = '<m:r><m:rPr><m:nor/></m:rPr><m:t xml:space="preserve">    </m:t></m:r>'
# Espaces (texte vide) entre deux équations d'une même ligne.
ENTRE_EQUATIONS = re.compile(
    r'</m:oMath>(?:<w:r>(?:<w:rPr>(?:(?!</w:rPr>).)*</w:rPr>)?<w:t xml:space="preserve">\s*</w:t></w:r>)*<m:oMath>',
    re.S,
)
# Réglages des équations : alignées à gauche, fractions en taille normale.
MATH_PR = (
    '<m:mathPr><m:mathFont m:val="Cambria Math"/><m:smallFrac m:val="0"/><m:dispDef/>'
    '<m:lMargin m:val="0"/><m:rMargin m:val="0"/><m:defJc m:val="left"/>'
    '<m:intLim m:val="subSup"/><m:naryLim m:val="undOvr"/></m:mathPr>'
)


def colorer(m):
    """Met en rouge une équation repérée par prepa.lua."""
    return re.sub(r"(<m:r>(?:<m:rPr>(?:(?!</m:rPr>).)*</m:rPr>)?)", r"\1" + ROUGE, m.group(1), flags=re.S)


def ligne_de_calcul(m):
    """Une ligne faite seulement d'équations devient une seule équation
    alignée à gauche, pour garder les fractions en grand."""
    corps = ENTRE_EQUATIONS.sub(ESPACE, m.group(2))
    ppr = re.match(r"\s*(<w:pPr>.*?</w:pPr>)?(.*)", corps, re.S)
    reste = ppr.group(2)
    if reste.count("<m:oMath>") == 1 and re.fullmatch(r"\s*<m:oMath>.*</m:oMath>\s*", reste, re.S):
        reste = f'<m:oMathPara><m:oMathParaPr><m:jc m:val="left"/></m:oMathParaPr>{reste.strip()}</m:oMathPara>'
    return f"{m.group(1)}{ppr.group(1) or ''}{reste}</w:p>"


def retoucher(docx):
    tmp = docx.with_suffix(".tmp")
    with zipfile.ZipFile(docx) as src, zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as dst:
        for item in src.infolist():
            data = src.read(item.filename)
            if item.filename == "word/document.xml":
                xml = data.decode("utf8")
                xml = re.sub(r"<!--rouge-debut-->(.*?)<!--rouge-fin-->", colorer, xml, flags=re.S)
                xml = re.sub(r"(<w:p>)(.*?)</w:p>", ligne_de_calcul, xml, flags=re.S)
                data = xml.encode("utf8")
            elif item.filename == "word/settings.xml":
                xml = data.decode("utf8")
                if "<m:mathPr>" not in xml:
                    xml = xml.replace("<w:themeFontLang", MATH_PR + "<w:themeFontLang", 1)
                xml = xml.replace('<w:decimalSymbol w:val="." />', '<w:decimalSymbol w:val="," />')
                xml = xml.replace('<w:listSeparator w:val="," />', '<w:listSeparator w:val=";" />')
                data = xml.encode("utf8")
            dst.writestr(item, data)
    tmp.replace(docx)


if __name__ == "__main__":
    main()
