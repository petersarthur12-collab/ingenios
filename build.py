# -*- coding: utf-8 -*-
import generate as g
import content as c

FR_ROOT_TO_EN = {  # nom fichier racine FR -> nom fichier racine EN
    "index.html": "index.html",
    "a-propos.html": "about.html",
    "realisations.html": "works.html",
    "actualites.html": "insights.html",
    "contact.html": "contact.html",
}

def ll_root(fr_file):
    en_file = FR_ROOT_TO_EN[fr_file]
    return {"fr": fr_file, "en": f"en/{en_file}"}

def ll_pole(fr_current_in_folder, en_hub_file):
    return {"fr": fr_current_in_folder, "en": f"../en/{en_hub_file}"}

def ll_en(en_file, fr_target):
    return {"fr": f"../{fr_target}", "en": en_file}


def _slider(lang):
    """Diaporama du héro (accueil) : fondu enchaîné entre les 3 illustrations."""
    if lang == "fr":
        slides = [("hero-audit-conseil.jpg", "Équipe en réunion d'audit analysant des graphiques sur une tablette", "Audit &amp; Conseils", "var(--blue)"),
                  ("hero-cybersecurite.jpg", "Interface numérique de cybersécurité avec cadenas et icônes connectées", "Technologie &amp; Digital", "var(--cyan)"),
                  ("hero-sante-numerique.jpg", "Soignant présentant un dossier médical électronique sur tablette", "Healthcare", "var(--green)")]
        label = "Illustrations de nos trois domaines d'expertise"
        dots = ["Audit et conseils", "Technologie et digital", "Healthcare"]
    else:
        slides = [("hero-audit-conseil.jpg", "Team in an audit meeting reviewing charts on a tablet", "Audit &amp; Advisory", "var(--blue)"),
                  ("hero-cybersecurite.jpg", "Digital cybersecurity interface with padlock and connected icons", "Technology &amp; Digital", "var(--cyan)"),
                  ("hero-sante-numerique.jpg", "Healthcare worker showing an electronic medical record on a tablet", "Healthcare", "var(--green)")]
        label = "Illustrations of our three practices"
        dots = ["Audit and advisory", "Technology and digital", "Healthcare"]
    pre = "" if lang == "fr" else "../"
    figs = ""
    for i, (f, alt, cap, col) in enumerate(slides):
        prio = 'fetchpriority="high"' if i == 0 else 'loading="eager"'
        figs += f"""
        <figure class="slide{' is-active' if i == 0 else ''}">
          <img src="{pre}assets/images/{f}" alt="{alt}" width="720" height="480" {prio}>
          <figcaption><i style="background:{col}"></i>{cap}</figcaption>
        </figure>"""
    dts = "".join(f'<button type="button" class="dot{" is-active" if i == 0 else ""}" aria-label="{d}"></button>' for i, d in enumerate(dots))
    return f"""<div class="hero-slider" data-slider role="group" aria-roledescription="carousel" aria-label="{label}">{figs}
        <div class="slider-dots">{dts}</div>
      </div>"""


SLIDERS = {"fr": _slider("fr"), "en": _slider("en")}

def pole_ico(p):
    """Icône du pôle ; l'Audit utilise l'émoji 📚 (bibliothèque) à la place de la balance."""
    if p["icon"] == "audit":
        return '<div class="ico ico-emoji" aria-hidden="true">📚</div>'
    return f'<div class="ico">{g.ICONS[p["icon"]]}</div>'

def actors_section(lang):
    if lang == "fr":
        head = ("Un écosystème à quatre acteurs", "Chaque service repose sur quatre rôles complémentaires. Voici qui fait quoi, de la demande jusqu'à la réalisation du service.")
        items = [
            ("users", "Consommateur du service", "Il exprime son besoin, choisit la prestation qui lui convient et suit sa réalisation en toute transparence.", "Demande"),
            ("card", "Moyen de paiement", "Des prestataires de services de paiement (PSP) sécurisent chaque transaction.", "Règlement"),
            ("mark", "INGENIOS", "Le tiers de confiance : il met en relation, coordonne les échanges et garantit la qualité et le suivi du service de bout en bout.", "Coordination"),
            ("briefcase", "Fournisseur de service", "Le professionnel ou la structure qui réalise la prestation selon les engagements définis.", "Réalisation"),
        ]
        psp_lbl, flow = "PSP partenaires", "Du besoin au service rendu : un parcours simple, sécurisé et suivi."
    else:
        head = ("A four-actor ecosystem", "Every service relies on four complementary roles. Here is who does what, from the initial request to delivery.")
        items = [
            ("users", "Service consumer", "They state their need, choose the right service and follow its delivery with full transparency.", "Request"),
            ("card", "Payment method", "Payment service providers (PSPs) secure every transaction.", "Payment"),
            ("mark", "INGENIOS", "The trusted third party: it connects the parties, coordinates exchanges and ensures quality and end-to-end follow-up.", "Coordination"),
            ("briefcase", "Service provider", "The professional or organisation that delivers the service according to the agreed commitments.", "Delivery"),
        ]
        psp_lbl, flow = "Partner PSPs", "From need to delivered service: a simple, secure and tracked journey."
    cards = ""
    for i, (ic, title, desc, step) in enumerate(items):
        svg = '<svg viewBox="0 0 440 610" aria-hidden="true"><use href="#mark"/></svg>' if ic == "mark" else g.ICONS[ic]
        extra = f'<div class="psp-list" aria-label="{psp_lbl}"><span>FedaPay</span><span>Celtis</span><span>Moov</span></div>' if ic == "card" else ""
        hub = " is-hub" if ic == "mark" else ""
        cards += f"""
        <li class="actor{hub}" style="--i:{i}">
          <span class="actor-step">{i+1} · {step}</span>
          <div class="actor-ico{' mark' if ic == 'mark' else ''}">{svg}</div>
          <h3>{title}</h3><p>{desc}</p>{extra}
        </li>"""
    return f"""<section class="actors" id="acteurs">
    <div class="wrap">
      <div class="section-head"><h2>{head[0]}</h2><p>{head[1]}</p></div>
      <ol class="actors-flow">{cards}
      </ol>
      <p class="actors-note">{flow}</p>
    </div>
  </section>"""

