# Site INGENIOS — Livraison développeur

Site statique multi-pages (HTML/CSS/JS vanilla, sans dépendance de build),
généré à partir de la maquette validée de la page d'accueil.

## Structure
- `index.html`, `a-propos.html`, `realisations.html`, `actualites.html`, `contact.html` — pages FR racine
- `expertise-audit-assistance-conseils/` — pôle 1 (hub + 4 pages d'audit + 6 sous-services)
- `expertise-technologie-digitale/` — pôle 2 (hub + 5 sous-services)
- `expertise-healthcare/` — pôle 3 (hub + 5 sous-services)
- `en/` — version anglaise : accueil, à propos, réalisations, actualités, contact, et une page
  de synthèse par pôle (les sous-pages détaillées ne sont pour l'instant qu'en français ;
  chaque page EN de pôle renvoie vers la version FR détaillée — traduction complète à prévoir)
- `assets/style.css` — feuille de style unique, fidèle à la maquette (couleurs, typographie,
  proportions, composants) — variables CSS en tête de fichier pour ajuster la charte
- `assets/main.js` — menu mobile, dropdown "Expertises", modale de contact rapide, formulaire
  de la page Contact, newsletter (Actualités)

## Régénérer le site
Le site est produit par un générateur Python (`generate.py` = gabarits, `content.py` = contenus
éditoriaux, `build.py` = assemblage). Pour régénérer après modification d'un contenu :
```
python3 build.py
```
Cela réécrit l'ensemble des fichiers HTML dans ce dossier à partir des gabarits.

## Points à finaliser côté développeur
- **Formulaires de contact** (page Contact + modale rapide) : simulation client-side côté front ;
  brancher sur l'API / CRM réel d'INGENIOS (voir commentaires `// NOTE développeur` dans `assets/main.js`).
- **Carte** de la page Contact : bloc `.map-box` à remplacer par une intégration Google Maps /
  OpenStreetMap (coordonnées : Tokoin, Lomé, TOGO).
- **Traduction anglaise complète** des pages de sous-services (actuellement FR uniquement).
- **Articles d'actualités** : les cartes de la page Actualités sont des exemples de structure,
  à remplacer par un vrai contenu (CMS ou fichiers Markdown).
- **Logo** : le symbole SVG `#mark` reprend le dessin des losanges de la maquette ; à remplacer
  par le fichier vectoriel officiel si disponible.
- **Liens réseaux sociaux** et mentions légales / politique de confidentialité (`href="#"`) à compléter.

## Charte respectée
Fond blanc, bleu institutionnel dominant (#062B4B / #0B4F7C), touche cyan tech (#0096CE),
vert santé numérique (#23893A / #82C42F), typographie Schibsted Grotesk, boutons et cartes
identiques à la maquette d'origine.

## Évolutions récentes
- **Héro (accueil)** : diaporama en fondu enchaîné de 3 illustrations (`assets/images/hero-*.jpg`), gabarit `_slider()` dans `build.py`, logique dans `assets/main.js`.
- **Section « quatre acteurs »** (`#acteurs`, accueil FR/EN) : consommateur, moyen de paiement (PSP FedaPay, Celtis, Moov), INGENIOS, fournisseur — gabarit `actors_section()` dans `build.py`. Textes à valider.
- **Actualités** : vignettes d'articles en illustrations vectorielles originales (`assets/images/news-*.svg`, une par thème : RH, cybersécurité, santé numérique) ; « Insights » retiré de l'intitulé français.
- **Pôle Audit (accueil)** : émoji 📚 à la place de l'icône balance (`pole_ico()` dans `build.py`).
- Images fournies en capture d'écran : remplacer par des fichiers haute définition et libres de droits avant mise en ligne.
