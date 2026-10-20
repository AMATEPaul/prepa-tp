---
title: TP partiel
subtitle: – Alim à découpage isolé –
---

# Partie 1 : étude Alim isolé à découpage simplifié

::: marge
$f = f_{commutateur}$
:::

::: q
1- Visualiser impulsion du générateur et régler $f = 5$ kHz, largeur d'impulsion $100$ µs, rapport cyclique 50 %
:::

::: capture
📷 Capture n°1 – impulsions du générateur ($f = 5$ kHz, largeur 100 µs, α = 50 %)
Noter : calibres (V/div et s/div), voie utilisée
:::

## a) Transfo à vide, secondaire non relié à la charge

::: q
2- câblage sans charge
:::

::: piste
alim de puissance réglée à 5 V, faire vérifier le câblage avant la mise sous tension
:::

::: q
3- • visualisation de : $v_2(t)$, $i_1(t)$ grâce au shunt de 1 Ω
:::

::: l
↳ et pince crochet pour visualiser $i_1(t)$
• relever : $v_2(t)$, et $i_1(t)$
:::

::: capture
📷 Capture n°2 – $v_2(t)$ et $i_1(t)$, transfo à vide
Noter : calibres (V/div et s/div), $V_1$ sur le palier négatif (démagnétisation)
:::

::: l
• $V_Z = \ ?$ = Tension aux bornes de la diode zener
:::

::: schema
✏️ Schéma – maille $M_2$ : primaire ($V_1$) + D1 ($V_D$) + DZ ($V_Z$) + shunt ($V_R$) (voir schéma du montage en annexe du sujet)
:::

::: c
$M_2 = V_1 + V_D + V_Z + V_R = 0 \qquad \text{↳ } V_R \text{ négligeable}$
$\Rightarrow V_Z = -V_1 - V_D$
$V_Z = -(\ldots) - 0{,}7$
$V_Z = \ldots\ \text{V}$
:::

::: piste
$V_1$ lu sur le palier négatif de la capture n°2 (m = 1 donc $v_2 = v_1$)
:::

::: q
4- • $L_m = \ ?$ = Valeur inductance
:::

