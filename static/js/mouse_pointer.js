  const dot = document.querySelector('.cursor-dot');
  const ring = document.querySelector('.cursor-ring');

  let mouseX = 0, mouseY = 0;
  let ringX = 0, ringY = 0;

  window.addEventListener('mousemove', (e) => {
    mouseX = e.clientX;
    mouseY = e.clientY;

    // Dot follows instantly
    dot.style.left = mouseX + 'px';
    dot.style.top = mouseY + 'px';
  });

  // Ring follows with slight lag
  function animateRing() {
    ringX += (mouseX - ringX) * 0.12;
    ringY += (mouseY - ringY) * 0.12;
    ring.style.left = ringX + 'px';
    ring.style.top = ringY + 'px';
    requestAnimationFrame(animateRing);
  }
  animateRing();

  // Hover detection on interactive elements
  const hoverTargets = document.querySelectorAll(
    'a, button, .nav-link, .mega-menu-item, .odoo-tag, .stat-card, input, textarea, select'
  );

  hoverTargets.forEach(el => {
    el.addEventListener('mouseenter', () => {
      dot.classList.add('is-hovering');
      ring.classList.add('is-hovering');
    });
    el.addEventListener('mouseleave', () => {
      dot.classList.remove('is-hovering');
      ring.classList.remove('is-hovering');
    });
  });
