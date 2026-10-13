/* ==========================================================================
   VOIX OFF — SOURCE UNIQUE DU MINUTAGE (le montage est calé sur ces repères)
   a / b   : début / fin de la phrase (secondes, timeline du film)
   key     : mot porteur de l'idée ; keyAt = instant où il est prononcé
   sub     : false quand la phrase est déjà affichée mot pour mot à l'écran
             (on n'affiche pas deux fois le même texte dans la version muette)
   Ces minutages sont des CIBLES pour la comédienne (débit ≈ 2,5 mots/s).
   Après l'enregistrement : mesurer les vrais instants dans la prise retenue,
   corriger les valeurs ici, relancer le rendu — l'animation suit.
   ========================================================================== */
window.VO = {
  master: [
    { a: 0.7, b: 2.2, text: "Un produit ici…", key: "ici", keyAt: 1.6, sub: false },
    { a: 2.7, b: 4.6, text: "L'autre, à l'autre bout de la ville.", key: "l'autre bout", keyAt: 3.6, sub: false },
    { a: 6.9, b: 8.7, text: "Et si les boutiques venaient à toi ?", key: "venaient à toi", keyAt: 8.0, sub: false },
    { a: 9.4, b: 12.6, text: "Kambily, c'est la marketplace des boutiques de chez toi.", key: "de chez toi", keyAt: 12.0, sub: true },
    { a: 14.2, b: 16.8, text: "Tout commence par une envie.", key: "envie", keyAt: 16.2, sub: false },
    { a: 19.6, b: 22.4, text: "Des centaines de produits, des boutiques d'ici.", key: "boutiques d'ici", keyAt: 21.8, sub: true },
    { a: 23.0, b: 26.6, text: "Beauté, mode, high-tech : tu compares, tu choisis.", key: "tu choisis", keyAt: 26.0, sub: true },
    { a: 28.8, b: 31.6, text: "Sur chaque produit : le prix, et la boutique qui le vend.", key: "la boutique", keyAt: 30.6, sub: true },
    { a: 31.9, b: 35.2, text: "Pas reçu, cassé ou différent ? Kambily te protège.", key: "te protège", keyAt: 34.4, sub: true },
    { a: 38.2, b: 41.4, text: "Plusieurs boutiques…", key: "Plusieurs boutiques", keyAt: 40.4, sub: false },
    { a: 42.0, b: 44.4, text: "… un seul panier.", key: "un seul panier", keyAt: 43.6, sub: false },
    { a: 45.6, b: 49.0, text: "On te livre chez toi, à ton heure.", key: "chez toi", keyAt: 48.2, sub: true },
    { a: 49.4, b: 52.6, text: "Standard, ou express le jour même.", key: "express", keyAt: 51.8, sub: true },
    { a: 53.6, b: 57.0, text: "Tu paies comme tu veux : Orange Money, MTN, carte…", key: "comme tu veux", keyAt: 55.0, sub: true },
    { a: 57.4, b: 60.4, text: "… ou en espèces à la livraison.", key: "à la livraison", keyAt: 59.6, sub: true },
    { a: 61.6, b: 64.4, text: "Et voilà : c'est confirmé.", key: "confirmé", keyAt: 63.6, sub: false },
    { a: 68.0, b: 71.6, text: "Tu la suis étape par étape, jusqu'à ta porte.", key: "étape par étape", keyAt: 70.4, sub: true },
    { a: 74.0, b: 77.6, text: "Et ton colis ne se remet qu'avec ton code.", key: "ton code", keyAt: 77.0, sub: true },
    { a: 79.6, b: 82.0, text: "Vous avez une boutique ?", key: "boutique", keyAt: 81.2, sub: false },
    { a: 82.6, b: 85.0, text: "Vendez sur Kambily.", key: "Vendez sur Kambily", keyAt: 83.8, sub: false },
    { a: 85.6, b: 86.6, text: "Kambily.", key: "Kambily", keyAt: 85.9, sub: false },
    { a: 87.0, b: 89.6, text: "Les boutiques d'ici. Un seul panier.", key: "un seul panier", keyAt: 88.8, sub: false },
  ],
  "15": [
    { a: 0.3,  b: 2.6,  text: "Un produit ici, l'autre ailleurs.",               key: "là-bas",       keyAt: 2.0,  sub: false },
    { a: 2.9,  b: 5.8,  text: "Sur Kambily : plusieurs boutiques, un seul panier.", key: "un seul panier", keyAt: 5.3, sub: false },
    { a: 7.2,  b: 9.8,  text: "Et ton colis ne se remet qu'avec ton code.",     key: "ton code",     keyAt: 9.4,  sub: true },
    { a: 12.5, b: 13.0, text: "Kambily.",                                       key: "Kambily",      keyAt: 12.6, sub: false },
    { a: 13.2, b: 15.2, text: "Les boutiques d'ici. Un seul panier.",           key: "un seul panier", keyAt: 14.4, sub: false },
  ],
};