ACTORS_HTML = {"fr": actors_section("fr"), "en": actors_section("en")}

# ---------------------------------------------------------------- ACCUEIL FR
def build_home_fr():
    SLIDER_FR = SLIDERS['fr']; ACTORS = ACTORS_HTML['fr']
    poles_cards = ""
    for p in c.POLES:
        lst = p["categories"] if p["categories"] else p["services"]
        li = "".join(f"<li>{it[1]}</li>" for it in lst[:6])
        poles_cards += f"""
        <article class="pole {p['css']}">
          {pole_ico(p)}
          <h3>{p['name']}</h3>
          <p>{p['tagline']}</p>
          <ul>{li}</ul>
          <a class="more" href="{p['slug']}/index.html">Découvrir</a>
        </article>"""
    body = f"""
  <div class="hero">
    <div class="wrap hero-grid">
      <div>
        <h1>Innovation, expertise et transformation au service des organisations.</h1>
        <p class="lead"><strong>INGENIOS</strong> accompagne les entreprises et les institutions dans l'amélioration de leur fonctionnement, de l'audit de leur organisation jusqu'à leur transformation numérique.</p>
        <div class="actions">
          <a class="btn btn-primary" href="#poles">Découvrir nos domaines d'expertise</a>
          <a class="btn btn-outline js-contact" href="#contact">Nous contacter</a>
        </div>
      </div>
      {SLIDER_FR}
    </div>
  </div>

  <section id="poles" style="padding-top:24px">
    <div class="wrap">
      <div class="section-head">
        <h2>Domaines d'expertise</h2>
        <p>Trois domaines d'expertise complémentaires pour répondre à chaque étape de la vie de votre organisation.</p>
      </div>
      <div class="poles-grid">{poles_cards}
      </div>
    </div>
  </section>

  {ACTORS}

  <section class="surface" id="apropos-extrait">
    <div class="wrap about-grid">
      <div>
        <h2>À propos</h2>
        <div class="txt"><p>INGENIOS est une structure d'expertise et de conseils, spécialisée dans l'accompagnement des organisations dans l'optimisation de leur fonctionnement et l'augmentation de leur productivité. À la croisée de l'Expertise Juridique, du Développement RH, de l'Administration et de l'Innovation Technologique, nous apportons une expertise adaptée aux réalités de chaque structure.</p></div>
        <a class="btn btn-outline" href="a-propos.html">En savoir plus sur INGENIOS</a>
      </div>
      <div class="facts">
        <dl>
          <div class="fact"><dt>Notre métier</dt><dd>Audit, assistance et conseils, technologie et Healthcare</dd></div>
          <div class="fact"><dt>Nos domaines</dt><dd>Expertise Juridique et RH, Innovation Technologique et Santé</dd></div>
          <div class="fact"><dt>Nos interlocuteurs</dt><dd>Entreprises, institutions et ONG</dd></div>
          <div class="fact"><dt>Implantation</dt><dd>Tokoin, Lomé, TOGO</dd></div>
        </dl>
      </div>
    </div>
  </section>

  <section class="approach" id="approche">
    <div class="wrap">
      <div class="section-head"><h2>Notre approche</h2><p>Quatre engagements qui guident chacune de nos missions.</p></div>
      <div class="approach-grid">
        <div class="step">{g.ICONS['check']}<h3>Expertise</h3><p>Analyser. Comprendre. Conseiller.<br>Une expertise pluridisciplinaire au service de vos enjeux.</p></div>
        <div class="step">{g.ICONS['data']}<h3>Innovation</h3><p>Des outils, méthodes et solutions numériques conçus pour simplifier les processus et renforcer l'efficacité de vos équipes.</p></div>
        <div class="step">{g.ICONS['users']}<h3>Accompagnement</h3><p>Un interlocuteur présent de l'analyse à la mise en œuvre, au plus près de vos équipes.</p></div>
        <div class="step">{g.ICONS['chart']}<h3>Impact</h3><p>Des diagnostics minutieux et des recommandations concrètes, jugés à leur effet sur la performance de votre structure.</p></div>
      </div>
    </div>
  </section>

  <section id="realisations-extrait">
    <div class="wrap">
      <div class="section-head"><h2>Ils nous font confiance</h2><p>Quelques repères sur nos interventions récentes.</p></div>
      <div class="stats-row">
        <div class="stat"><b>12+</b><span>ans d'expérience cumulée</span></div>
        <div class="stat"><b>3</b><span>domaines d'expertise intégrés</span></div>
        <div class="stat"><b>2</b><span>pays d'intervention (Togo, Bénin)</span></div>
        <div class="stat"><b>360°</b><span>accompagnement, de l'audit au digital</span></div>
      </div>
      <div style="margin-top:32px"><a class="btn btn-outline" href="realisations.html">Voir nos réalisations</a></div>
    </div>
  </section>

  <section class="cta" id="contact">
    <div class="wrap">
      <div class="cta-panel">
        <svg class="deco" viewBox="0 0 400 600" fill="none" stroke="#fff" stroke-opacity=".16" stroke-width="2" aria-hidden="true">
          <rect x="120" y="60" width="200" height="200" transform="rotate(45 220 160)"/>
          <rect x="150" y="220" width="200" height="200" transform="rotate(45 250 320)"/>
          <rect x="60" y="300" width="160" height="160" transform="rotate(45 140 380)"/>
        </svg>
        <div>
          <h2>Vous avez un projet ? Construisons la solution ensemble.</h2>
          <p>Décrivez-nous votre besoin : nous revenons vers vous rapidement pour en discuter.</p>
          <a class="btn js-contact" href="contact.html">Parlons de votre projet</a>
        </div>
      </div>
    </div>
  </section>"""
    return g.page("fr", "", "Accueil", "INGENIOS — audit, assistance & conseils, technologie et santé numérique.", "accueil", body, ll_root("index.html"))


