# KAMBILY Marketplace : film publicitaire « Les boutiques d'ici. Un seul panier. »

Dossier de production : direction créative, voix off, storyboard, ressources, déclinaisons et contrôle qualité.

---

## 0. Ce qui est livré, et ce qui reste à faire

Le film livré est **entièrement animé et sonorisé** : image + voix + musique + effets, monté, synchronisé et exporté. Il est **présentable en l'état** comme première version. Deux éléments restent à « monter en gamme » pour une diffusion officielle : la **voix** (remplacer la voix de synthèse par une comédienne) et la **musique** (passer de la maquette originale à une version finale). Ces remplacements se font **sans refaire l'image**, grâce aux stems séparés.

| Élément | État |
|---|---|
| Direction créative, 3 concepts, choix argumenté | ✅ §1–3 |
| Texte définitif de la voix off + direction de jeu + minutage | ✅ §4, `animatic/vo-cues.js` |
| Storyboard de production plan par plan | ✅ §5 et `out/planches/` |
| **Film animé complet** (16:9 et 9:16, 90 s explicatif et spot 15 s) | ✅ `out/kambily-animatique-*.mp4`. Film **entièrement animé** : motion design + UI reconstruites + scènes graphiques de marque. Aucun placeholder. |
| **Voix off** intégrée et synchronisée | ⚠️ ✅ Produite et montée, mais **voix de synthèse neuronale** (modèle open-source Kokoro, voix française `ff_siwis`, licence Apache-2.0). **Ce n'est pas une voix humaine** : à remplacer par une comédienne (§4) pour la version officielle. Stem : `out/audio/kambily-voix-*.wav` |
| **Musique + effets + logo sonore** | ⚠️ ✅ Intégrés et calés sur le montage, musique **atténuée sous la voix** (ducking). Musique **originale temporaire** générée par programme (`render/audio_temp.py`), sans échantillon ni morceau existant — donc sans problème de droits — **mais ce n'est pas la musique finale** (§7). Mix −14 LUFS / −1 dBFS |
| Sous-titres synchronisés (.srt) | ✅ `out/kambily-voix-off-90s.srt`, `…-15s.srt` |
| Essai voix 0–13 s avec prompteur (pour diriger la comédienne) | ✅ `out/kambily-essai-voix-prompteur-16x9.mp4` |
| **Voix d'une comédienne professionnelle** | ❌ À enregistrer (§4.6). C'est l'amélioration n° 1. |
| **Musique finale** (sur mesure ou sous licence) | ❌ À produire (§7). |
| Prises de vues réelles (amélioration **optionnelle**) | ❌ Le film se tient sans tournage ; les 3 moments « humains » sont rendus en scènes graphiques. Fiches de tournage au §9 si vous voulez tourner plus tard. |

**En clair :** vous pouvez regarder, juger et partager le film maintenant. Avant une diffusion payante, faites enregistrer la voix par une comédienne et finaliser la musique (tout le reste est prêt). Je n'ai pas fait passer la voix de synthèse pour une voix humaine : elle est signalée comme telle ici et dans les noms de fichiers (`voix` = scratch).

---

## 1. Diagnostic créatif

KAMBILY n'est pas une boutique : c'est **un lieu où se retrouvent les boutiques de Conakry**. Une publicité qui montre « un smartphone + des produits » la confondrait avec n'importe quel site de vente. Le positionnement doit donc partir de ce qui est **propre à une marketplace et visible dans l'application** :

1. **Plusieurs boutiques, un seul panier.** C'est littéralement le libellé de l'écran Panier (« N boutiques. Un seul panier. »). C'est la promesse la plus distinctive, la plus vraie et la plus simple à montrer.
2. **Des boutiques d'ici, identifiées.** Chaque produit affiche sa boutique (Abdalah, Tombon (Electro), Mouctar Bah, Diouma diwe, Mundjiir, Mamadou Alpha Bah…), et l'accueil parle de « Tendances à Conakry ». Le local est un atout de confiance.
3. **La confiance à la livraison.** Le code de livraison (« Le livreur ne valide la commande qu'avec ton code ») répond à la peur n° 1 de l'achat en ligne : payer et ne rien recevoir. C'est une preuve concrète, pas un slogan.
4. **Les moyens de paiement du quotidien** : Orange Money, MTN Mobile Money, carte, PayCard, paiement à la livraison. On les montre à l'écran sans en faire un argument criard.

La tension narrative la plus universelle pour le public guinéen connecté : **ce que je veux est éparpillé** (un produit dans une boutique, l'autre à l'autre bout de la ville). KAMBILY le rassemble. Le film est construit sur cette tension, résolue par l'image du panier unique.

---

## 2. Trois concepts

| | A. « Un seul panier » (**retenu**) | B. « Le fil » | C. « Rideau levé » |
|---|---|---|---|
| Idée centrale | Ce qu'on cherche est éparpillé entre plusieurs boutiques ; KAMBILY les réunit dans un seul panier. | Une ligne teal (tirée de la courbe du logo) relie l'acheteuse, les boutiques et le livreur, du clic à la porte. | Le matin, un commerçant lève son rideau métallique… et sa vitrine s'ouvre sur l'écran de milliers de téléphones. |
| Émotion | Soulagement, plaisir de la simplicité | Fluidité, continuité | Fierté, ambition |
| Mécanisme visuel | Raccords de forme : deux repères éloignés **convergent** et deviennent le pictogramme K (un grand et un petit quart de cercle qui se rejoignent) | Plan-séquence virtuel guidé par une ligne | Raccord rideau → interface |
| Avantage commercial | Montre la fonction **différenciante** réelle (multi-boutiques) et la confiance (code) | Très élégant, mémorisation graphique | Excellent pour recruter des vendeurs |
| Limite | Demande un vrai casting pour les plans tournés | Risque d'abstraction : on retient la ligne, pas le service | Centre le film sur les vendeurs ; le public prioritaire (acheteurs) passe au second plan |

**Choix : A.** Meilleure compréhension du service en une phrase, différenciation par une fonctionnalité réelle et visible, mémorisation par une formule qui reprend un libellé de l'app (l'utilisateur la retrouvera **dans** le produit). B est intégré comme grammaire de transition, C comme séquence vendeurs (plan 8) et comme piste pour une future déclinaison B2B.

