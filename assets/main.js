// INGENIOS — comportements partagés du site
(function () {
  // Menu mobile
  var burger = document.getElementById('burger');
  var menu = document.getElementById('mainMenu');
  if (burger && menu) {
    burger.addEventListener('click', function () {
      var open = menu.classList.toggle('open');
      burger.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
    menu.querySelectorAll('a').forEach(function (a) {
      a.addEventListener('click', function () { menu.classList.remove('open'); });
    });
  }

  // Modale de contact rapide (accessible depuis tous les boutons "Nous contacter")
  var overlay = document.getElementById('contactOverlay');
  if (overlay) {
    var closeBtn = document.getElementById('contactClose');
    var form = document.getElementById('contactForm');
    var formWrap = document.getElementById('contactFormWrap');
    var success = document.getElementById('contactSuccess');
    var status = document.getElementById('contactStatus');
    var submitBtn = document.getElementById('contactSubmit');

    function openModal(subject) {
      overlay.classList.add('open');
      overlay.setAttribute('aria-hidden', 'false');
      document.body.style.overflow = 'hidden';
      formWrap.style.display = '';
      success.style.display = 'none';
      status.className = 'form-status';
      status.textContent = '';
      if (subject) {
        var sujetField = document.getElementById('c-sujet');
        if (sujetField) sujetField.value = subject;
      }
    }
    function closeModal() {
      overlay.classList.remove('open');
      overlay.setAttribute('aria-hidden', 'true');
      document.body.style.overflow = '';
    }
    document.querySelectorAll('.js-contact').forEach(function (btn) {
      btn.addEventListener('click', function (e) {
        e.preventDefault();
        openModal(btn.getAttribute('data-subject'));
      });
    });
    if (closeBtn) closeBtn.addEventListener('click', closeModal);
    overlay.addEventListener('click', function (e) { if (e.target === overlay) closeModal(); });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape' && overlay.classList.contains('open')) closeModal(); });

    function setError(id, on) {
      var el = document.getElementById(id);
      if (el) el.classList.toggle('error', on);
    }
    if (form) {
      form.addEventListener('submit', function (e) {
        e.preventDefault();
        var nom = document.getElementById('c-nom').value.trim();
        var email = document.getElementById('c-email').value.trim();
        var msg = document.getElementById('c-msg').value.trim();
        var emailOk = /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
        setError('f-nom', !nom);
        setError('f-email', !emailOk);
        setError('f-msg', !msg);
        if (!nom || !emailOk || !msg) return;

        submitBtn.disabled = true;
        submitBtn.textContent = '…';
        // NOTE développeur : point d'intégration à brancher sur l'API / CRM d'INGENIOS
        // (endpoint REST, service d'emailing, etc.). Simulation locale ci-dessous.
        setTimeout(function () {
          formWrap.style.display = 'none';
          success.style.display = '';
          submitBtn.disabled = false;
        }, 500);
      });
    }
    var againBtn = document.getElementById('contactAgain');
    if (againBtn) {
      againBtn.addEventListener('click', function () {
        form.reset();
        ['f-nom', 'f-email', 'f-msg'].forEach(function (id) { setError(id, false); });
        formWrap.style.display = '';
        success.style.display = 'none';
      });
    }
  }

  // Formulaire de la page Contact (dédiée)
  var pageForm = document.getElementById('pageContactForm');
  if (pageForm) {
    pageForm.addEventListener('submit', function (e) {
      e.preventDefault();
      var statusEl = document.getElementById('pageFormStatus');
      var btn = document.getElementById('pageFormSubmit');
      btn.disabled = true;
      // NOTE développeur : brancher ici l'appel API réel (POST vers le backend INGENIOS).
      setTimeout(function () {
        pageForm.style.display = 'none';
        document.getElementById('pageFormSuccess').style.display = '';
      }, 500);
    });
  }

  // Newsletter (Actualités)
  var nl = document.getElementById('newsletterForm');
  if (nl) {
    nl.addEventListener('submit', function (e) {
      e.preventDefault();
      var btn = nl.querySelector('button');
      btn.textContent = '✓ Inscrit(e)';
      btn.disabled = true;
    });
  }

  // Marqueur JS (active les animations d'apparition, sans casser le rendu si JS désactivé)
  document.documentElement.classList.add('js');

  // Héro : diaporama en fondu enchaîné (défilement automatique toujours actif ; seul le zoom est retiré si l'utilisateur réduit les animations)
  var slider = document.querySelector('[data-slider]');
  if (slider) {
    var slides = slider.querySelectorAll('.slide');
    var dots = slider.querySelectorAll('.dot');
    var idx = 0, timer = null;
    var show = function (n) {
      idx = (n + slides.length) % slides.length;
      slides.forEach(function (s, i) { s.classList.toggle('is-active', i === idx); });
      dots.forEach(function (d, i) { d.classList.toggle('is-active', i === idx); });
    };
    var start = function () { if (!timer) timer = setInterval(function () { show(idx + 1); }, 5200); };
    var stop = function () { clearInterval(timer); timer = null; };
    dots.forEach(function (d, i) { d.addEventListener('click', function () { show(i); stop(); start(); }); });
    slider.addEventListener('mouseenter', stop);
    slider.addEventListener('mouseleave', start);
    document.addEventListener('visibilitychange', function () { document.hidden ? stop() : start(); });
    start();
  }

  // Section des acteurs : apparition progressive au défilement
  var actors = document.querySelector('.actors');
  if (actors) {
    if ('IntersectionObserver' in window) {
      var io = new IntersectionObserver(function (entries) {
        entries.forEach(function (en) { if (en.isIntersecting) { actors.classList.add('in-view'); io.disconnect(); } });
      }, { threshold: 0.2 });
      io.observe(actors);
    } else { actors.classList.add('in-view'); }
  }
})();