# ---------------------------------------------------------------- HUB DE PÔLE FR
def build_pole_hub_fr(pole):
    base = "../"
    cat_html = ""
    if pole["categories"]:
        cards = "".join(f"""
        <article class="service-card">
          <h3>{title}</h3><p>{desc}</p>
          <a class="more" href="{slug}.html">Découvrir cet audit →</a>
        </article>""" for slug, title, desc, bullets in pole["categories"])
        cat_html = f"""
  <section style="padding-top:8px">
    <div class="wrap">
      <div class="section-head"><h2>Nos catégories d'audit</h2><p>Quatre angles d'analyse pour un diagnostic complet de votre organisation.</p></div>
      <div class="cards-grid">{cards}
      </div>
    </div>
  </section>"""
    serv_cards = "".join(f"""
        <article class="service-card">
          <h3>{title}</h3><p>{desc}</p>
          <a class="more" href="{slug}.html">{'Découvrir' if True else ''} →</a>
        </article>""" for slug, title, icon, desc, bullets in pole["services"])
    body = f"""
  {g.breadcrumb(base, [("Accueil", "index.html"), (pole['name'], None)])}
  <div class="page-hero {pole['css']}">
    <div class="wrap">
      <span class="eyebrow">Domaine d'expertise</span>
      <h1>{pole['name']}</h1>
      <p class="lead">{pole['intro']}</p>
      <div class="actions"><a class="btn btn-primary js-contact" href="#contact" data-subject="{pole['name']}">Parler de mon projet</a></div>
    </div>
  </div>
  {cat_html}
  <section style="padding-top:{'0' if cat_html else '8px'}">
    <div class="wrap">
      <div class="section-head"><h2>Nos autres expertises</h2><p>{'Au-delà de l’audit, notre équipe intervient sur l’ensemble du cycle RH, juridique et organisationnel.' if pole['categories'] else 'Un accompagnement complet, du cadrage stratégique à la mise en œuvre opérationnelle.'}</p></div>
      <div class="cards-grid">{serv_cards}
      </div>
    </div>
  </section>
  <section class="cta" id="contact">
    <div class="wrap">
      <div class="cta-panel">
        <div><h2>Un besoin dans ce domaine ?</h2><p>Décrivez-nous votre contexte : notre équipe revient vers vous rapidement.</p>
        <a class="btn js-contact" href="../contact.html" data-subject="{pole['name']}">Parlons de votre projet</a></div>
      </div>
    </div>
  </section>"""
    ll = ll_pole("index.html", {"expertise-audit-assistance-conseils": "audit-assistance-advisory.html",
                                 "expertise-technologie-digitale": "technology-digital-transformation.html",
                                 "expertise-healthcare": "healthcare.html"}[pole["slug"]])
    return g.page("fr", base, pole["name"], pole["tagline"], "expertises", body, ll)


# ---------------------------------------------------------------- SOUS-PAGE DÉTAIL FR (audit / service)
def build_detail_fr(pole, slug, title, icon_key, desc, bullets, family_label):
    base = "../"
    siblings = pole["categories"] if any(s[0] == slug for s in pole["categories"]) else pole["services"]
    others = [s for s in siblings if s[0] != slug]
    icon_svg = g.ICONS.get(icon_key, g.ICONS["check"])
    others_html = "".join(f'<li><a href="{s[0]}.html">{s[1]}</a></li>' for s in others[:6])
    bullets_html = "".join(f"<li>{b}</li>" for b in bullets)
    body = f"""
  {g.breadcrumb(base, [("Accueil", "index.html"), (pole['name'], f"{pole['slug']}/index.html"), (title, None)])}
  <div class="page-hero {pole['css']}">
    <div class="wrap">
      <span class="eyebrow">{family_label} · {pole['name']}</span>
      <h1>{title}</h1>
      <p class="lead">{desc}</p>
      <div class="actions"><a class="btn btn-primary js-contact" href="#contact" data-subject="{title}">{STR_MORE_FR}</a></div>
    </div>
  </div>
  <section style="padding-top:0">
    <div class="wrap detail-grid">
      <div>
        <div class="detail-block">
          <h2>Notre approche</h2>
          <p>Nos équipes interviennent avec méthode et pragmatisme, en s'appuyant sur une connaissance fine des réalités opérationnelles, juridiques et humaines de votre organisation.</p>
        </div>
        <div class="detail-block">
          <h2>Ce que nous faisons</h2>
          <ul class="bullets">{bullets_html}</ul>
        </div>
      </div>
      <aside class="side-card">
        <h4>{pole['name']}</h4>
        <ul>{others_html}</ul>
        <a class="btn btn-primary js-contact" href="#contact" data-subject="{title}">Demander un devis</a>
      </aside>
    </div>
  </section>
  <section class="cta" id="contact">
    <div class="wrap">
      <div class="cta-panel">
        <div><h2>Discutons de votre besoin</h2><p>Un échange de 20 minutes suffit pour cadrer votre demande.</p>
        <a class="btn js-contact" href="../contact.html" data-subject="{title}">Parlons de votre projet</a></div>
      </div>
    </div>
  </section>"""
    ll = ll_pole(f"{slug}.html", {"expertise-audit-assistance-conseils": "audit-assistance-advisory.html",
                                   "expertise-technologie-digitale": "technology-digital-transformation.html",
                                   "expertise-healthcare": "healthcare.html"}[pole["slug"]])
    return g.page("fr", base, title, desc, "expertises", body, ll)

