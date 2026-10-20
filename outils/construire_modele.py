"""Construit modele/reference.docx : le modèle Word des préparations de TP.

On part du modèle par défaut de pandoc et on remplace ses styles par ceux
des préparations (titres, questions, lignes, calculs, encadrés de capture…).
À relancer seulement si on veut changer l'apparence des préparations :

    uv run --no-project --with pypandoc_binary python -I outils/construire_modele.py
"""

import pathlib
import re
import subprocess
import sys
import zipfile

import pypandoc

sys.stdout.reconfigure(encoding="utf-8")

RACINE = pathlib.Path(__file__).resolve().parent.parent
SORTIE = RACINE / "modele" / "reference.docx"

BLEU = "1F4E79"
ROUGE = "C00000"
GRIS = "7F7F7F"


def paragraphe(sid, nom, ppr="", rpr="", base="Normal", suivant=None):
    suivant = f'<w:next w:val="{suivant}"/>' if suivant else ""
    return (
        f'<w:style w:type="paragraph" w:customStyle="1" w:styleId="{sid}">'
        f'<w:name w:val="{nom}"/><w:basedOn w:val="{base}"/>{suivant}<w:qFormat/>'
        f"<w:pPr>{ppr}</w:pPr><w:rPr>{rpr}</w:rPr></w:style>"
    )


def encadre(couleur, fond):
    bord = f'w:val="dashed" w:sz="8" w:space="12" w:color="{couleur}"'
    return (
        f"<w:keepLines/><w:pBdr><w:top {bord}/><w:left {bord}/><w:bottom {bord}/><w:right {bord}/></w:pBdr>"
        f'<w:shd w:val="clear" w:color="auto" w:fill="{fond}"/>'
        f'<w:spacing w:before="320" w:after="320"/><w:ind w:left="680" w:right="113"/>'
    )


# Styles de pandoc qu'on redéfinit entièrement.
REMPLACES = {
    "Normal": '<w:style w:type="paragraph" w:default="1" w:styleId="Normal"><w:name w:val="Normal"/><w:qFormat/>'
    '<w:pPr><w:spacing w:before="0" w:after="0" w:line="276" w:lineRule="auto"/></w:pPr>'
    '<w:rPr><w:rFonts w:ascii="Calibri" w:hAnsi="Calibri" w:cs="Calibri"/><w:sz w:val="23"/><w:szCs w:val="23"/></w:rPr></w:style>',
    "BodyText": '<w:style w:type="paragraph" w:styleId="BodyText"><w:name w:val="Body Text"/><w:basedOn w:val="Normal"/>'
    '<w:link w:val="BodyTextChar"/><w:qFormat/><w:pPr><w:spacing w:before="60" w:after="60"/></w:pPr></w:style>',
    "Title": '<w:style w:type="paragraph" w:styleId="Title"><w:name w:val="Title"/><w:basedOn w:val="Normal"/>'
    '<w:next w:val="BodyText"/><w:link w:val="TitleChar"/><w:qFormat/>'
    '<w:pPr><w:spacing w:before="0" w:after="60"/><w:jc w:val="center"/></w:pPr>'
    '<w:rPr><w:b/><w:sz w:val="44"/><w:szCs w:val="44"/></w:rPr></w:style>',
    "Subtitle": '<w:style w:type="paragraph" w:styleId="Subtitle"><w:name w:val="Subtitle"/><w:basedOn w:val="Normal"/>'
    '<w:next w:val="BodyText"/><w:link w:val="SubtitleChar"/><w:qFormat/>'
    '<w:pPr><w:spacing w:before="0" w:after="360"/><w:jc w:val="center"/></w:pPr>'
    '<w:rPr><w:sz w:val="30"/><w:szCs w:val="30"/></w:rPr></w:style>',
    "Heading1": '<w:style w:type="paragraph" w:styleId="Heading1"><w:name w:val="heading 1"/><w:basedOn w:val="Normal"/>'
    '<w:next w:val="BodyText"/><w:link w:val="Heading1Char"/><w:qFormat/>'
    '<w:pPr><w:keepNext/><w:keepLines/><w:spacing w:before="480" w:after="160"/><w:outlineLvl w:val="0"/></w:pPr>'
    f'<w:rPr><w:b/><w:color w:val="{BLEU}"/><w:sz w:val="30"/><w:szCs w:val="30"/></w:rPr></w:style>',
    "Heading2": '<w:style w:type="paragraph" w:styleId="Heading2"><w:name w:val="heading 2"/><w:basedOn w:val="Normal"/>'
    '<w:next w:val="BodyText"/><w:link w:val="Heading2Char"/><w:qFormat/>'
    '<w:pPr><w:keepNext/><w:keepLines/><w:spacing w:before="360" w:after="120"/><w:ind w:left="340"/><w:outlineLvl w:val="1"/></w:pPr>'
    '<w:rPr><w:b/><w:sz w:val="26"/><w:szCs w:val="26"/></w:rPr></w:style>',
    "Heading3": '<w:style w:type="paragraph" w:styleId="Heading3"><w:name w:val="heading 3"/><w:basedOn w:val="Normal"/>'
    '<w:next w:val="BodyText"/><w:link w:val="Heading3Char"/><w:qFormat/>'
    '<w:pPr><w:keepNext/><w:keepLines/><w:spacing w:before="240" w:after="80"/><w:outlineLvl w:val="2"/></w:pPr>'
    '<w:rPr><w:b/><w:sz w:val="23"/><w:szCs w:val="23"/></w:rPr></w:style>',
    "Table": '<w:style w:type="table" w:default="1" w:styleId="Table"><w:name w:val="Table"/><w:basedOn w:val="TableNormal"/><w:qFormat/>'
    '<w:pPr><w:jc w:val="center"/></w:pPr>'
    '<w:tblPr><w:jc w:val="center"/><w:tblBorders>'
    '<w:top w:val="single" w:sz="4" w:color="000000"/><w:left w:val="single" w:sz="4" w:color="000000"/>'
    '<w:bottom w:val="single" w:sz="4" w:color="000000"/><w:right w:val="single" w:sz="4" w:color="000000"/>'
    '<w:insideH w:val="single" w:sz="4" w:color="000000"/><w:insideV w:val="single" w:sz="4" w:color="000000"/>'
    '</w:tblBorders><w:tblCellMar><w:top w:w="60" w:type="dxa"/><w:left w:w="108" w:type="dxa"/>'
    '<w:bottom w:w="60" w:type="dxa"/><w:right w:w="108" w:type="dxa"/></w:tblCellMar></w:tblPr>'
    '<w:tblStylePr w:type="firstRow"><w:rPr><w:b/></w:rPr><w:tcPr><w:shd w:val="clear" w:color="auto" w:fill="F2F2F2"/></w:tcPr></w:tblStylePr>'
    "</w:style>",
}