---

## 3. Direction créative retenue

- **Titre de travail :** « Un seul panier »
- **Idée :** *Les boutiques d'ici, enfin au même endroit.*
- **Émotion :** passer de « c'est compliqué » à « c'est réglé », avec un sourire, sans euphorie.
- **Format :** publicité **explicative**. **Durée maître : 90 s.** Le film prend le temps de montrer tout le parcours réel (découvrir, choisir, panier multi-boutiques, livraison, paiement, confirmation, suivi, remise avec le code), puis l'invitation aux commerçants. Le spot de 15 s garde la version « impact ».
- **Tutoiement acheteur / vouvoiement commerçant.** Le film tutoie l'acheteuse, comme l'app (« ton code », « reçois »), puis passe au « vous » pour les boutiques. Ce changement de registre marque le changement d'audience sans carton explicatif.

### Slogans proposés

1. **« Les boutiques d'ici. Un seul panier. »** ← **recommandé**
2. « Toutes vos envies, un seul panier. » (« toutes » : promesse trop large)
3. « Kambily rapproche. » (élégant mais abstrait)
4. « Le marché vient à toi. » (fort, mais évoque un service de courses)
5. « Trouve. Compare. Reçois. » (générique)

**Pourquoi le n° 1 :** il dit ce qu'est le service (des boutiques), d'où elles viennent (d'ici, donc confiance et proximité) et ce qu'il apporte (un seul panier). Il ne promet ni délai, ni prix, ni exhaustivité, et il reprend un libellé réel de l'application.

---

## 4. Voix off (pilote du montage)

### 4.1 Texte définitif, film maître (90 s)

| # | Début → fin | Texte | Mot porteur (instant) | Scène / image synchronisée |
|---|---|---|---|---|
| 1 | 0,7 → 2,2 | « Un produit ici… » | *ici* (1,6) | 1 · Plan de ville : le repère « Abdalah · Beauté » se pose |
| 2 | 2,7 → 4,6 | « L'autre, à l'autre bout de la ville. » | *l'autre bout* (3,6) | Le repère « Tombon · Électro » apparaît loin, la route pointillée les relie |
| — | 4,6 → 6,9 | *silence, image* | — | Les deux repères convergent |
| 3 | 6,9 → 8,7 | « Et si les boutiques venaient à toi ? » | *venaient à toi* (8,0) | 2 · Le pictogramme K se forme sur le teal |
| 4 | 9,4 → 12,6 | « Kambily, c'est la marketplace des boutiques de chez toi. » | *de chez toi* (12,0) | « kambily » s'affiche sur le mot (9,3), puis la définition (10,0) |
| 5 | 14,2 → 16,8 | « Tout commence par une envie. » | *envie* (16,2) | 3 · Écran Catégories (libellés et nombres réels), 3 catégories mises en avant |
| 6 | 19,6 → 22,4 | « Des centaines de produits, des boutiques d'ici. » | *boutiques d'ici* (21,8) | 4 · Vitrine Beauté & Soins ; six cartes boutiques réelles sortent du téléphone |
| 7 | 23,0 → 26,6 | « Beauté, mode, high-tech : tu compares, tu choisis. » | *Beauté* · *mode* · *high-tech* · *tu choisis* (26,0) | Vitrines Beauté → Chaussures → Électronique, calées sur les mots |
| 8 | 28,8 → 31,6 | « Sur chaque produit : le prix, et la boutique qui le vend. » | *la boutique* (30,6) | 5 · Fiche produit The Ordinary, 190 000 GNF, boutique Abdalah |
| 9 | 31,9 → 35,2 | « Pas reçu, cassé ou différent ? Kambily te protège. » | *te protège* (34,4) | L'encadré réel « Pas reçu, différent, cassé ? Kambily prend en charge… » s'allume ; tap « Ajouter au panier » à 35,2 |
| 10 | 38,2 → 41,4 | « Plusieurs boutiques… » | *Plusieurs boutiques* (40,4) | 6 · Fond teal ; les deux boutiques glissent dans le panier |
| 11 | 42,0 → 44,4 | « … un seul panier. » | *un seul panier* (43,6) | Le bandeau réel « 2 boutiques. Un seul panier. » ; « Un seul panier. » en lime ; tap « Passer au paiement » |
| 12 | 45,6 → 49,0 | « On te livre chez toi, à ton heure. » | *chez toi* (48,2) | 7 · Écran Livraison ; créneau « Après-midi · 14h-18h » choisi (47,6) |
| 13 | 49,4 → 52,6 | « Standard, ou express le jour même. » | *express* (51,8) | « Livraison express · Aujourd'hui » sélectionnée (51,0) |
| 14 | 53,6 → 57,0 | « Tu paies comme tu veux : Orange Money, MTN, carte… » | *comme tu veux* (55,0) | 8 · Écran Paiement, moyens réels en cascade, Orange Money sélectionné (56,4) |
| 15 | 57,4 → 60,4 | « … ou en espèces à la livraison. » | *à la livraison* (59,6) | « … ou à la livraison. » ; tap « Payer 4 320 000 GNF » |
| 16 | 61,6 → 64,4 | « Et voilà : c'est confirmé. » | *confirmé* (63,6) | 9 · « Commande confirmée » : la pastille éclot (62,2), le code 5348 monte |
| 17 | 68,0 → 71,6 | « Tu la suis étape par étape, jusqu'à ta porte. » | *étape par étape* (70,4) | 10 · Écran Suivi : les 7 étapes réelles s'allument une à une |
| 18 | 74,0 → 77,6 | « Et ton colis ne se remet qu'avec ton code. » | *ton code* (77,0) | 11 · Scène graphique : maison, colis, carte « Votre code de livraison 5348 », bouclier (76,4), « Livrée ✓ » |
| 19 | 79,6 → 82,0 | « Vous avez une boutique ? » | *boutique* (81,2) | 12 · Devanture stylisée, store qui se déroule |
| 20 | 82,6 → 85,0 | « Vendez sur Kambily. » | *Vendez sur Kambily* (83,8) | « Vendez sur Kambily. » + contact@kambily.com |
| 21 | 85,6 → 86,6 | « Kambily. » | *Kambily* (85,9) | 13 · Les cartes boutiques convergent ; le **logo** s'impose sur le mot |
| 22 | 87,0 → 89,6 | « Les boutiques d'ici. Un seul panier. » | *un seul panier* (88,8) | Accroche puis www.kambily.com ; logo stable jusqu'à 90 s |

**≈ 160 mots en 90 s** : débit posé (≈ 2,4 mots/s dans les phrases), avec des respirations entre chaque étape pour laisser lire l'écran.

### 4.2 Direction de comédienne, phrase par phrase

| # | Intention | Ton / rythme | Mots à appuyer légèrement | Pauses |
|---|---|---|---|---|
| 1–2 | **Intrigue.** Elle constate, elle ne vend pas, comme à une amie. | Bas, proche du micro, lent. | *ici* / *l'autre bout* | Vraie suspension après « ici… » |
| 3 | **Ouverture.** Une idée qui naît. | Légère montée, premier sourire sur *toi*. | *venaient à toi* | Laisser mourir la fin |
| 4 | **Présentation.** La marque se présente simplement. | Clair, chaleureux, assuré. | *Kambily* (net), *de chez toi* | Micro-pause après « Kambily, » |
| 5 | **Complicité.** | Doux, presque confidentiel. | *envie* | — |
| 6–7 | **Découverte, flânerie.** L'énumération se promène. | Plus lumineux ; chaque catégorie avec une couleur différente. | *boutiques d'ici*, *Beauté*, *mode*, *high-tech*, *choisis* | ≈ 0,3 s entre les catégories |
| 8–9 | **Clarté puis réassurance.** | 8 informatif et simple ; 9 posé, protecteur, sans dramatiser. | *la boutique* ; *te protège* | Petite suspension après la question |
| 10–11 | **Le message clé.** | Deux temps nets ; « un seul panier » un ton plus bas, conclusif. | *Plusieurs*, *un seul* | ≈ 0,6 s entre les deux |
| 12–13 | **Service, confiance.** | Rassurant, précis. | *chez toi*, *à ton heure*, *express* | ≈ 0,4 s entre les phrases |
| 14–15 | **Liberté.** | Léger, souriant ; l'énumération des moyens de paiement reste fluide. | *comme tu veux*, *à la livraison* | Suspension sur « carte… » |
| 16 | **Satisfaction.** | Court, souriant, sans exclamation. | *confirmé* | — |
| 17 | **Accompagnement.** | Calme, continu. | *étape par étape*, *ta porte* | — |
| 18 | **Garantie.** Une promesse donnée doucement. | Grave léger, posé. | *ton code* | Micro-pause avant « qu'avec » |
| 19–20 | **Invitation aux commerçants.** Plus droite, plus directe, sans promesse de résultat. | Un cran d'appui en plus. | *boutique*, *Vendez sur Kambily* | ≈ 0,5 s entre les deux |
| 21–22 | **Signature.** Calme, assurée, chaleureuse. | « Kambily. » seul, avec intention. L'accroche plus douce. | *Kambily*, *d'ici*, *un seul* | ≈ 0,4 s après « Kambily. » |

**À éviter absolument :** voix de présentatrice de journal, exclamations, montées systématiques en fin de phrase, accent forcé, ton « pub télé crié ».

### 4.3 Prononciation

- **KAMBILY** : prononciation de travail [kɑ̃.bi.li] ou [kam.bi.li], c'est-à-dire « kam-bi-li », trois syllabes égales, sans accent anglais sur « bi ». **À faire valider par KAMBILY avant la séance** : la prononciation officielle de la marque n'est pas connue à ce stade et ne doit pas être devinée. Si le nom vient d'une langue locale, l'actrice doit le prononcer comme les fondateurs.
- Liaisons : « boutiques‿d'ici », « les‿boutiques ». Pas de liaison forcée dans « Plusieurs boutiques ».

### 4.4 Profil et casting

- Comédienne voix off **professionnelle**, 25–40 ans, francophone, **idéalement guinéenne ou ouest-africaine**, avec une couleur naturelle (jamais imitée). Timbre chaud et clair, légèrement velouté, sans gravité artificielle.
- Casting : 3 à 5 comédiennes, chacune enregistre l'**essai de 13 s** (phrases 1 à 4) sur l'image de `out/kambily-essai-voix-prompteur-16x9.mp4`.
- Grille d'évaluation, notée sur 5 par critère, critère éliminatoire si < 3 : **naturel**, **interprétation**, **prononciation / intelligibilité** (y compris « Kambily »), **adéquation à la marque**, **compatibilité avec le rythme** (les mots porteurs tombent-ils sur leurs instants ?).
- Droits : cession écrite des droits d'exploitation publicitaire (supports, territoires, durée). **Aucun clonage de voix.**

### 4.5 Voix de synthèse utilisée comme scratch (ce qui a été fait ici)

La version livrée utilise une **voix de synthèse neuronale open-source** (modèle Kokoro, voix française `ff_siwis`, licence Apache-2.0), générée localement, phrase par phrase, depuis `animatic/vo-cues.js` (`render/vo_gen.py`). Débit et pauses réglés par phrase (§4.2). C'est une **voix de travail**, honnêtement signalée, destinée à entendre le film monté — **pas** la voix officielle.

Ses limites : français européen (pas de couleur ouest-africaine), expressivité plus plate que celle d'une comédienne, « Kambily » prononcé via une graphie de contournement (« Kambili ») car le moteur lit « Kambily » en anglais. **Pour la diffusion : enregistrer une comédienne (§4.6).** Les moteurs commerciaux haut de gamme (voix françaises expressives sous licence) sont une autre option, mais une vraie voix reste préférable.

#### Brancher une voix Google Cloud TTS (prêt, il ne manque que la clé)

L'API Google Text-to-Speech est joignable depuis l'environnement de production ; seule une **clé API** manque. Avec une clé (projet Google Cloud, API Text-to-Speech activée) :

```bash
export GOOGLE_TTS_API_KEY="…"
python3 render/vo_google.py --list                 # voir les voix fr-FR (choisir une voix féminine Chirp 3 HD)
VO_VOICE=fr-FR-Chirp3-HD-Aoede ./render/mix.sh     # régénère la voix + remixe les 4 vidéos
```

Même minutage, mêmes fichiers : l'image ne change pas. Toute autre source de voix (Flora, comédienne, autre moteur) se branche de la même façon en remplaçant `out/audio/kambily-voix-master.wav` (§4.8).

### 4.6 Consignes d'enregistrement (séance avec comédienne)

- Cabine traitée ou pièce très mate ; bruit de fond < −60 dBFS.
- Micro statique à large membrane, anti-pop, distance **constante** de 15 à 20 cm, légèrement hors axe.
- 48 kHz / 24 bits, crêtes autour de −10 à −6 dBFS, aucun traitement à la prise.
- La comédienne joue **à l'image** avec le prompteur (le mot-clé surligné indique l'instant visé).
- Enregistrer : 3 prises complètes en continu (continuité du souffle), puis 2 à 3 prises isolées par phrase, plus 2 alternatives d'intention pour les phrases 4, 10–11 et 21–22 (plus chaleureuse / plus affirmée).
- Enregistrer aussi la **version 15 s** (5 phrases, §8.2) ; le débit ne doit pas être accéléré, le texte est déjà raccourci.