::: c
[$V_L = L\dfrac{di}{dt}$]{.rouge} $\Rightarrow V_L = L\dfrac{\Delta i}{\Delta t} \Rightarrow L = V_L\dfrac{\Delta t}{\Delta i}$
$V_L = V_1 = E = \text{tension d'entrée} = 5\ \text{V}$
$L_m = V_1\dfrac{\Delta t}{\Delta i_1}$
$L_m = 5 \times \dfrac{\ldots}{\ldots}$
$L_m = \ldots\ \text{H} = \ldots\ \text{mH}$
:::

::: piste
$\Delta t$ et $\Delta i_1$ lus sur la rampe de $i_1(t)$ pendant l'impulsion (capture n°2)
:::

::: l
• Transfo IT 237 comparaison
$L_p = L_m = 25$ mH $\approx \ldots$ mH
(Doc technique)
:::

::: q
5- Observation lors de ↗ durée de l'impulsion
:::

::: piste
$f = 2$ kHz, durée d'impulsion ↗ en partant de 0, vérifier que la démagnétisation reste complète
:::

::: l
-> un seuil/saturation apparaît de $i_1(t)$
-> Aire maxi (sans saturation) de l'impulsion
:::

::: capture
📷 Capture n°3 – $i_1(t)$ au début de la saturation ($f = 2$ kHz)
Noter : $\Delta t$ de l'impulsion juste avant la saturation, $E = V = 5$ V
:::

::: c
$Aire = \text{tension} \times \text{durée d'impulsion (µs)}$
$= V \times \Delta t\ \text{(µs)}$
$= 5 \times \ldots$
$= \ldots\ \text{V·µs}$
:::

::: piste
à comparer avec $(V_1 \cdot t)_{max} = 1100$ V·µs (doc IT 237)
:::

## b) Transfo en charge, secondaire relié à la charge

::: marge
$f = f_{commutateur}$
:::

::: q
6- • câblage avec $D_2$, charge
:::

::: l
• visualiser $v_s(t)$ pour $f = 2$ kHz et $\alpha = 30$ %
:::

::: capture
📷 Capture n°4 – $v_s(t)$ avec $D_2$ et charge, sans condensateur ($f = 2$ kHz, α = 30 %)
Noter : calibres (V/div et s/div)
:::

::: l
Commentaire Résultat obtenu :
-> ……………………………………………
:::

::: piste
regarder ce que devient la partie négative de $v_s(t)$ avec la diode
:::

::: l
• câblage avec $D_2$, charge, et condensateur
:::

::: capture
📷 Capture n°5 – courant du primaire $i_1(t)$ et $v_s(t)$, avec condensateur
Noter : calibres (V/div et s/div), ondulation $\Delta V$ de $v_s$
:::

::: l
Commentaire Résultat obtenu :
-> ……………………………………………
-> ……………………………………………
:::

::: piste
regarder les tensions négatives (diode) et le lissage / taux d'ondulation de $v_s$ (condensateur)
:::

::: l
• pour diminuer $\Delta V$ on doit jouer sur ……………
:::

::: capture
📷 Capture n°6 – $v_s(t)$ pour une autre fréquence ou un autre rapport cyclique (en partant de $f = 1$ kHz)
Noter : $f$, α et $\Delta V$
:::

# Partie 2 : Platine Hacheur isolé

::: q
1- Principales caractéristiques datasheet MAX17691B
:::

::: l
• Plage de tension d'entrée -> …… V – …… V
Tension et courant de sortie -> …… V et …… A DC
fréquence de découpage -> …… kHz
rendement du courant nominal -> …… %
:::

::: l
• isolation galvanique = [isolation qui consiste à faire la liaison entre les différentes parties du montage par magnétisme au lieu de liaison physique de l'alimentation]{.rouge}
:::

::: q
2- • Proposition schéma de câblage pour mesurer le η global
:::

::: schema
✏️ Schéma – $E = 30$ V → (A) en série et (V) en parallèle → [DC / DC] → (V) en parallèle et (A) en série ($i_{sortie}$) → Rhéostat
↳ Rhéostat = résistance variable
:::

::: l
• En faisant varier le Rhéostat ça varie uniquement $i(t)_{sortie}$
:::

::: piste
rhéostat au max au départ, puis $i_{sortie}$ de sa valeur mini à 0,5 A : 5 points de mesure
:::

| R (Ω) | i sortie (A) | V sortie (V) | P sortie (W) | i entrée (A) | V entrée (V) | P entrée (W) | η (%) |
|:-----:|:------------:|:------------:|:------------:|:------------:|:------------:|:------------:|:-----:|
|       |              |              |              |              |              |              |       |
|       |              |              |              |              |              |              |       |
|       |              |              |              |              |              |              |       |
|       |              |              |              |              |              |              |       |
|       |              |              |              |              |              |              |       |

::: c
[$\text{↳ } P = V \times I$]{.rouge} [$\qquad \text{↳ } \eta = \dfrac{P_{sortie}}{P_{entrée}}$]{.rouge}
$\eta_{moyen} = \dfrac{\sum \eta}{nb\ \eta} = \dfrac{\ldots + \ldots + \ldots + \ldots + \ldots}{5} = \ldots\ \%$
:::

::: q
3- • $\eta = \ ?$ -> si on remplace ce convertisseur par une Alim linéaire
:::

::: c
$\eta_{linéaire} = \dfrac{P_{sortie}}{P_{entrée}} = \dfrac{U_{sortie} \times I_{sortie}}{U_{entrée} \times I_{entrée}} \qquad \text{Or } I_{sortie} = I_{entrée}$
$\text{donc } \eta_{linéaire} = \dfrac{U_{sortie}}{U_{entrée}} = \dfrac{5}{30} = 0{,}1667$
$\eta_{linéaire} = 16{,}67\ \%$
:::

::: l
• Conclusion :
Le $\eta$ alim linéaire (16,67 %) est …………… face à $\eta$ alim découpage (…… %)
:::

::: q
4-
:::

::: q
5- • visualisation de : $V_1(t)$, $V_2(t)$
:::

::: l
réglage $i = 0{,}5$ A
:::

::: piste
attention aux masses : PGND côté primaire, GND0 côté secondaire
:::

::: capture
📷 Capture n°7 – oscillogramme $V_1(t)$ et $V_2(t)$, $i = 0{,}5$ A
Noter : calibres (V/div de chaque voie et s/div), $V_1$, $V_2$, période $T$
:::

::: l
• $m = \dfrac{n_2}{n_1} = \ ?$ = rapport de transformation
:::

::: c
$m = \dfrac{V_2}{V_1} = \dfrac{\ldots}{\ldots} \approx \ldots$
:::

::: l
• $f_{découpage} = \ ?$
:::

::: c
[$f = \dfrac{1}{T}$]{.rouge}
$f_{découpage} = \dfrac{1}{\ldots} = \ldots\ \text{kHz}$
:::

::: piste
$T$ lu sur la capture n°7, à comparer avec la fréquence de découpage de la datasheet (1-)
:::