STR_MORE_FR = "Parler de mon projet"

# ---------------------------------------------------------------- À PROPOS FR
def build_about_fr():
    team = [("FE", "Direction générale", "Pilotage stratégique et développement des activités d'INGENIOS."),
            ("RH", "Pôle Audit, Assistance & Conseils", "Audit organisationnel, RH, juridique et accompagnement des équipes."),
            ("TD", "Pôle Technologie & Healthcare", "Conseil digital, développement de solutions et santé numérique.")]
    team_html = "".join(f"""<div class="team-card"><div class="avatar">{i}</div><h4>{t}</h4><p>{d}</p></div>""" for i, t, d in team)
    body = f"""
  {g.breadcrumb("", [("Accueil", "index.html"), ("À propos", None)])}
  <div class="page-hero">
    <div class="wrap">
      <span class="eyebrow">À propos</span>
      <h1>Une structure d'expertise au service des organisations</h1>
      <p class="lead">INGENIOS accompagne entreprises, institutions et ONG dans l'optimisation de leur fonctionnement et l'augmentation de leur productivité, à la croisée du droit, des ressources humaines, de l'administration et de l'innovation technologique.</p>
    </div>
  </div>
  <section style="padding-top:0">
    <div class="wrap about-grid">
      <div>
        <h2>Notre mission</h2>
        <div class="txt">
          <p>Notre ambition est de simplifier, structurer et faire progresser les organisations, en plaçant l'expertise, l'innovation et l'impact au centre de chacune de nos interventions.</p>
          <p>Nous intervenons aussi bien sur des missions d'audit et de conseil classiques que sur des projets de transformation digitale et de santé numérique, avec la même exigence de rigueur et de résultat.</p>
        </div>
      </div>
      <div class="facts">
        <dl>
          <div class="fact"><dt>Notre métier</dt><dd>Audit, assistance et conseils, technologie et Healthcare</dd></div>
          <div class="fact"><dt>Nos domaines</dt><dd>Expertise Juridique et RH, Innovation Technologique et Santé</dd></div>
          <div class="fact"><dt>Nos interlocuteurs</dt><dd>Entreprises, institutions et ONG</dd></div>
          <div class="fact"><dt>Implantation</dt><dd>Tokoin, Lomé, TOGO</dd></div>
        </dl>
      </div>
    </div>
  </section>
  <section class="surface">
    <div class="wrap">
      <div class="section-head"><h2>Notre organisation</h2><p>Une équipe pluridisciplinaire organisée autour de nos trois domaines d'expertise.</p></div>
      <div class="team-grid">{team_html}</div>
    </div>
  </section>
  <section class="approach">
    <div class="wrap">
      <div class="section-head"><h2>Nos valeurs</h2><p>Ce qui guide chacune de nos interventions, au quotidien.</p></div>
      <div class="approach-grid">
        <div class="step">{g.ICONS['check']}<h3>Rigueur</h3><p>Des méthodes éprouvées et une exigence constante de qualité.</p></div>
        <div class="step">{g.ICONS['heart']}<h3>Intégrité</h3><p>Une relation de confiance fondée sur la transparence et l'éthique professionnelle.</p></div>
        <div class="step">{g.ICONS['users']}<h3>Proximité</h3><p>Un accompagnement humain, au plus près des réalités de chaque structure.</p></div>
        <div class="step">{g.ICONS['data']}<h3>Innovation</h3><p>Une veille constante pour proposer des solutions actuelles et pertinentes.</p></div>
      </div>
    </div>
  </section>
  <section class="cta" id="contact">
    <div class="wrap"><div class="cta-panel"><div><h2>Envie d'en savoir plus ?</h2><p>Échangeons sur votre organisation et vos priorités.</p>
      <a class="btn js-contact" href="contact.html">Parlons de votre projet</a></div></div></div>
  </section>"""
    return g.page("fr", "", "À propos", "INGENIOS : mission, valeurs et organisation.", "apropos", body, ll_root("a-propos.html"))