### 4.7 Post-production voix

- Nettoyage léger (bruits de bouche, bruit de fond) sans « effet aquarium ».
- Respirations naturelles **conservées** quand elles portent le sens (avant 4, avant 10, avant 18, avant 21) ; aucun souffle ajouté artificiellement.
- Filtre passe-haut ≈ 80 Hz, EQ douce (présence + 1 à 2 dB vers 3–5 kHz si nécessaire), de-esser, compression modérée (ratio 2:1 à 3:1, 2–4 dB de réduction). Pas de réverbération perceptible.
- Raccords entre prises en fondus de 10 à 30 ms sur les silences, jamais au milieu d'un mot.

### 4.8 Remplacer ou réenregistrer la voix sans refaire le film

Le montage lit son minutage dans **`animatic/vo-cues.js`**. Après l'enregistrement :
1. Mesurer dans la prise retenue le début, la fin et l'instant du mot porteur de chaque phrase.
2. Reporter ces valeurs dans `vo-cues.js` (champs `a`, `b`, `keyAt`).
3. Les sous-titres se mettent à jour automatiquement (`node render/srt.mjs`, puis rendu). Dans After Effects ou Premiere, importer le .srt comme repères de composition : les animations de chaque plan sont ancrées sur ces repères (§9.2).
4. Livrer la voix en **stem séparé** (voix seule, sans musique) : une nouvelle voix ou une nouvelle langue se pose sans toucher à l'image.

