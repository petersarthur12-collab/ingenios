#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Génère le site statique multi-pages INGENIOS à partir de la maquette validée."""
import os

ROOT = os.path.dirname(os.path.abspath(__file__))

LOGO_DEFS = """<svg width="0" height="0" style="position:absolute" aria-hidden="true">
  <defs>
    <symbol id="mark" viewBox="190 415 440 610">
      <polygon points="414,427 519,533 428,625 322,518" style="fill:var(--mark-navy)"/>
      <polygon points="322,518 402,600 286,721 203,639" fill="#23893A"/>
      <polygon points="519,533 617,632 525,724 428,625" fill="#0096CE"/>
      <polygon points="386,620 490,727 390,828 285,722" fill="#82C42F"/>
      <polygon points="201,813 287,725 405,845 330,942" style="fill:var(--mark-navy)"/>
      <polygon points="405,845 525,724 604,804 398,1011 330,942" style="fill:var(--mark-blue)"/>
    </symbol>
  </defs>
</svg>"""

ICONS = {
    "audit": '<svg viewBox="0 0 24 24"><path d="m16 16 3-8 3 8c-.87.65-1.92 1-3 1s-2.13-.35-3-1Z"/><path d="m2 16 3-8 3 8c-.87.65-1.92 1-3 1s-2.13-.35-3-1Z"/><path d="M7 21h10"/><path d="M12 3v18"/><path d="M3 7h2c2 0 5-1 7-2 2 1 5 2 7 2h2"/></svg>',
    "tech": '<svg viewBox="0 0 24 24"><rect width="16" height="16" x="4" y="4" rx="2"/><rect width="6" height="6" x="9" y="9" rx="1"/><path d="M15 2v2"/><path d="M15 20v2"/><path d="M2 15h2"/><path d="M2 9h2"/><path d="M20 15h2"/><path d="M20 9h2"/><path d="M9 2v2"/><path d="M9 20v2"/></svg>',
    "health": '<svg viewBox="0 0 24 24"><path d="M19 14c1.49-1.46 3-3.21 3-5.5A5.5 5.5 0 0 0 16.5 3c-1.76 0-3 .5-4.5 2-1.5-1.5-2.74-2-4.5-2A5.5 5.5 0 0 0 2 8.5c0 2.3 1.5 4.05 3 5.5l7 7Z"/><path d="M3.22 12H9.5l.5-1 2 4.5 2-7 1.5 3.5h5.27"/></svg>',
    "doc": '<svg viewBox="0 0 24 24"><path d="M14 3v4a1 1 0 0 0 1 1h4"/><path d="M17 21H7a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h7l5 5v11a2 2 0 0 1-2 2Z"/><path d="M9 13h6"/><path d="M9 17h6"/></svg>',
    "users": '<svg viewBox="0 0 24 24"><path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>',
    "grad": '<svg viewBox="0 0 24 24"><path d="M22 10 12 5 2 10l10 5 10-5Z"/><path d="M6 12v5c0 1.5 3 3 6 3s6-1.5 6-3v-5"/></svg>',
    "check": '<svg viewBox="0 0 24 24"><path d="M9 12l2 2 4-4"/><circle cx="12" cy="12" r="9"/></svg>',
    "hand": '<svg viewBox="0 0 24 24"><path d="M11 12h6l3 3-3 3h-6"/><path d="M11 6h4l3 3-3 3h-4"/><path d="M3 3v18"/></svg>',
    "mic": '<svg viewBox="0 0 24 24"><path d="M12 2a3 3 0 0 0-3 3v6a3 3 0 0 0 6 0V5a3 3 0 0 0-3-3Z"/><path d="M19 10v1a7 7 0 0 1-14 0v-1"/><path d="M12 18v4"/><path d="M8 22h8"/></svg>',
    "chart": '<svg viewBox="0 0 24 24"><path d="M3 3v18h18"/><path d="M7 15l4-5 3 3 5-7"/></svg>',
    "code": '<svg viewBox="0 0 24 24"><path d="m8 6-6 6 6 6"/><path d="m16 6 6 6-6 6"/></svg>',
    "data": '<svg viewBox="0 0 24 24"><ellipse cx="12" cy="5" rx="8" ry="3"/><path d="M4 5v14c0 1.66 3.58 3 8 3s8-1.34 8-3V5"/><path d="M4 12c0 1.66 3.58 3 8 3s8-1.34 8-3"/></svg>',
    "shield": '<svg viewBox="0 0 24 24"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10Z"/></svg>',
    "pulse": '<svg viewBox="0 0 24 24"><path d="M22 12h-4l-3 9L9 3l-3 9H2"/></svg>',
    "video": '<svg viewBox="0 0 24 24"><path d="m22 8-6 4 6 4V8Z"/><rect x="2" y="6" width="14" height="12" rx="2"/></svg>',
    "lock": '<svg viewBox="0 0 24 24"><rect x="3" y="11" width="18" height="11" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>',
    "folder": '<svg viewBox="0 0 24 24"><path d="M3 7a2 2 0 0 1 2-2h4l2 2h8a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2Z"/></svg>',
    "heart": '<svg viewBox="0 0 24 24"><path d="M20.8 4.6a5.5 5.5 0 0 0-7.8 0L12 5.6l-1-1a5.5 5.5 0 0 0-7.8 7.8l1 1L12 21l7.8-7.6 1-1a5.5 5.5 0 0 0 0-7.8Z"/></svg>',
    "pin": '<svg viewBox="0 0 24 24"><path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z"/><circle cx="12" cy="10" r="3"/></svg>',
    "phone": '<svg viewBox="0 0 24 24"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.3 1.8.6 2.7a2 2 0 0 1-.4 2.1L8 9.9a16 16 0 0 0 6 6l1.4-1.4a2 2 0 0 1 2.1-.4c.9.3 1.8.5 2.7.6a2 2 0 0 1 1.8 2Z"/></svg>',
    "mail": '<svg viewBox="0 0 24 24"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="m2 7 10 6 10-6"/></svg>',
    "card": '<svg viewBox="0 0 24 24"><rect x="2" y="5" width="20" height="14" rx="2"/><path d="M2 10h20"/><path d="M6 15h4"/></svg>',
    "briefcase": '<svg viewBox="0 0 24 24"><rect x="2" y="7" width="20" height="14" rx="2"/><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"/></svg>',
    "clock": '<svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 3"/></svg>',
}