# ---------------------------------------------------------------- RÉALISATIONS FR
def build_works_fr():
    cases = [
        ("Audit, Assistance & Conseils", "Audit organisationnel d'un groupe multi-activités", "Diagnostic complet de la gouvernance et des processus RH, avec plan d'action priorisé sur 12 mois."),
        ("Technologie & Transformation Digitale", "Digitalisation des processus RH d'une PME", "Déploiement d'outils numériques pour automatiser le recrutement, l'évaluation et la formation."),
        ("Healthcare", "Accompagnement d'une structure de soins", "Mise en place d'un dossier patient informatisé et sensibilisation des équipes soignantes."),
        ("Audit, Assistance & Conseils", "Recrutement de cadres pour une institution", "Sourcing, évaluation et intégration de profils clés en moins de 8 semaines."),
    ]
    cases_html = "".join(f"""<article class="case-card"><span class="tag">{tag}</span><h3>{title}</h3><p>{desc}</p></article>""" for tag, title, desc in cases)
    body = f"""
  {g.breadcrumb("", [("Accueil", "index.html"), ("Réalisations", None)])}
  <div class="page-hero">
    <div class="wrap">
      <span class="eyebrow">Réalisations</span>
      <h1>Des interventions concrètes, au service de nos clients</h1>
      <p class="lead">Un aperçu représentatif de nos missions récentes, dans nos trois domaines d'expertise.</p>
    </div>
  </div>
  <section style="padding-top:0">
    <div class="wrap">
      <div class="stats-row">
        <div class="stat"><b>12+</b><span>ans d'expérience cumulée</span></div>
        <div class="stat"><b>3</b><span>domaines d'expertise intégrés</span></div>
        <div class="stat"><b>2</b><span>pays d'intervention</span></div>
        <div class="stat"><b>360°</b><span>de l'audit au digital</span></div>
      </div>
    </div>
  </section>
  <section style="padding-top:0">
    <div class="wrap"><div class="case-grid">{cases_html}</div></div>
  </section>
  <section class="cta" id="contact">
    <div class="wrap"><div class="cta-panel"><div><h2>Votre projet pourrait être le prochain</h2><p>Parlons de vos enjeux et de la façon dont nous pouvons vous accompagner.</p>
      <a class="btn js-contact" href="contact.html">Parlons de votre projet</a></div></div></div>
  </section>"""
    return g.page("fr", "", "Réalisations", "Références et missions représentatives d'INGENIOS.", "realisations", body, ll_root("realisations.html"))


# ---------------------------------------------------------------- ACTUALITÉS FR
def build_news_fr():
    posts = [
        ("12 sept. 2026", "Pourquoi structurer sa fonction RH avant de digitaliser", "Les prérequis organisationnels d'une transformation digitale réussie.", "news-rh-structure.svg", "Organigramme illustrant la structuration de la fonction RH"),
        ("28 août 2026", "Cybersécurité : les fondamentaux pour les PME", "Cinq réflexes simples pour réduire les risques numériques de votre structure.", "news-cybersecurite.svg", "Bouclier et cadenas illustrant la cybersécurité"),
        ("14 juil. 2026", "Santé numérique : ce que change le dossier patient informatisé", "Comment la digitalisation améliore la coordination des soins.", "news-sante-numerique.svg", "Tablette affichant un dossier patient informatisé"),
    ]
    cards = "".join(f"""<article class="news-card"><div class="thumb"><img src="assets/images/{img}" alt="{alt}" loading="lazy"></div><div class="body"><span class="date">{d}</span><h3>{t}</h3><p>{s}</p><a class="more" href="#">Lire l'article →</a></div></article>""" for d, t, s, img, alt in posts)
    body = f"""
  {g.breadcrumb("", [("Accueil", "index.html"), ("Actualités", None)])}
  <div class="page-hero">
    <div class="wrap">
      <span class="eyebrow">Actualités</span>
      <h1>Nos analyses et prises de position</h1>
      <p class="lead">Retrouvez nos publications sur l'audit, la transformation digitale et la santé numérique.</p>
    </div>
  </div>
  <section style="padding-top:0"><div class="wrap"><div class="news-grid">{cards}</div></div></section>
  <section style="padding-top:0">
    <div class="wrap">
      <div class="newsletter">
        <div><h3 style="font-size:20px;font-weight:700">Recevez nos publications</h3><p style="margin-top:6px;color:var(--muted)">Une sélection de nos analyses, directement par email.</p></div>
        <form id="newsletterForm"><input type="email" required placeholder="Votre email"><button class="btn btn-primary" type="submit">S'inscrire</button></form>
      </div>
    </div>
  </section>"""
    return g.page("fr", "", "Actualités", "Analyses et publications d'INGENIOS.", "actualites", body, ll_root("actualites.html"))


