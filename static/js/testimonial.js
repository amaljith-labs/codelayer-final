document.addEventListener('DOMContentLoaded', () => {
  const track = document.getElementById('testimonialsTrack');
  const slides = document.querySelectorAll('.testimonial-slide');
  const dotsContainer = document.getElementById('testimonialDots');
  const prevBtn = document.getElementById('testimonialPrev');
  const nextBtn = document.getElementById('testimonialNext');

  let current = 0;

  // Slides visible per view
  function slidesVisible() {
    if (window.innerWidth <= 480) return 1;
    if (window.innerWidth <= 768) return 2;
    return 3;
  }

  const total = slides.length;

  // Build dots
  slides.forEach((_, i) => {
    const dot = document.createElement('button');
    dot.classList.add('t-dot');
    if (i === 0) dot.classList.add('active');
    dot.addEventListener('click', () => goTo(i));
    dotsContainer.appendChild(dot);
  });

  const dots = document.querySelectorAll('.t-dot');

  function goTo(index) {
    const visible = slidesVisible();
    const maxIndex = total - visible;
    current = Math.max(0, Math.min(index, maxIndex));

    // Calculate slide width including gap
    const slideWidth = slides[0].offsetWidth + 24;
    track.style.transform = `translateX(-${current * slideWidth}px)`;

    // Update dots
    dots.forEach((d, i) => d.classList.toggle('active', i === current));
  }

  prevBtn.addEventListener('click', () => goTo(current - 1));
  nextBtn.addEventListener('click', () => goTo(current + 1));

  // Recalculate on resize
  window.addEventListener('resize', () => goTo(current));

  // Equalise card heights
  function equaliseHeights() {
    const cards = document.querySelectorAll('.testimonial-card');
    cards.forEach(c => c.style.height = 'auto');
    let max = 0;
    cards.forEach(c => { if (c.offsetHeight > max) max = c.offsetHeight; });
    cards.forEach(c => c.style.height = max + 'px');
  }

  equaliseHeights();
  window.addEventListener('resize', equaliseHeights);
});