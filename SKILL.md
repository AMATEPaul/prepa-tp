---
name: prepa-tp
description: Préparer un TP d'IUT avant la séance, dans le style exact des comptes rendus de l'utilisateur (n'importe quelle matière) — questions numérotées comme le sujet, reformulation télégraphique, « X = ? = définition », formules et démarche de calcul sans les valeurs mesurées, tableaux de mesures vides, emplacements marqués pour les captures d'oscilloscope et autres appareils. Produit un document Word (.docx) à compléter pendant le TP. À utiliser quand l'utilisateur veut préparer un TP à partir de son sujet (et du TD associé).
metadata:
  categorie: iut/preparation
  resume: Préparer un TP - formules sans valeurs, tableaux vides, emplacements des captures, en Word.
---

# Préparer un TP (IUT)

Ce skill fait **la préparation** d'un TP à la place de l'utilisateur : le document qu'il aurait écrit avant la séance, avec sa numérotation, sa façon d'écrire et ses formules, mais **sans les valeurs mesurées**, puisqu'on les trouve pendant le TP. Il le complète ensuite en séance (valeurs, captures, commentaires).

Le résultat est un **document Word** : les formules sont de vraies équations modifiables, et chaque capture d'écran à faire a son encadré.

Avant d'écrire quoi que ce soit, lire :
- `references/style.md` : sa façon d'écrire, règle par règle ;
- `exemples/prepa-ENER3-alim-decoupage.md` : une préparation complète, à imiter.

(Chemins relatifs au dossier du skill, `~/.claude/skills/prepa-tp/`.)

---

## 0. Démarrage

Chercher dans le dossier courant (et ses sous-dossiers) :

| Document | Rôle |
|---|---|
| **Sujet du TP** (PDF, images) | Les questions, leur numérotation, les réglages, les annexes (schéma du montage, doc constructeur) |
| **TD associé** | Les formules et notations du cours, les valeurs théoriques |
| **Datasheets / docs constructeur** | Valeurs à reporter ou à comparer |
| **Anciens comptes rendus** de l'utilisateur (photos) | Exemples de style en plus de celui du skill |

- S'il n'y a pas de sujet de TP : demander où il est. Ne rien inventer.
- Si le fascicule contient plusieurs TP ou séances : demander lequel préparer (`AskUserQuestion`).
- Ne pas poser d'autre question quand la réponse est dans les documents.

## 1. Lire les documents

- **PDF** : `Read` avec `pages` (20 pages max par appel). Si le rendu des pages n'est pas disponible :
  - texte : `pdftotext -layout sujet.pdf -` ;
  - figures (schémas, annexes, courbes) : rendre les pages en PNG puis les regarder avec `Read` :
    ```bash
    uv run --no-project --with pymupdf python -I -c "import fitz,sys; d=fitz.open(sys.argv[1]); [p.get_pixmap(dpi=110).save(f'{sys.argv[2]}/page_{i+1:02d}.png') for i,p in enumerate(d)]" sujet.pdf <dossier-temporaire>
    ```
- **Photos** (sujet ou compte rendu manuscrit) : `Read` directement ; si l'écriture est petite, recadrer avec `ffmpeg -i photo.jpg -vf "crop=L:H:X:Y" morceau.jpg`.
- Lire **tout** le TP, annexes comprises, et la partie du TD qui lui correspond (formules, notations, valeurs numériques données).

## 2. Ce que contient la préparation

Pour **chaque question du sujet**, dans l'ordre et avec sa numérotation :

1. **La consigne reformulée** en style télégraphique (jamais recopiée), réglages compris.
2. **Chaque grandeur demandée** : `• X = ? = définition`, puis la démarche complète (loi de cours en rouge ⇒ transformations ⇒ identification ⇒ expression appliquée ⇒ remplacement ⇒ résultat avec unité). Voir `references/style.md` § 4.
3. **Les valeurs** :
   - données par le sujet, le TD ou une doc fournie (tension d'alim, seuil de diode, valeur constructeur…) → **écrites** ;
   - calculables uniquement à partir de ces données (rendement théorique, valeur attendue…) → **calculées jusqu'au bout** ;
   - mesurées pendant le TP → **`\ldots`**, jamais inventées, même si le TD donne un ordre de grandeur ;
   - à lire dans une datasheet qui n'est pas dans le dossier → `……`, et le signaler à la fin.
4. **Les captures** : chaque « visualiser », « relever », « observer » sur un oscilloscope ou tout autre appareil ou logiciel à écran (analyseur, simulation, IDE…) a son encadré `::: capture`, numéroté, qui dit quoi afficher, dans quelles conditions et quoi noter (calibres V/div et s/div, grandeurs à lire). Les calculs qui utilisent la capture y renvoient (« lu sur la capture n°2 »).
5. **Les schémas** à faire (câblage proposé, maille, montage) : encadré `::: schema` qui décrit le circuit en une ou deux lignes (ordre des éléments, appareils en série / en parallèle, sens des tensions et courants).
6. **Les séries de mesures** : tableau vide, colonnes avec unités, autant de lignes que de points demandés, formules des colonnes calculées en rouge sous le tableau.
7. **Les commentaires et conclusions** : « Commentaire Résultat obtenu : » + lignes `-> ……` à remplir. Le résultat n'est jamais écrit à sa place. Une piste grise peut dire quoi regarder.
8. **Les pistes** (`::: piste`, en gris) : seulement ce qui sert pendant la séance (réglage à faire avant de mesurer, sécurité / faire vérifier le câblage, où lire une grandeur, à quoi comparer). Une ligne, une par question au plus.

Une question sans rien à préparer garde son numéro seul (« 4- »).

## 3. Écrire le Markdown

Fichier `prepa-<matiere>-<sujet-court>.md` dans le dossier courant (ex. `prepa-ENER3-alim-decoupage.md`).

```markdown
---
title: TP <nom ou numéro>
subtitle: – <sujet du TP> –
---

# Partie 1 : <titre court>

::: marge
$f = f_{commutateur}$
:::

::: q
1- <consigne reformulée>
:::

## a) <sous-partie>

::: l
• $V_Z = \ ?$ = Tension aux bornes de la diode zener
:::

::: c
[$V_L = L\dfrac{di}{dt}$]{.rouge} $\Rightarrow V_L = L\dfrac{\Delta i}{\Delta t}$
$L_m = 5 \times \dfrac{\ldots}{\ldots}$
$L_m = \ldots\ \text{mH}$
:::

::: capture
📷 Capture n°1 – <signaux> (<conditions>)
Noter : calibres (V/div et s/div), <grandeurs à lire>
:::

::: schema
✏️ Schéma – <description du circuit>
:::

::: piste
<rappel utile en séance>
:::
```

| Bloc | Rendu Word |
|---|---|
| `# …` / `## …` | « Partie N : … » / « a) … » |
| `::: q` | ligne de question (« 1- … ») |
| `::: l` | ligne sous la question (retrait 1) : `•`, `->`, `↳` |
| `::: c` | ligne de calcul (retrait 2) |
| `::: capture` | encadré bleu pointillé où coller la capture |
| `::: schema` | encadré orange pointillé pour le schéma |
| `::: marge` | note de marge en petit gris |
| `::: piste` | piste en gris italique |
| `[…]{.rouge}` | formule de cours ou définition en rouge |

Règles de saisie :
- Dans un bloc, **une ligne du Markdown = un paragraphe** : pas de ligne vide entre deux lignes de calcul.
- Les lignes `::: c` sont **entièrement en maths** (un ou plusieurs `$…$` séparés d'espaces) : le texte va dans `\text{…}`, l'unité aussi (`\ldots\ \text{V}`). Sinon Word rapetisse les fractions.
- Virgule décimale : `0{,}7`. Fractions : `\dfrac{}{}`. Valeur à mesurer : `\ldots`. Implication : `\Rightarrow`. Espace large : `\qquad`.
- Hors calculs, les `$…$` restent courts (grandeur, petite égalité).

## 4. Convertir en Word

```bash
uv run --no-project --with pypandoc_binary python -I ~/.claude/skills/prepa-tp/outils/vers_docx.py prepa-<...>.md
```

- Le `.docx` est écrit à côté du `.md`.
- « … est ouvert dans Word » : demander à l'utilisateur de le fermer, puis relancer.
- Sans `uv` mais avec `pandoc` installé : `python ~/.claude/skills/prepa-tp/outils/vers_docx.py prepa-<...>.md`.

## 5. Vérifier le rendu (Windows avec Word)

```bash
uv run --no-project --with pymupdf python -I ~/.claude/skills/prepa-tp/outils/apercu.py prepa-<...>.docx <dossier-temporaire>
```

Regarder chaque page avec `Read` et vérifier :
- les calculs sont alignés à gauche, aucun n'est centré, les fractions sont en taille normale ;
- les formules de cours sont en rouge, les encadrés de capture et de schéma sont visibles ;
- chaque question du sujet est présente, avec son numéro ;
- aucune valeur mesurée n'a été écrite.

Corriger le `.md` et reconvertir si besoin. Si Word n'est pas installé, passer cette étape.

## 6. Rendre

Message court :
- le chemin du `.docx` (et du `.md`) ;
- la liste des captures à faire pendant le TP (n°, quoi) ;
- ce qui manque, par exemple une datasheet absente du dossier.