# ---------------------------------------------------------------- CONTACT FR
def build_contact_fr():
    body = f"""
  {g.breadcrumb("", [("Accueil", "index.html"), ("Contact", None)])}
  <div class="page-hero">
    <div class="wrap">
      <span class="eyebrow">Contact</span>
      <h1>Parlons de votre projet</h1>
      <p class="lead">Une question, un besoin d'audit, de recrutement ou de transformation digitale ? Notre équipe vous répond rapidement.</p>
    </div>
  </div>
  <section style="padding-top:0">
    <div class="wrap contact-grid">
      <div class="contact-info">
        <div class="item"><div class="ico">{g.ICONS['pin']}</div><div><h4>Adresse</h4><p>Tokoin, Lomé, TOGO</p></div></div>
        <div class="item"><div class="ico">{g.ICONS['phone']}</div><div><h4>Téléphone</h4><p>Togo : <a href="tel:+22898912439">+228 98 91 24 39</a></p><p>Bénin : <a href="tel:+2290147736495">+229 01 47 73 64 95</a> (Appel &amp; WhatsApp)</p></div></div>
        <div class="item"><div class="ico">{g.ICONS['mail']}</div><div><h4>Email</h4><p><a href="mailto:contact@ingenios.com">contact@ingenios.com</a></p></div></div>
        <div class="item"><div class="ico">{g.ICONS['clock']}</div><div><h4>Disponibilité</h4><p>Lundi – Vendredi, 8h – 18h (GMT)</p></div></div>
        <div class="channels">
          <a class="btn btn-outline btn-sm" href="tel:+22898912439">Appeler (Togo)</a>
          <a class="btn btn-outline btn-sm" href="https://wa.me/22901477364" target="_blank" rel="noopener">WhatsApp</a>
          <a class="btn btn-outline btn-sm" href="mailto:contact@ingenios.com">Envoyer un email</a>
        </div>
        <div class="map-box">Carte interactive — à intégrer par le développeur (Google Maps / OpenStreetMap) : Tokoin, Lomé, TOGO.</div>
      </div>
      <div class="form-card">
        <form id="pageContactForm" novalidate>
          <h3 style="font-size:22px;font-weight:700">Envoyez-nous un message</h3>
          <div class="form-row">
            <div class="field"><label for="p-nom">Nom complet</label><input type="text" id="p-nom" required></div>
            <div class="field"><label for="p-email">Email</label><input type="email" id="p-email" required></div>
          </div>
          <div class="form-row">
            <div class="field"><label for="p-tel">Téléphone (optionnel)</label><input type="tel" id="p-tel"></div>
            <div class="field"><label for="p-sujet">Domaine concerné</label>
              <select id="p-sujet">
                <option>Audit, Assistance &amp; Conseils</option>
                <option>Technologie &amp; Transformation Digitale</option>
                <option>Healthcare</option>
                <option>Autre demande</option>
              </select>
            </div>
          </div>
          <div class="field"><label for="p-msg">Votre message</label><textarea id="p-msg" rows="5" required></textarea></div>
          <button type="submit" class="btn btn-primary" id="pageFormSubmit">Envoyer le message</button>
          <p class="form-status">Champs marqués requis. Réponse sous 48h ouvrées.</p>
        </form>
        <div class="form-success" id="pageFormSuccess" style="display:none">
          <div class="ico-ok"><svg viewBox="0 0 24 24"><path d="m20 6-11 11-5-5"/></svg></div>
          <h3 style="font-size:22px;font-weight:700">Message envoyé</h3>
          <p style="margin-top:8px;color:var(--muted)">Merci, notre équipe revient vers vous très rapidement.</p>
        </div>
      </div>
    </div>
  </section>"""
    return g.page("fr", "", "Contact", "Contactez INGENIOS — Tokoin, Lomé, TOGO.", "contact", body, ll_root("contact.html"))


# ---------------------------------------------------------------- EN : HOME / HUBS / PAGES
def build_home_en():
    SLIDER_EN = SLIDERS['en']; ACTORS = ACTORS_HTML['en']
    cards = "".join(f"""
        <article class="pole {p['css']}">{pole_ico(p)}<h3>{p['name']}</h3><p>{p['tagline']}</p>
        <ul>{''.join(f"<li>{i}</li>" for i in p['items'][:6])}</ul>
        <a class="more" href="{p['slug']}">Discover</a></article>""" for p in c.POLES_EN)
    body = f"""
  <div class="hero"><div class="wrap hero-grid">
    <div><h1>Innovation, expertise and transformation for high-performing organisations.</h1>
      <p class="lead"><strong>INGENIOS</strong> helps businesses and institutions improve how they operate — from organisational audit through to digital transformation.</p>
      <div class="actions"><a class="btn btn-primary" href="#poles">Explore our practices</a><a class="btn btn-outline js-contact" href="#contact">Contact us</a></div>
    </div>
    {SLIDER_EN}
  </div></div>
  <section id="poles" style="padding-top:24px"><div class="wrap">
    <div class="section-head"><h2>Areas of expertise</h2><p>Three complementary practices to support every stage of your organisation's growth.</p></div>
    <div class="poles-grid">{cards}</div>
  </div></section>
  {ACTORS}
  <section class="surface"><div class="wrap about-grid">
    <div><h2>About</h2><div class="txt"><p>INGENIOS is an advisory firm helping organisations optimise how they operate and increase productivity, at the crossroads of legal expertise, HR development, administration and technology innovation.</p></div>
    <a class="btn btn-outline" href="about.html">Learn more about INGENIOS</a></div>
    <div class="facts"><dl>
      <div class="fact"><dt>What we do</dt><dd>Audit, assistance & advisory, technology and Healthcare</dd></div>
      <div class="fact"><dt>Our focus</dt><dd>Legal & HR expertise, Technology & Health innovation</dd></div>
      <div class="fact"><dt>Who we serve</dt><dd>Businesses, institutions and NGOs</dd></div>
      <div class="fact"><dt>Based in</dt><dd>Tokoin, Lomé, TOGO</dd></div>
    </dl></div>
  </div></section>
  <section class="cta" id="contact"><div class="wrap"><div class="cta-panel">
    <div><h2>Have a project in mind? Let's build the solution together.</h2><p>Tell us about your needs — we'll get back to you quickly.</p>
    <a class="btn js-contact" href="contact.html">Let's talk about your project</a></div>
  </div></div></section>"""
    return g.page("en", "../", "Home", "INGENIOS — audit, assistance & advisory, technology and digital health.", "accueil", body, ll_en("index.html", "index.html"))


