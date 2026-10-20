# Le style des comptes rendus de l'utilisateur

Tiré de son compte rendu manuscrit du TP « Alim à découpage isolé » (ENER3). Il écrit **tous** ses TP de la même façon, quelle que soit la matière. La préparation doit ressembler à ce compte rendu avant qu'il soit rempli.

Exemple complet : `exemples/prepa-ENER3-alim-decoupage.md` (et son `.docx`).

---

## 1. Structure et numérotation

```
TP partiel                                  ← titre (pandoc : title)
– Alim à découpage isolé –                  ← sujet du TP entre tirets (pandoc : subtitle)

Partie 1 : étude Alim isolé à découpage simplifié      ← # Partie N : titre court
    a) Transfo à vide, secondaire non relié à la charge  ← ## a) …
1- …                                        ← question, numérotée comme le sujet
    • …                                     ← lignes sous la question
        calculs                             ← retrait de calcul
```

- **Même numérotation que le sujet** : « Partie 1 », « a) », « 1- », « 2- »… (chiffre + tiret, sans point). Si le sujet numérote « I – », « II – », garder les parties en « Partie 1 », « Partie 2 » et les questions en « 1- ».
- Une question sans rien à préparer garde quand même son numéro, seul sur sa ligne (« 4- »).
- Les sous-parties a), b) du sujet sont reprises **à leur place** (entre deux questions, pas en tête de partie si le sujet les met plus loin).
- Beaucoup d'air : chaque question est séparée de la précédente, chaque calcul a sa ligne.

## 2. Façon d'écrire

- **Style télégraphique**, pas de phrases complètes : « câblage sans charge », « visualisation de : $v_2(t)$, $i_1(t)$ grâce au shunt de 1 Ω », « relever : … », « Observation lors de ↗ durée de l'impulsion ».
- **Abréviations** : Alim, Transfo, GBF, oscillo, η, ↗ (augmente), ↘ (diminue).
- **Minuscules** au début des lignes courantes (« câblage avec $D_2$, charge »), majuscule pour les titres de bloc (« Commentaire Résultat obtenu : », « Conclusion : »).
- On **reformule** la consigne en quelques mots, on ne recopie jamais le sujet.
- Les réglages de la consigne passent dans la ligne : « régler $f = 5$ kHz, largeur d'impulsion 100 µs, rapport cyclique 50 % ».

## 3. Les marqueurs

| Marqueur | Usage | Exemple |
|---|---|---|
| `•` | chaque idée / action sous une question | `• relever : $v_2(t)$, et $i_1(t)$` |
| `->` | conséquence, observation, réponse courte | `-> un seuil/saturation apparaît de $i_1(t)$` |
| `↳` | précision rattachée à la ligne au-dessus | `↳ et pince crochet pour visualiser $i_1(t)$`, `↳ $V_R$ négligeable` |
| `⇒` (`\Rightarrow`) | étape suivante d'un calcul | `$\Rightarrow V_Z = -V_1 - V_D$` |
| `= ?` | la grandeur cherchée | `• $V_Z = \ ?$ = Tension aux bornes de la diode zener` |
| `≈` | comparaison avec une valeur constructeur | `$L_p = L_m = 25$ mH $\approx \ldots$ mH` |

## 4. Une grandeur à trouver : toujours le même enchaînement

1. **La question en une ligne** : `• X = ? = définition en mots` (« Valeur inductance », « rapport de transformation »).
2. **La loi de départ** en rouge si c'est une formule de cours : `[$V_L = L\dfrac{di}{dt}$]{.rouge}`.
3. **Les transformations** sur la même ligne, séparées par ⇒ : `⇒ V_L = L Δi/Δt ⇒ L = V_L Δt/Δi`.
4. **L'identification** des grandeurs du montage : `$V_L = V_1 = E = \text{tension d'entrée} = 5\ \text{V}$`.
5. **L'expression appliquée** : `$L_m = V_1\dfrac{\Delta t}{\Delta i_1}$`.
6. **Le remplacement** : valeurs connues écrites, valeurs mesurées en `\ldots` : `$L_m = 5 \times \dfrac{\ldots}{\ldots}$`.
7. **Le résultat** avec unité, en `\ldots` s'il dépend d'une mesure : `$L_m = \ldots\ \text{H} = \ldots\ \text{mH}$`.

Pour une loi des mailles, on nomme la maille : `$M_2 = V_1 + V_D + V_Z + V_R = 0$`, avec à côté `↳ $V_R$ négligeable` si un terme est négligé, et l'encadré ✏️ du schéma de la maille.

## 5. Couleurs

- **Rouge** (`[…]{.rouge}`) : formules de cours (`V_L = L di/dt`, `P = V × I`, `η = P_sortie / P_entrée`, `f = 1/T`) et **définitions** (« isolation galvanique = … »).
- Texte normal pour tout le reste : reformulations, calculs, résultats.
- **Gris** (`::: piste`) : ajouts de la préparation qui ne viennent pas de sa façon d'écrire (réglages à faire, où lire une valeur, à quoi comparer). Courts, une ligne.

## 6. Mesures et tableaux

- Tableau avec **une colonne par grandeur, unité entre parenthèses** dans l'en-tête : `R (Ω) | i sortie (A) | V sortie (V) | P sortie (W) | i entrée (A) | V entrée (V) | P entrée (W) | η (%)`.
- Autant de lignes vides que de points de mesure demandés (5 si le sujet ne dit rien).
- Sous le tableau, en rouge avec `↳`, la formule de chaque colonne calculée : `↳ P = V × I`, `↳ η = P_sortie / P_entrée`.
- Puis la moyenne si utile : `$\eta_{moyen} = \dfrac{\sum \eta}{nb\ \eta} = \dfrac{\ldots + \ldots + \ldots + \ldots + \ldots}{5} = \ldots\ \%$`.

## 7. Oscillogrammes et captures

Sur papier, il redessine l'oscillogramme avec les calibres (« 10 V/div », « 5 V/div »), les noms des courbes ($V_1(t)$, $V_2(t)$) et les durées ($T$, $T_{on}$). En numérique, **on met une capture d'écran à la place** : chaque fois qu'on visualise, relève ou observe quelque chose à l'oscillo (ou sur un autre appareil ou logiciel), un encadré `::: capture` dit :

- `📷 Capture n°k –` les signaux affichés et les conditions (f, α, charge, avec ou sans C…) ;
- `Noter :` les calibres (V/div de chaque voie, s/div) et les grandeurs à lire dessus.

Les captures sont numérotées dans l'ordre du TP, et les calculs y renvoient (« lu sur la capture n°2 »).

## 8. Commentaires et conclusions

Toujours sous cette forme, à remplir pendant le TP :

```
Commentaire Résultat obtenu :
-> ……………………………………………
```

```
• Conclusion :
Le η alim linéaire (16,67 %) est …………… face à η alim découpage (…… %)
```

La phrase de conclusion peut être amorcée avec les valeurs déjà calculées, mais le verdict reste à écrire. Une `::: piste` grise peut dire quoi regarder.

## 9. Notes de marge

Les petits rappels qu'il écrit dans la marge (« f = f commutateur ») vont dans `::: marge`, juste avant la question concernée, et sont répétés si la notion revient plus loin.