# Styles propres aux préparations (le nom est celui utilisé par prepa.lua).
AJOUTES = [
    paragraphe("Question", "Question", '<w:keepNext/><w:spacing w:before="280" w:after="60"/>'),
    paragraphe("Ligne", "Ligne", '<w:spacing w:before="50" w:after="50"/><w:ind w:left="680"/>'),
    paragraphe("Calcul", "Calcul", '<w:spacing w:before="40" w:after="40"/><w:ind w:left="1247"/>'),
    paragraphe("Capture", "Capture", encadre(BLEU, "EAF2FB"), f'<w:color w:val="{BLEU}"/>'),
    paragraphe("Schema", "Schema", encadre("C55A11", "FDF0E6"), '<w:color w:val="C55A11"/>'),
    paragraphe("Marge", "Marge", '<w:keepNext/><w:spacing w:before="200" w:after="0"/>',
               f'<w:i/><w:color w:val="{GRIS}"/><w:sz w:val="19"/><w:szCs w:val="19"/>'),
    paragraphe("Piste", "Piste", '<w:spacing w:before="20" w:after="40"/><w:ind w:left="1247"/>',
               f'<w:i/><w:color w:val="{GRIS}"/><w:sz w:val="20"/><w:szCs w:val="20"/>'),
    '<w:style w:type="character" w:customStyle="1" w:styleId="Rouge"><w:name w:val="Rouge"/>'
    f'<w:basedOn w:val="DefaultParagraphFont"/><w:qFormat/><w:rPr><w:color w:val="{ROUGE}"/></w:rPr></w:style>',
]


def main():
    pandoc = pypandoc.get_pandoc_path()
    defaut = subprocess.run([pandoc, "--print-default-data-file", "reference.docx"],
                            capture_output=True, check=True).stdout
    SORTIE.parent.mkdir(exist_ok=True)
    tmp = SORTIE.with_suffix(".tmp")
    tmp.write_bytes(defaut)

    with zipfile.ZipFile(tmp) as src, zipfile.ZipFile(SORTIE, "w", zipfile.ZIP_DEFLATED) as dst:
        for item in src.infolist():
            data = src.read(item.filename)
            if item.filename == "word/styles.xml":
                xml = data.decode("utf8")
                for sid, style in REMPLACES.items():
                    xml, n = re.subn(rf'<w:style [^>]*w:styleId="{sid}".*?</w:style>', style, xml, count=1, flags=re.S)
                    if n == 0:
                        xml = xml.replace("</w:styles>", style + "</w:styles>")
                xml = xml.replace("</w:styles>", "".join(AJOUTES) + "</w:styles>")
                xml = xml.replace('w:val="en-US"', 'w:val="fr-FR"')
                data = xml.encode("utf8")
            dst.writestr(item, data)
    tmp.unlink()
    print(f"Modèle écrit : {SORTIE}")


if __name__ == "__main__":
    main()