---

## 5. Storyboard de production (film maître 16:9, 90 s)

Planches : `out/planches/16x9-planXX-*.png` et `9x16-…` (une image clé par scène). Film de référence : `out/kambily-animatique-master-16x9.mp4`. Le film est **entièrement animé** ; chaque scène s'enchaîne par un fondu de 0,45 s.

| Scène | TC | Composition | Animation | Texte à l'écran | VO | Son |
|---|---|---|---|---|---|---|
| **1. Le problème** | 0:00–0:07 | Plan de ville stylisé (rues et îlots teal), deux repères boutiques éloignés reliés par une route pointillée lime | Travelling lent ; repères qui se posent ; à 5,4 s le repère de droite rejoint celui de gauche | « Un produit ici. » / « L'autre, là-bas. » | 1–2 | Ambiance de rue filtrée, notes de marimba sur les repères |
| **2. La marque** | 0:07–0:14 | Fond teal, pictogramme K officiel, « kambily », définition | Raccord de forme (convergence → K), le K monte, mot « kambily » puis définition ; le téléphone monte, le fond s'éclaircit | « kambily » / « La marketplace des boutiques de chez toi. » | 3–4 | La musique démarre sur le K |
| **3. L'envie** | 0:13–0:19 | Téléphone (tiers droit), écran Catégories réel | Défilement doux, 3 catégories cerclées (Beauté & Soins, Chaussures, Électronique) | « Tout commence par une envie. » | 5 | Ticks sur les catégories |
| **4. Les vitrines** | 0:19–0:28 | Listes réelles (produits, boutiques, prix GNF), cartes boutiques autour du téléphone | Volets latéraux calés sur « Beauté », « mode », « high-tech » | « Des centaines de produits. » / « Des boutiques d'ici. » | 6–7 | Ticks sur chaque vitrine |
| **5. Le produit** | 0:28–0:37 | Fiche produit The Ordinary (190 000 GNF, Abdalah) + encadré réel de protection | Ouverture depuis la carte ; encadré protection souligné ; tap, le produit vole vers le panier | « Le prix. » / « La boutique. » / « Tout est clair. » | 8–9 | Tap, « pop » d'arrivée |
| **6. Un seul panier** | 0:37–0:45 | Fond qui vire au teal ; panier réel à deux boutiques | Blocs boutiques qui glissent ; bandeau « 2 boutiques. Un seul panier. » souligné ; tap paiement | « Plusieurs boutiques. » / « Un seul panier. » | 10–11 | Temps fort musical |
| **7. La livraison** | 0:45–0:53 | Écran Livraison réel (modes, par boutique, créneau, code de validation) | Créneau « Après-midi » puis « Express » sélectionnés | « Chez toi, à ton heure. » / « Standard ou express. » | 12–13 | Ticks de sélection |
| **8. Le paiement** | 0:53–1:01 | Écran Paiement réel, total 4 320 000 GNF | Moyens réels en cascade, Orange Money sélectionné, tap « Payer » | « Comme tu veux : » / « Orange Money, MTN, carte… » / « … ou à la livraison. » | 14–15 | Ticks, tap |
| **9. Confirmé** | 1:01–1:07 | Écran « Commande confirmée » réel, code 5348 | Pastille qui éclot, code qui monte | « Et voilà. » / « C'est confirmé. » | 16 | Carillon |
| **10. Le suivi** | 1:07–1:13 | Écran Suivi réel (7 étapes) | Les étapes s'allument une à une, le titre change | « Tu suis ta commande, » / « étape par étape. » | 17 | 7 ticks légers |
| **11. La confiance** | 1:13–1:19 | Scène graphique : maison, colis déposé, carte « Votre code de livraison », bouclier | Illustration et carte qui montent ; bouclier et « Livrée ✓ » | « Ton code. » / « Ton colis. » | 18 | Musique qui redescend ; carillon doux |
| **12. Les commerçants** | 1:19–1:25 | Scène graphique : devanture au store lime, colis prêts, enseigne K, carte « Tombon · Électro » | Le store se déroule ; carte et texte en trois temps | « Vous avez une boutique ? » / « Vendez sur Kambily. » / contact@kambily.com | 19–20 | Remontée d'énergie |
| **13. Signature** | 1:25–1:30 | Fond teal, logo, accroche, URL | Cartes boutiques qui convergent → logo sur « Kambily » → accroche → URL ; logo stable 3,7 s | « Les boutiques d'ici. Un seul panier. » / www.kambily.com | 21–22 | Logo sonore, fin naturelle |