STR = {
    "fr": dict(
        tagline="Innovation, expertise et transformation au service des organisations.",
        contact_cta="Nous contacter", discover="Découvrir", more="En savoir plus",
        home="Accueil", expertises="Expertises", about="À propos", works="Réalisations",
        news="Actualités", contact="Contact", related="Autres expertises du pôle",
        need_help="Un projet en tête ?", cta_generic="Parlons de votre projet",
        legal1="Mentions légales", legal2="Politique de confidentialité",
        addr="Tokoin, Lomé, TOGO",
    ),
    "en": dict(
        tagline="Innovation, expertise and transformation for high-performing organisations.",
        contact_cta="Contact us", discover="Discover", more="Learn more",
        home="Home", expertises="Expertise", about="About", works="Track record",
        news="Insights", contact="Contact", related="Other services in this practice",
        need_help="Have a project in mind?", cta_generic="Let's talk about your project",
        legal1="Legal notice", legal2="Privacy policy",
        addr="Tokoin, Lomé, TOGO",
    ),
}

def contact_modal(lang):
    L = STR[lang]
    if lang == "fr":
        return f"""
<div class="modal-overlay" id="contactOverlay" aria-hidden="true">
  <div class="modal-box" role="dialog" aria-modal="true" aria-labelledby="contactTitle">
    <button class="modal-close" id="contactClose" aria-label="Fermer">✕</button>
    <div id="contactFormWrap">
      <h3 id="contactTitle">{L['cta_generic']}</h3>
      <p class="sub">Décrivez-nous votre besoin, nous revenons vers vous rapidement.</p>
      <form id="contactForm" novalidate>
        <div class="field" id="f-nom"><label for="c-nom">Nom complet</label><input type="text" id="c-nom" name="nom" autocomplete="name"><span class="err-msg">Merci d'indiquer votre nom.</span></div>
        <div class="field" id="f-email"><label for="c-email">Email</label><input type="email" id="c-email" name="email" autocomplete="email"><span class="err-msg">Merci d'indiquer un email valide.</span></div>
        <input type="hidden" id="c-sujet" name="sujet">
        <div class="field" id="f-msg"><label for="c-msg">Votre message</label><textarea id="c-msg" name="message" rows="4"></textarea><span class="err-msg">Merci de décrire brièvement votre besoin.</span></div>
        <button type="submit" class="btn btn-primary" id="contactSubmit">Envoyer</button>
        <p class="form-status" id="contactStatus"></p>
      </form>
    </div>
    <div class="modal-success" id="contactSuccess" style="display:none">
      <div class="ico-ok"><svg viewBox="0 0 24 24"><path d="m20 6-11 11-5-5"/></svg></div>
      <h3>Message envoyé</h3><p class="sub">Merci, nous revenons vers vous très rapidement.</p>
      <button type="button" class="btn btn-outline" id="contactAgain" style="margin-top:22px">Envoyer un autre message</button>
    </div>
  </div>
</div>"""
    return f"""
<div class="modal-overlay" id="contactOverlay" aria-hidden="true">
  <div class="modal-box" role="dialog" aria-modal="true" aria-labelledby="contactTitle">
    <button class="modal-close" id="contactClose" aria-label="Close">✕</button>
    <div id="contactFormWrap">
      <h3 id="contactTitle">{L['cta_generic']}</h3>
      <p class="sub">Tell us about your needs and we'll get back to you shortly.</p>
      <form id="contactForm" novalidate>
        <div class="field" id="f-nom"><label for="c-nom">Full name</label><input type="text" id="c-nom" name="nom" autocomplete="name"><span class="err-msg">Please enter your name.</span></div>
        <div class="field" id="f-email"><label for="c-email">Email</label><input type="email" id="c-email" name="email" autocomplete="email"><span class="err-msg">Please enter a valid email.</span></div>
        <input type="hidden" id="c-sujet" name="sujet">
        <div class="field" id="f-msg"><label for="c-msg">Your message</label><textarea id="c-msg" name="message" rows="4"></textarea><span class="err-msg">Please briefly describe your needs.</span></div>
        <button type="submit" class="btn btn-primary" id="contactSubmit">Send</button>
        <p class="form-status" id="contactStatus"></p>
      </form>
    </div>
    <div class="modal-success" id="contactSuccess" style="display:none">
      <div class="ico-ok"><svg viewBox="0 0 24 24"><path d="m20 6-11 11-5-5"/></svg></div>
      <h3>Message sent</h3><p class="sub">Thank you, we'll be in touch very soon.</p>
      <button type="button" class="btn btn-outline" id="contactAgain" style="margin-top:22px">Send another message</button>
    </div>
  </div>
</div>"""