def build_pole_hub_en(p):
    base = "../"
    items_html = "".join(f"<li>{i}</li>" for i in p["items"])
    body = f"""
  {g.breadcrumb(base, [("Home", "index.html"), (p['name'], None)])}
  <div class="page-hero {p['css']}"><div class="wrap">
    <span class="eyebrow">Area of expertise</span><h1>{p['name']}</h1><p class="lead">{p['intro']}</p>
    <div class="actions"><a class="btn btn-primary js-contact" href="#contact" data-subject="{p['name']}">Talk about my project</a></div>
  </div></div>
  <section style="padding-top:0"><div class="wrap">
    <div class="section-head"><h2>What we cover</h2><p>An overview of our services in this practice.</p></div>
    <div class="side-card" style="max-width:640px"><ul>{items_html}</ul></div>
    <p style="margin-top:28px;color:var(--muted);font-size:15px">Detailed service pages are currently available in French — <a href="../expertise-{'audit-assistance-conseils' if 'Audit' in p['name'] else ('technologie-digitale' if 'Technology' in p['name'] else 'healthcare')}/index.html" style="color:var(--link);font-weight:600">view the French version</a> or contact us for an English briefing.</p>
  </div></section>
  <section class="cta" id="contact"><div class="wrap"><div class="cta-panel">
    <div><h2>Need support in this area?</h2><p>Tell us about your context — our team will get back to you quickly.</p>
    <a class="btn js-contact" href="../en/contact.html" data-subject="{p['name']}">Let's talk about your project</a></div>
  </div></div></section>"""
    fr_map = {"audit-assistance-advisory.html": "expertise-audit-assistance-conseils/index.html",
              "technology-digital-transformation.html": "expertise-technologie-digitale/index.html",
              "healthcare.html": "expertise-healthcare/index.html"}
    ll = ll_en(p["slug"], fr_map[p["slug"]])
    return g.page("en", base, p["name"], p["tagline"], "expertises", body, ll)


def build_about_en():
    body = f"""
  {g.breadcrumb("", [("Home", "index.html"), ("About", None)])}
  <div class="page-hero"><div class="wrap">
    <span class="eyebrow">About</span><h1>An advisory firm for high-performing organisations</h1>
    <p class="lead">INGENIOS supports businesses, institutions and NGOs in optimising their operations and increasing productivity — across legal, HR, administrative and technology dimensions.</p>
  </div></div>
  <section style="padding-top:0"><div class="wrap about-grid">
    <div><h2>Our mission</h2><div class="txt"><p>We simplify, structure and grow organisations, placing expertise, innovation and impact at the heart of every engagement.</p></div></div>
    <div class="facts"><dl>
      <div class="fact"><dt>What we do</dt><dd>Audit, assistance & advisory, technology and Healthcare</dd></div>
      <div class="fact"><dt>Our focus</dt><dd>Legal & HR expertise, Technology & Health innovation</dd></div>
      <div class="fact"><dt>Who we serve</dt><dd>Businesses, institutions and NGOs</dd></div>
      <div class="fact"><dt>Based in</dt><dd>Tokoin, Lomé, TOGO</dd></div>
    </dl></div>
  </div></section>
  <section class="cta" id="contact"><div class="wrap"><div class="cta-panel">
    <div><h2>Want to know more?</h2><p>Let's discuss your organisation and priorities.</p><a class="btn js-contact" href="contact.html">Let's talk about your project</a></div>
  </div></div></section>"""
    return g.page("en", "../", "About", "INGENIOS: mission and focus areas.", "apropos", body, ll_en("about.html", "a-propos.html"))


def build_works_en():
    cases = [("Audit, Assistance & Advisory", "Organisational audit for a multi-business group", "Full review of governance and HR processes, with a prioritised 12-month action plan."),
             ("Technology & Digital Transformation", "HR process digitisation for an SME", "Deployment of digital tools to automate recruitment, evaluation and training."),
             ("Healthcare", "Support for a healthcare facility", "Rollout of an electronic patient record and staff awareness training.")]
    cards = "".join(f"""<article class="case-card"><span class="tag">{t}</span><h3>{ti}</h3><p>{d}</p></article>""" for t, ti, d in cases)
    body = f"""
  {g.breadcrumb("", [("Home", "index.html"), ("Track record", None)])}
  <div class="page-hero"><div class="wrap"><span class="eyebrow">Track record</span><h1>Real engagements, real impact</h1>
  <p class="lead">A representative sample of our recent work across our three practices.</p></div></div>
  <section style="padding-top:0"><div class="wrap"><div class="case-grid">{cards}</div></div></section>
  <section class="cta" id="contact"><div class="wrap"><div class="cta-panel"><div><h2>Your project could be next</h2><p>Let's discuss your challenges.</p>
  <a class="btn js-contact" href="contact.html">Let's talk about your project</a></div></div></div></section>"""
    return g.page("en", "../", "Track record", "INGENIOS references and case studies.", "realisations", body, ll_en("works.html", "realisations.html"))


