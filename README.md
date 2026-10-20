# prepa-tp

Un skill [Claude Code](https://code.claude.com/docs/en/skills) qui prépare un TP d'IUT avant la séance, dans le style de mes comptes rendus, quelle que soit la matière.

## Ce qu'il fait

À partir du sujet du TP (et du TD associé s'il est là), il écrit la préparation que j'aurais faite à la main :

- **même numérotation que le sujet** (Partie 1, a), 1-, 2-…) et consignes reformulées en style télégraphique ;
- pour chaque grandeur : `• X = ? = définition`, puis la démarche (loi de cours en rouge ⇒ transformations ⇒ expression ⇒ remplacement) ;
- **les valeurs données par le sujet sont écrites, celles qu'on mesure en TP restent en `…`** ;
- **tableaux de mesures vides**, avec les unités et les formules des colonnes calculées ;
- un **encadré numéroté pour chaque capture d'écran** à faire (oscilloscope ou autre appareil) : quoi afficher, quoi noter ;
- un encadré pour chaque schéma à faire, et `Commentaire Résultat obtenu : -> ……` à remplir en séance.

Le résultat est un **document Word** (`.docx`) avec de vraies équations, à compléter pendant le TP.

Exemple : [`exemples/prepa-ENER3-alim-decoupage.docx`](exemples/prepa-ENER3-alim-decoupage.docx) (source : [`.md`](exemples/prepa-ENER3-alim-decoupage.md)).

## Installation

```bash
git clone https://github.com/AMATEPaul/prepa-tp.git ~/.claude/skills/prepa-tp
```

Puis, dans Claude Code, `/reload-skills` (ou redémarrer la session).

## Utilisation

Mettre le sujet du TP (et le TD, les datasheets…) dans un dossier, ouvrir Claude Code dedans et lancer `/prepa-tp`.

## Prérequis

- [`uv`](https://docs.astral.sh/uv/) : il télécharge pandoc tout seul pour la conversion en Word (sinon, `pandoc` installé).
- **Optionnel** : Microsoft Word, pour que Claude vérifie le rendu page par page.

## Contenu

| Fichier | Rôle |
|---|---|
| `SKILL.md` | La méthode que suit Claude |
| `references/style.md` | Ma façon d'écrire un compte rendu, règle par règle |
| `exemples/` | Une préparation complète (TP ENER3, alim à découpage isolée) |
| `modele/reference.docx` | Le modèle Word (styles, encadrés, couleurs) |
| `outils/vers_docx.py` | Markdown → Word |
| `outils/prepa.lua` | Filtre pandoc : raccourcis `::: q`, `::: c`, `::: capture`… |
| `outils/apercu.py` | Aperçu des pages du `.docx` en images (Windows + Word) |
| `outils/construire_modele.py` | Reconstruit `modele/reference.docx` |
