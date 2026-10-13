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
    { a: 0.6,  b: 1.8,  text: "Un produit ici…",                                key: "ici",          keyAt: 1.5,  sub: false },
    { a: 2.2,  b: 3.6,  text: "L'autre… là-bas.",                               key: "là-bas",       keyAt: 3.2,  sub: false },
    { a: 5.4,  b: 7.4,  text: "Et si les boutiques venaient à toi ?",           key: "venaient à toi", keyAt: 6.8, sub: false },
    { a: 9.8,  b: 12.2, text: "Sur Kambily, les boutiques d'ici ont leur vitrine.", key: "vitrine",   keyAt: 11.9, sub: true },
    { a: 12.5, b: 16.4, text: "Beauté, chaussures, électronique… tu compares, tu choisis.", key: "tu choisis", keyAt: 16.0, sub: true },
    { a: 17.9, b: 19.5, text: "Ce que tu aimes… tu l'ajoutes.",                 key: "ajoutes",      keyAt: 19.2, sub: true },
    { a: 24.0, b: 26.4, text: "Plusieurs boutiques. Un seul panier.",           key: "un seul panier", keyAt: 25.6, sub: false },
    { a: 29.7, b: 31.9, text: "Ton créneau. Ton moyen de paiement.",            key: "paiement",     keyAt: 31.5, sub: true },
    { a: 33.4, b: 34.4, text: "Et c'est confirmé.",                             key: "confirmé",     keyAt: 34.0, sub: true },
    { a: 36.0, b: 38.6, text: "Ton colis ne se remet qu'avec ton code.",        key: "ton code",     keyAt: 38.2, sub: true },
    { a: 41.8, b: 44.2, text: "Vous avez une boutique ? Rejoignez Kambily.",    key: "Rejoignez Kambily", keyAt: 43.4, sub: false },
    { a: 44.6, b: 45.4, text: "Écrivez-nous.",                                  key: "Écrivez-nous", keyAt: 44.8, sub: true },
    { a: 47.5, b: 48.1, text: "Kambily.",                                       key: "Kambily",      keyAt: 47.6, sub: false },
    { a: 48.4, b: 50.4, text: "Les boutiques d'ici. Un seul panier.",           key: "un seul panier", keyAt: 49.8, sub: false },
  ],
  "15": [
    { a: 0.3,  b: 2.4,  text: "Un produit ici… l'autre, là-bas.",               key: "là-bas",       keyAt: 2.0,  sub: false },
    { a: 2.9,  b: 5.8,  text: "Sur Kambily : plusieurs boutiques, un seul panier.", key: "un seul panier", keyAt: 5.3, sub: false },
    { a: 7.2,  b: 9.8,  text: "Et ton colis ne se remet qu'avec ton code.",     key: "ton code",     keyAt: 9.4,  sub: true },
    { a: 12.5, b: 13.0, text: "Kambily.",                                       key: "Kambily",      keyAt: 12.6, sub: false },
    { a: 13.2, b: 14.8, text: "Les boutiques d'ici. Un seul panier.",           key: "un seul panier", keyAt: 14.4, sub: false },
  ],
};