def build_news_en():
    posts = [("Sep 12, 2026", "Why structure HR before you digitise", "The organisational prerequisites for a successful digital transformation.", "news-rh-structure.svg", "Organisation chart illustrating HR structuring"),
             ("Aug 28, 2026", "Cybersecurity basics for SMEs", "Five simple steps to reduce your organisation's digital risk.", "news-cybersecurite.svg", "Shield and padlock illustrating cybersecurity")]
    cards = "".join(f"""<article class="news-card"><div class="thumb"><img src="../assets/images/{img}" alt="{alt}" loading="lazy"></div><div class="body"><span class="date">{d}</span><h3>{t}</h3><p>{s}</p><a class="more" href="#">Read more →</a></div></article>""" for d, t, s, img, alt in posts)
    body = f"""
  {g.breadcrumb("", [("Home", "index.html"), ("Insights", None)])}
  <div class="page-hero"><div class="wrap"><span class="eyebrow">Insights</span><h1>Our latest thinking</h1>
  <p class="lead">Perspectives on audit, digital transformation and digital health.</p></div></div>
  <section style="padding-top:0"><div class="wrap"><div class="news-grid">{cards}</div></div></section>"""
    return g.page("en", "../", "Insights", "INGENIOS insights and publications.", "actualites", body, ll_en("insights.html", "actualites.html"))


def build_contact_en():
    body = f"""
  {g.breadcrumb("", [("Home", "index.html"), ("Contact", None)])}
  <div class="page-hero"><div class="wrap"><span class="eyebrow">Contact</span><h1>Let's talk about your project</h1>
  <p class="lead">A question about audit, recruitment or digital transformation? Our team responds quickly.</p></div></div>
  <section style="padding-top:0"><div class="wrap contact-grid">
    <div class="contact-info">
      <div class="item"><div class="ico">{g.ICONS['pin']}</div><div><h4>Address</h4><p>Tokoin, Lomé, TOGO</p></div></div>
      <div class="item"><div class="ico">{g.ICONS['phone']}</div><div><h4>Phone</h4><p>Togo: <a href="tel:+22898912439">+228 98 91 24 39</a></p><p>Benin: <a href="tel:+2290147736495">+229 01 47 73 64 95</a> (Call &amp; WhatsApp)</p></div></div>
      <div class="item"><div class="ico">{g.ICONS['mail']}</div><div><h4>Email</h4><p><a href="mailto:contact@ingenios.com">contact@ingenios.com</a></p></div></div>
      <div class="channels">
        <a class="btn btn-outline btn-sm" href="tel:+22898912439">Call (Togo)</a>
        <a class="btn btn-outline btn-sm" href="https://wa.me/22901477364" target="_blank" rel="noopener">WhatsApp</a>
        <a class="btn btn-outline btn-sm" href="mailto:contact@ingenios.com">Send an email</a>
      </div>
      <div class="map-box">Interactive map — to be integrated by the developer (Google Maps / OpenStreetMap): Tokoin, Lomé, TOGO.</div>
    </div>
    <div class="form-card">
      <form id="pageContactForm" novalidate>
        <h3 style="font-size:22px;font-weight:700">Send us a message</h3>
        <div class="form-row"><div class="field"><label for="p-nom">Full name</label><input type="text" id="p-nom" required></div>
        <div class="field"><label for="p-email">Email</label><input type="email" id="p-email" required></div></div>
        <div class="field"><label for="p-msg">Your message</label><textarea id="p-msg" rows="5" required></textarea></div>
        <button type="submit" class="btn btn-primary" id="pageFormSubmit">Send message</button>
        <p class="form-status">Required fields. We reply within 48 business hours.</p>
      </form>
      <div class="form-success" id="pageFormSuccess" style="display:none">
        <div class="ico-ok"><svg viewBox="0 0 24 24"><path d="m20 6-11 11-5-5"/></svg></div>
        <h3 style="font-size:22px;font-weight:700">Message sent</h3><p style="margin-top:8px;color:var(--muted)">Thank you, our team will be in touch shortly.</p>
      </div>
    </div>
  </div></section>"""
    return g.page("en", "../", "Contact", "Contact INGENIOS — Tokoin, Lomé, TOGO.", "contact", body, ll_en("contact.html", "contact.html"))


# ================================================================ BUILD
def run():
    g.write("index.html", build_home_fr())
    g.write("a-propos.html", build_about_fr())
    g.write("realisations.html", build_works_fr())
    g.write("actualites.html", build_news_fr())
    g.write("contact.html", build_contact_fr())

    for p in c.POLES:
        g.write(f"{p['slug']}/index.html", build_pole_hub_fr(p))
        family = "Audit" if p["slug"].endswith("conseils") else ("Technologie" if "technologie" in p["slug"] else "Healthcare")
        for slug, title, desc, bullets in p["categories"]:
            g.write(f"{p['slug']}/{slug}.html", build_detail_fr(p, slug, title, "audit", desc, bullets, "Audit"))
        for slug, title, icon, desc, bullets in p["services"]:
            g.write(f"{p['slug']}/{slug}.html", build_detail_fr(p, slug, title, icon, desc, bullets, "Service"))

    g.write("en/index.html", build_home_en())
    g.write("en/about.html", build_about_en())
    g.write("en/works.html", build_works_en())
    g.write("en/insights.html", build_news_en())
    g.write("en/contact.html", build_contact_en())
    for p in c.POLES_EN:
        g.write(f"en/{p['slug']}", build_pole_hub_en(p))

    print("Site généré avec succès.")

if __name__ == "__main__":
    run()
