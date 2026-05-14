'use strict';

/* NAVBAR SCROLL */
const navbar = document.querySelector('.navbar');
window.addEventListener('scroll', () => {
  navbar.classList.toggle('scrolled', window.scrollY > 40);
}, { passive: true });

/* HAMBURGER */
const hamburger = document.querySelector('.hamburger');
const mobileMenu = document.querySelector('.mobile-menu');
if (hamburger && mobileMenu) {
  hamburger.addEventListener('click', () => {
    const open = mobileMenu.classList.toggle('open');
    hamburger.setAttribute('aria-expanded', open);
    const spans = hamburger.querySelectorAll('span');
    if (open) {
      spans[0].style.transform = 'translateY(7px) rotate(45deg)';
      spans[1].style.opacity = '0';
      spans[2].style.transform = 'translateY(-7px) rotate(-45deg)';
    } else {
      spans.forEach(s => { s.style.transform = ''; s.style.opacity = ''; });
    }
  });
  mobileMenu.querySelectorAll('a').forEach(a => {
    a.addEventListener('click', () => {
      mobileMenu.classList.remove('open');
      hamburger.setAttribute('aria-expanded', false);
      hamburger.querySelectorAll('span').forEach(s => { s.style.transform = ''; s.style.opacity = ''; });
    });
  });
}

/* TYPED EFFECT */
const typedEl = document.querySelector('.hero-title');
if (typedEl) {
  const phrases = [
    'AI & Machine Learning Engineer',
    'Deep Learning Practitioner',
    'NLP & LLM Specialist',
    'Computer Vision Engineer',
  ];
  let pi = 0, ci = 0, del = false, speed = 60;
  function type() {
    const cur = phrases[pi];
    if (!del) {
      typedEl.textContent = cur.slice(0, ++ci);
      if (ci === cur.length) { del = true; speed = 2200; } else speed = 60;
    } else {
      typedEl.textContent = cur.slice(0, --ci);
      if (ci === 0) { del = false; pi = (pi + 1) % phrases.length; speed = 300; } else speed = 35;
    }
    setTimeout(type, speed);
  }
  setTimeout(type, 800);
}

/* SKILL BAR ANIMATION */
const skillObserver = new IntersectionObserver(entries => {
  entries.forEach(entry => {
    if (!entry.isIntersecting) return;
    entry.target.querySelectorAll('.skill-fill').forEach(fill => {
      setTimeout(() => { fill.style.width = fill.dataset.pct + '%'; }, 100);
    });
    skillObserver.unobserve(entry.target);
  });
}, { threshold: 0.15 });
document.querySelectorAll('.skill-category').forEach(el => skillObserver.observe(el));

/* CARD TILT */
document.querySelectorAll('.project-card').forEach(card => {
  card.addEventListener('mousemove', e => {
    const r = card.getBoundingClientRect();
    const rx = ((e.clientY - r.top) / r.height - 0.5) * -8;
    const ry = ((e.clientX - r.left) / r.width - 0.5) * 8;
    card.style.transform = `perspective(800px) rotateX(${rx}deg) rotateY(${ry}deg) translateY(-6px)`;
  });
  card.addEventListener('mouseleave', () => { card.style.transform = ''; });
});

/* TOAST */
function showToast(type, title, msg) {
  let c = document.getElementById('toast-container');
  if (!c) { c = document.createElement('div'); c.id = 'toast-container'; document.body.appendChild(c); }
  const t = document.createElement('div');
  t.className = `toast toast-${type}`;
  t.innerHTML = `<div class="toast-icon">${type === 'success' ? '✅' : '❌'}</div>
    <div><div class="toast-title">${title}</div><div class="toast-msg">${msg}</div></div>`;
  c.appendChild(t);
  requestAnimationFrame(() => requestAnimationFrame(() => t.classList.add('show')));
  setTimeout(() => { t.classList.remove('show'); setTimeout(() => t.remove(), 400); }, 5000);
}

/* AJAX CONTACT FORM */
document.querySelectorAll('.contact-form').forEach(form => {
  form.addEventListener('submit', async e => {
    e.preventDefault();
    const btn = form.querySelector('.form-submit');
    const orig = btn.innerHTML;
    btn.innerHTML = '<span>Sending…</span>';
    btn.disabled = true;
    try {
      const res = await fetch(form.action || window.location.href, {
        method: 'POST',
        body: new FormData(form),
        headers: { 'X-Requested-With': 'XMLHttpRequest' },
      });
      const data = await res.json();
      if (data.success) {
        showToast('success', 'Message Sent! 🎉', "I'll get back to you within 24 hours.");
        form.reset();
      } else {
        showToast('error', 'Please check your inputs', 'All required fields must be filled.');
      }
    } catch {
      showToast('error', 'Error', 'Please email me at smdshoyab07@gmail.com');
    } finally {
      btn.innerHTML = orig;
      btn.disabled = false;
    }
  });
});

/* AUTO DISMISS DJANGO MESSAGES */
document.querySelectorAll('.toast.show').forEach(t => {
  setTimeout(() => { t.classList.remove('show'); setTimeout(() => t.remove(), 400); }, 4500);
});