def nav_items(lang, base):
    L = STR[lang]
    if lang == "fr":
        p1, p2, p3 = "expertise-audit-assistance-conseils/index.html", "expertise-technologie-digitale/index.html", "expertise-healthcare/index.html"
        items = [
            ("index.html", L["home"], "accueil"),
        ]
        drop = [
            (p1, "Audit, Assistance & Conseils"),
            (p2, "Technologie & Transformation Digitale"),
            (p3, "Healthcare"),
        ]
        items2 = [
            ("a-propos.html", L["about"], "apropos"),
            ("realisations.html", L["works"], "realisations"),
            ("actualites.html", L["news"], "actualites"),
            ("contact.html", L["contact"], "contact"),
        ]
    else:
        items = [("index.html", L["home"], "accueil")]
        drop = [
            ("audit-assistance-advisory.html", "Audit, Assistance & Advisory"),
            ("technology-digital-transformation.html", "Technology & Digital Transformation"),
            ("healthcare.html", "Healthcare"),
        ]
        items2 = [
            ("about.html", L["about"], "apropos"),
            ("works.html", L["works"], "realisations"),
            ("insights.html", L["news"], "actualites"),
            ("contact.html", L["contact"], "contact"),
        ]
    return items, drop, items2


def header(lang, base, current, lang_links):
    """lang_links: dict {'fr': relative href from this page, 'en': relative href}"""
    L = STR[lang]
    nbase = "" if lang == "en" else base
    items, drop, items2 = nav_items(lang, base)
    links_html = ""
    for href, label, key in items:
        cls = "link current" if key == current else "link"
        links_html += f'<a class="{cls}" href="{nbase}{href}">{label}</a>\n'
    drop_html = '<div class="drop">' + "".join(f'<a href="{nbase}{h}">{lbl}</a>' for h, lbl in drop) + "</div>"
    exp_href = (nbase + "index.html#poles") if lang == "fr" else (nbase + drop[0][0])
    links_html += f'<div class="has-drop"><a class="link{" current" if current=="expertises" else ""}" href="{exp_href}">{L["expertises"]}</a>{drop_html}</div>\n'
    for href, label, key in items2:
        cls = "link current" if key == current else "link"
        links_html += f'<a class="{cls}" href="{nbase}{href}">{label}</a>\n'
    lang_sw = f"""<div class="lang-switch">
      <a href="{lang_links['fr']}" class="{'current' if lang=='fr' else ''}">FR</a>
      <a href="{lang_links['en']}" class="{'current' if lang=='en' else ''}">EN</a>
    </div>"""
    return f"""<header class="site">
  <div class="wrap nav">
    <a class="brand" href="{nbase}index.html" aria-label="INGENIOS">
      <svg viewBox="0 0 440 610"><use href="#mark"/></svg>
      <span>INGENIOS</span>
    </a>
    <nav class="menu" id="mainMenu" aria-label="Navigation principale">
      {links_html}
      {lang_sw}
      <a class="btn btn-primary btn-sm js-contact" href="#contact">{L['contact_cta']}</a>
    </nav>
    <button class="burger" id="burger" aria-label="Ouvrir le menu" aria-expanded="false"><span></span></button>
  </div>
</header>"""