**Règles de raccord :** aucune coupe au milieu d'une phrase (vérifié dans `vo-cues.js`) ; chaque scène change dans un silence de la voix.

## 6. Direction artistique

### Palette

| Rôle | Couleur | Usage |
|---|---|---|
| Teal KAMBILY (référence fournie) | **#048B9A** | Fonds de marque, prix, boutons principaux, pictogramme |
| Teal profond (dérivé) | #036F7B / #02434B | Ombres, texte sur lime |
| Lime (relevé dans l'app et la campagne) | #D9FF98 | Accents : mot-clé des titres, accroche finale, pastille de confirmation |
| Lime clair (relevé dans l'app) | #F3FFE0 | Encadrés « code » |
| Blanc / gris | #FFFFFF, #F5F7F7, #F2F3F3, #E6E8E8, #9AA0A3 | Fonds UI, cartes, textes secondaires |
| Encre | #17181A | Texte principal |

*Les dérivés et le lime sont relevés sur les captures : à confirmer avec la charte officielle si elle existe.*

### Typographie

- **Poppins** (SemiBold / Bold pour les titres, Medium pour les sous-titres) : c'est la police apparente de l'application et de l'affiche « Kambily débarque sur vos écrans ! », d'où une cohérence directe entre le film et le produit. À confirmer avec KAMBILY.
- Titres en 2 lignes maximum ; approche −2 % ; la seconde ligne porte la couleur (teal ou lime).
- Corps minimum à l'écran : 44 px en 1080p (16:9) et 56 px en 1080 × 1920 (9:16).

### Lumière, matières, profondeur

- Plans tournés : lumière naturelle chaude (matin, après-midi), contre-jour doux, peaux bien exposées et nuancées, étalonnage neutre-chaud, légèrement désaturé sur les fonds pour que le teal de marque reste la seule couleur saturée.
- Motion : fonds plats (teal ou gris très clair), **une seule ombre portée** douce sous le téléphone et les cartes. Grain fin (5 %) pour lier le tourné et la 2D. Pas de néons, pas de particules, pas de reflets « verre » appuyés.

### Règles d'animation

- Courbes : **ease-out cubique ou exponentielle** pour les arrivées, in-out pour les déplacements, léger *back* (1,4) seulement pour les éléments qui « se posent » (cartes, pastille). Jamais de linéaire.
- Durées : entrées 0,5–0,7 s, cascades de 40 à 80 ms, volets d'écran 0,4 s.
- Un seul mouvement principal à la fois ; l'œil suit toujours un élément.
- Les interfaces ne flottent pas : elles restent dans le téléphone, sauf les **cartes boutiques**, qui sortent volontairement de l'écran parce qu'elles représentent le « monde réel » des commerçants.
- **Motif de marque :** convergence de deux éléments (grand + petit), qui reprend la construction du pictogramme. Utilisé 3 fois : fin du plan 1, plan 2, plan 9.

---

## 7. Musique et design sonore

### 7.1 Musique

- Morceau **sur mesure ou sous licence commerciale vérifiée** (synchro + diffusion sur réseaux sociaux et web, territoire Guinée et monde, durée de la campagne).
- 100–104 BPM, pop afro contemporaine épurée : basse ronde, percussions sèches, motif de marimba/mallet en deux notes. Pas de *drop* EDM, pas de pastiche.
- Structure (90 s) : 0–7 s ambiance · 6,6 s départ sur le K · 13–37 s montée (découverte, produit) · **37–45 s temps fort** (« un seul panier ») · 45–73 s pulsation régulière (livraison, paiement, confirmation, suivi) · 73–79 s redescente (confiance) · 79 s remontée (commerçants) · logo sonore à 85,9 s · fin naturelle à 90 s.
- La musique est **atténuée de 8 à 10 dB sous la voix** (ducking doux), avec un creux EQ de 2–3 dB vers 2–4 kHz.

### 7.2 Effets sonores

Clics d'interface feutrés (tap, volet), un « pop » (panier), un « chime » (✓), notes de mallet sur les repères. **Aucun whoosh générique.** Niveau : toujours sous la voix.

### 7.3 Logo sonore

Deux notes de mallet (grave puis aiguë, comme le grand et le petit quart de cercle du pictogramme) suivies d'un accord ouvert court, à 47,5 s sur l'apparition du logo, juste après « Kambily ».

### 7.4 Mixage et livraison audio

- Intégré **−14 LUFS** (réseaux sociaux), crêtes ≤ **−1 dBTP** ; version **−23 LUFS** si diffusion TV.
- Vérification d'écoute sur téléphone (haut-parleur), ordinateur portable et casque.
- Stems à livrer : **voix seule**, musique seule, effets seuls, mix complet.

---

## 8. Déclinaisons

### 8.1 Film maître explicatif : 90 s, 16:9 et 9:16 (voir §5)

### 8.2 Spot 15 s, un remontage narratif (pas une accélération)

La structure problème → solution → preuve → marque est conservée :

| TC | Scène (source maître) | VO | Texte |
|---|---|---|---|
| 0:00–2,6 | Le problème (scène 1) | « Un produit ici, l'autre ailleurs. » | Un produit ici. / L'autre, là-bas. |
| 2,6–6,6 | Un seul panier (scène 6) | « Sur Kambily : plusieurs boutiques, un seul panier. » | Plusieurs boutiques. / Un seul panier. |
| 6,6–9,6 | Confirmé (scène 9) | « Et ton colis ne se remet qu'avec ton code. » | C'est confirmé. |
| 9,6–11,4 | La confiance (scène 11) | *(fin de phrase)* | Ton code. / Ton colis. |
| 11,4–15 | Signature (scène 13) | « Kambily. Les boutiques d'ici. Un seul panier. » | Logo, accroche, URL |

Fichiers : `out/kambily-animatique-15-16x9.mp4` et `…-15-9x16.mp4`.

### 8.3 Version verticale 9:16, réagencée

- Téléphone centré et agrandi (× 1,32), titres dans le tiers supérieur, cartes boutiques dans le tiers inférieur.
- **Zones de sécurité** (1080 × 1920) : 220 px en haut, 340 px en bas, 140 px à droite (boutons TikTok / Reels), 60 px à gauche. Repère visible avec `?format=9x16&safe=1`.
- Sous-titres incrustés au-dessus de la zone basse, sur fond sombre à 72 %.

### 8.4 Déclinaison suggérée (hors périmètre) : « Rideau levé », 20 s pour les commerçants

À partir du concept C ; elle exige de connaître le **parcours vendeur réel** (inscription, tableau de bord), qui ne figure pas dans les captures fournies.

---

## 9. Ressources et instructions de production

### 9.1 Inventaire

**Disponibles (fournies)**
- Pictogramme K (fichier 1 001 × 1 001 px, raster) ; couleur #048B9A confirmée.
- Affiche « Kambily débarque sur vos écrans ! » (logotype, bannière livreur en polo).
- Captures : Accueil, fiche produit (Abaya), Catégories, Beauté & Soins, Chaussures, Électronique, Panier, Livraison, Paiement, Commande confirmée, Suivi.
- Contact : contact@kambily.com · www.kambily.com.

**À obtenir auprès de KAMBILY**
1. **Logo vectoriel officiel** (pictogramme + logotype « kambily », SVG ou AI) et charte, si elle existe. *Le logotype de l'animatique est un placeholder typographique.*
2. **Prononciation officielle** du nom.
3. Captures **HD natives** (1290 × 2796 ou plus) des écrans du §5, sur un compte de démonstration propre (sans produits « TEST Playwright », sans données personnelles réelles) ; idéalement la **fiche produit réelle** de The Ordinary chez Abdalah.
4. **Visuels produits HD** et autorisation des boutiques montrées (Abdalah, Tombon (Electro), Mouctar Bah, Diouma diwe, Mundjiir, Mamadou Alpha Bah), y compris leur accord pour apparaître dans une publicité.
5. **Confirmation que chaque fonction montrée est en production** : multi-boutiques, créneaux, moyens de paiement listés, code de livraison, suivi.
6. Polo officiel de livreur (pour le tournage) ; accord d'une boutique partenaire pour le plan 8.
7. Le parcours d'inscription des vendeurs, s'il existe ; sinon le film garde « Écrivez-nous : contact@kambily.com ».

**À produire**
- 3 plans tournés (casting de 3 personnes : acheteuse, livreur, gérant), musique, effets sonores, voix off, mixage, motion final en 4K/1080p.

### 9.2 Méthode d'exécution recommandée

1. **Valider l'essai voix** (13 s), puis enregistrer la voix complète **avant** l'animation finale.
2. Reporter le minutage réel dans `vo-cues.js`, rendre l'animatique recalée, puis faire valider le rythme par KAMBILY.
3. **Tournage (optionnel)** : le film se tient sans prises de vues. Si vous voulez une présence humaine, 1 journée à Conakry suffit pour remplacer les scènes 1, 11 et 12 (fiches au §9.3) : lumière naturelle, 4K 25 i/s, Log, optiques fixes 35/50/85 mm, macro pour les inserts téléphone (l'UI est réincrustée).
4. **Motion** dans After Effects (ou équivalent) :
   - Composition maître 1920 × 1080 à 25 i/s et composition 1080 × 1920 **construite séparément** (même précompositions d'écrans, mises en page distinctes).
   - Écrans reconstruits en vectoriel à partir des captures HD (police Poppins, libellés **identiques**), une précomposition par écran.
   - Téléphone : maquette 3D ou 2.5D réaliste (pas de déformation), écran en précomposition ; une seule ombre douce.
   - Repères de composition importés du .srt : chaque animation clé est ancrée sur le `keyAt` de sa phrase.
   - L'animatique `animatic/index.html` sert de **référence chiffrée** : courbes, durées et positions sont lisibles dans le code (une fonction par plan).
5. **Montage et étalonnage** : intégration du tourné, étalonnage commun, grain 5 %.
6. **Mixage** (§7.4), puis exports (§9.4).

### 9.3 Fiches de tournage

- **Plan 1 :** Aminata, 25–30 ans, tenue urbaine contemporaine colorée sans motif bruyant ; rue commerçante animée mais lisible (arrière-plan flou) ; elle regarde son téléphone puis lève les yeux, légèrement contrariée. 6–8 s utiles, plusieurs prises de regard.
- **Plan 7 :** pas de porte, après-midi ; le livreur (polo Kambily, posture professionnelle) tend le colis ; insert macro de l'écran « Votre code de livraison » (incrusté en post) ; sourires naturels, pas de « pouce levé ».
- **Plan 8 :** comptoir de boutique d'électronique réelle et rangée ; le gérant emballe avec soin, pose le colis sur une pile, regard caméra et léger sourire.

*Des prompts d'images générées peuvent servir de moodboard ou de prévisualisation, **pas** d'images finales (exigence d'authenticité des personnages) :*

> « Photographie publicitaire, rue commerçante de Conakry au matin, lumière rasante dorée, jeune femme guinéenne de 27 ans en tenue urbaine contemporaine, téléphone en main, expression naturelle et pensive, profondeur de champ faible, optique 85 mm, étalonnage neutre-chaud, réaliste, sans texte. »
>
> « Livreur souriant en polo vert lime et teal tendant un colis à une jeune femme sur le pas de sa porte à Conakry, après-midi, lumière naturelle douce, plan moyen, photographie publicitaire réaliste. »
>
> « Gérant d'une boutique d'électronique à Conakry emballant soigneusement un ordinateur portable sur son comptoir, colis prêts à côté, lumière de fin de journée, regard caméra, sourire léger, 35 mm, réaliste. »

### 9.4 Exports finaux

- 16:9 : 1920 × 1080 (et 3840 × 2160), H.264 ou ProRes en master, 25 i/s.
- 9:16 : 1080 × 1920, H.264, débit élevé.
- 15 s dans les deux formats ; versions **avec et sans sous-titres incrustés** ; .srt séparés ; stems audio.

---

## 10. Contrôle qualité

### 10.1 Points d'alerte relevés dans les captures (à régler avant diffusion)

| Observation | Risque | Décision dans le film |
|---|---|---|
| « **1 boutiques**. Un seul panier. » et « Vos **1 boutique** préparent… » | Faute visible | Le film montre 2 boutiques (« 2 boutiques », « Vos 2 boutiques »). **Signaler à l'équipe produit** l'accord au singulier. |
| Fiche Abaya avec une option « **Stockage 128 Go / 256 Go** » | Incohérence produit visible | Fiche Abaya non utilisée ; on montre The Ordinary. |
| Produits « **TEST Playwright** » dans Électronique ; produits sans image (Asics Gel, sneaker Nike) | Données de test visibles | Exclus de l'animatique ; captures finales à faire sur un catalogue propre. |
| « Fiabilité 81 % · 391 ventes · depuis 2026 », avis clients | Données de démonstration possibles | **Non montrés** tant qu'ils ne sont pas confirmés comme réels. |
| « Livraison standard 0 GNF », « Frais de service 0 GNF », « Livré aujourd'hui » | Promesse tarifaire ou de délai | Visibles à l'écran comme dans l'app, **jamais dits en VO** ; l'express à 25 000 GNF reste visible, par honnêteté. À confirmer. |
| « Payer en 2 fois », « Quelqu'un paie pour moi depuis l'étranger ? », « Portefeuille Kambily » | Fonctions non mises en avant | Non montrées : elles alourdiraient le récit. Pistes pour de futures déclinaisons, si elles sont confirmées. |
| Numéro de téléphone et adresse dans les captures Livraison et Suivi | Données personnelles | **Non affichés** dans le film (l'adresse est omise de la reconstruction). |

### 10.2 Liste de vérification finale

**Marque**
- [ ] Logo officiel vectoriel, jamais redessiné, déformé ou recoloré ; zone de protection respectée.
- [ ] Teal #048B9A exact (vérifier la conversion vidéo Rec.709 : pas de dérive vers le vert ou le bleu).
- [ ] Logo final stable ≥ 3 s, CTA lisible (www.kambily.com).

**Interfaces**
- [ ] Chaque libellé à l'écran est identique à l'application en production.
- [ ] Prix en GNF, séparateur d'espace (« 190 000 GNF ») ; total exact (190 000 + 4 130 000 = **4 320 000 GNF**).
- [ ] Aucune fonction montrée qui ne soit disponible ; aucun produit de test ; aucune donnée personnelle.

**Texte et promesses**
- [ ] Orthographe et typographie française (espaces insécables avant « ? ! : », apostrophes typographiques).
- [ ] Aucun superlatif (« n° 1 », « le moins cher »), aucun délai garanti en VO, aucune promesse de ventes aux commerçants.
- [ ] Tutoiement acheteur / vouvoiement commerçant cohérents.

**Lisibilité mobile**
- [ ] Test sur un vrai téléphone, luminosité moyenne : chaque texte est lisible en moins de 1,5 s.
- [ ] Textes et CTA hors des zones d'interface des plateformes (9:16).
- [ ] Film compréhensible **sans le son** (titres + sous-titres).

**Rythme et synchro**
- [ ] Chaque mot porteur de la voix finale tombe à ±0,15 s de son événement visuel.
- [ ] Aucune coupe au milieu d'une phrase ; silences respectés.
- [ ] L'accroche est compréhensible dans les 2 premières secondes.

**Voix et son**
- [ ] Voix d'une comédienne professionnelle (ou, à défaut, synthèse **déclarée comme telle**) ; « Kambily » prononcé selon la validation de la marque.
- [ ] −14 LUFS / −1 dBTP ; voix intelligible sur haut-parleur de téléphone.
- [ ] Fin audio naturelle, sans coupure.

**Droits**
- [ ] Musique, SFX et voix sous licence commerciale écrite ; autorisations à l'image des personnes filmées ; accord des boutiques montrées ; marques des produits visibles (The Ordinary, HP, etc.) vérifiées par le juridique ou remplacées par des produits génériques.

---

## 11. Fichiers et rendu

```
kambily-pub/
├── BIBLE-PRODUCTION.md          ← ce document
├── animatic/
│   ├── index.html               ← film animé (moteur d'animation, une fonction par plan)
│   ├── vo-cues.js               ← minutage voix : source unique pour le montage et les sous-titres
│   └── assets/                  ← pictogramme extrait du fichier fourni, recadrages produits, Poppins
├── render/
│   ├── all.sh                   ← rend toutes les vidéos
│   ├── render.mjs               ← rendu image par image (Playwright + ffmpeg)
│   ├── stills.mjs               ← planches du storyboard
│   ├── srt.mjs                  ← sous-titres .srt
│   ├── audio_temp.py            ← musique temporaire + SFX + logo sonore (synthèse programmée)
│   ├── vo_gen.py                ← voix off scratch (Kokoro ff_siwis) depuis vo-cues.js
│   ├── mux.sh                   ← ajoute musique+SFX seuls aux MP4 (version muette de voix)
│   └── mix.sh                   ← mixe voix + musique + SFX (ducking) dans les MP4 → version sonorisée
└── out/
    ├── kambily-animatique-master-16x9.mp4 / -9x16.mp4   (90 s, explicatif)
    ├── kambily-animatique-15-16x9.mp4 / -9x16.mp4       (15 s)
    ├── kambily-essai-voix-prompteur-16x9.mp4            (13 s, prompteur pour la comédienne)
    ├── kambily-voix-off-90s.srt / -15s.srt
    ├── audio/                                           (stems : voix, musique, SFX, mix — régénérables)
    └── planches/                                        (images clés, 16:9 et 9:16)
```

- **Visualiser :** ouvrir `animatic/index.html?format=16x9` (ou `9x16`, `&cut=15`, `&cues=1`, `&safe=1`) dans un navigateur ; un clic met en pause.
- **Rendre l'image :** `./render/all.sh`. **Sonoriser (voix+musique+SFX) :** `./render/mix.sh`. Nécessite Node 18+, Playwright, Chromium, ffmpeg, Python 3, numpy, soundfile, `kokoro-onnx` (+ modèle) et espeak-ng. Les stems WAV sont écrits dans `out/audio/`.
- **Remplacer la voix de synthèse par une comédienne :** déposer le nouvel enregistrement à la place de `out/audio/kambily-voix-master.wav` (48 kHz, mêmes départs de phrases, cf. §4.8) puis relancer `./render/mix.sh`. L'image ne change pas.