def footer(lang, base):
    L = STR[lang]
    nbase = "" if lang == "en" else base
    if lang == "fr":
        useful = [("index.html", "Accueil"), ("expertise-audit-assistance-conseils/index.html", "Audit, Assistance & Conseils"),
                  ("expertise-technologie-digitale/index.html", "Technologie & Digital"), ("expertise-healthcare/index.html", "Healthcare"),
                  ("a-propos.html", "À propos"), ("realisations.html", "Réalisations"), ("contact.html", "Contact")]
        heading_coord, heading_liens, heading_follow = "Coordonnées", "Liens utiles", "Suivez-nous"
        rights = "© 2026 INGENIOS. Tous droits réservés."
    else:
        useful = [("index.html", "Home"), ("audit-assistance-advisory.html", "Audit, Assistance & Advisory"),
                  ("technology-digital-transformation.html", "Technology & Digital"), ("healthcare.html", "Healthcare"),
                  ("about.html", "About"), ("works.html", "Track record"), ("contact.html", "Contact")]
        heading_coord, heading_liens, heading_follow = "Contact details", "Useful links", "Follow us"
        rights = "© 2026 INGENIOS. All rights reserved."
    useful_html = "".join(f'<li><a href="{nbase}{h}">{lbl}</a></li>' for h, lbl in useful)
    return f"""<footer class="site">
  <div class="wrap">
    <div class="foot-grid">
      <div>
        <a class="brand" href="{nbase}index.html" aria-label="INGENIOS">
          <svg viewBox="0 0 440 610"><use href="#mark"/></svg><span>INGENIOS</span>
        </a>
        <p class="tag">{L['tagline']}</p>
      </div>
      <div>
        <h4>{heading_coord}</h4>
        <ul>
          <li>{L['addr']}</li>
          <li>Tel. Togo: <a href="tel:+22898912439">+228 98 91 24 39</a></li>
          <li>Bénin: <a href="tel:+2290147736495">+229 01 47 73 64 95</a> (Appel&nbsp;&amp;&nbsp;WhatsApp)</li>
          <li><a href="mailto:contact@ingenios.com">contact@ingenios.com</a></li>
        </ul>
      </div>
      <div><h4>{heading_liens}</h4><ul>{useful_html}</ul></div>
      <div>
        <h4>{heading_follow}</h4>
        <div class="socials">
          <a href="#" aria-label="LinkedIn">in</a>
          <a href="#" aria-label="Facebook">f</a>
          <a href="#" aria-label="WhatsApp"><svg viewBox="0 0 24 24"><path d="M21 11.5a8.4 8.4 0 0 1-12.4 7.4L3 20.5l1.7-5.4A8.4 8.4 0 1 1 21 11.5Z"/></svg></a>
        </div>
      </div>
    </div>
    <div class="legal">
      <span>{rights}</span>
      <nav aria-label="Informations légales"><a href="#">{L['legal1']}</a><a href="#">{L['legal2']}</a></nav>
    </div>
  </div>
</footer>"""


def page(lang, base, title, desc, current, body, lang_links):
    hreflang = f'<link rel="alternate" hreflang="fr" href="{lang_links["fr"]}"><link rel="alternate" hreflang="en" href="{lang_links["en"]}">' if lang_links else ""
    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title} · INGENIOS</title>
<meta name="description" content="{desc}">
{hreflang}
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Schibsted+Grotesk:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{base}assets/style.css">
</head>
<body id="top">
{LOGO_DEFS}
{header(lang, base, current, lang_links or {"fr": base + "index.html", "en": base + "index.html"})}
<main>
{body}
</main>
{footer(lang, base)}
{contact_modal(lang)}
<script src="{base}assets/main.js"></script>
</body>
</html>"""


def write(path, content):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)


def breadcrumb(base, trail):
    # trail: list of (label, href|None)
    parts = []
    for label, href in trail:
        if href:
            parts.append(f'<a href="{base}{href}">{label}</a>')
        else:
            parts.append(f"<span>{label}</span>")
    return f'<div class="wrap breadcrumb">{" <span class=\"sep\">/</span> ".join(parts)}</div>'


print("Gabarits chargés.")
