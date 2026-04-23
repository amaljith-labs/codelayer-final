///animated hero title

document.addEventListener("DOMContentLoaded", function() {
  const words = [
    "Intelligent Solutions",
    "Specialized ERPs",
    "Custom Software",
    "Unified Platforms",
    "Digital Transformation"
  ];

  let i = 0;
  const textElement = document.getElementById("typed-text");

  // Safety check to ensure element exists
  if (textElement) {
    setInterval(() => {
      // Step 1: Fade out
      textElement.classList.add("fade-hidden");

      setTimeout(() => {
        // Step 2: Change text while invisible
        i = (i + 1) % words.length;
        textElement.textContent = words[i];

        // Step 3: Fade back in
        textElement.classList.remove("fade-hidden");
      }, 600); // Matches the 0.6s CSS transition
    }, 4000); // Changes every 4 seconds
  }
});


///HERO SECTION PADDED

const hero = document.querySelector('.header');

window.addEventListener('scroll', () => {
  const scrollY = window.scrollY;
  const maxScroll = hero.offsetHeight;
  const progress = Math.min(scrollY / maxScroll, 1);

  const isDesktop = window.innerWidth >= 992;
  const maxMargin = isDesktop ? 240 : 60;
  const margin = progress * maxMargin;
  const radius = progress * 16;

  hero.style.margin = `0 ${margin}px`;
  hero.style.borderRadius = `${radius}px`;
  hero.style.overflow = 'hidden';
});

window.addEventListener('resize', () => {
  const isDesktop = window.innerWidth >= 992;
  const maxMargin = isDesktop ? 240 : 60;
  const scrollY = window.scrollY;
  const maxScroll = hero.offsetHeight;
  const progress = Math.min(scrollY / maxScroll, 1);

  hero.style.margin = `0 ${progress * maxMargin}px`;
});












///Text reveal section

const el = document.getElementById('scrollText');

  // Wrap each word in a span
  el.innerHTML = el.innerText
    .split(' ')
    .map(w => `<span class="word">${w}</span>`)
    .join(' ');

  const words = el.querySelectorAll('.word');

  window.addEventListener('scroll', () => {
    const elTop = el.getBoundingClientRect().top;
    const elBottom = el.getBoundingClientRect().bottom;
    const viewH = window.innerHeight;

    // How far we've scrolled through the element (0 to 1)
    const progress = 1 - (elBottom / (viewH + el.offsetHeight));

    const litCount = Math.floor(progress * words.length * 1.5);

    words.forEach((word, i) => {
      word.classList.toggle('lit', i < litCount);
    });
  });



// ── Count up animation ────────────────────────
const statNumbers = document.querySelectorAll('.stat-number');

const countUp = (el) => {
  const target = parseInt(el.textContent);
  const suffix = el.textContent.replace(/[0-9]/g, ''); // captures "+" or any suffix
  const duration = 1800;
  const steps = 60;
  const increment = target / steps;
  let current = 0;
  let step = 0;

  const timer = setInterval(() => {
    step++;
    current = Math.min(Math.round(increment * step), target);
    el.textContent = current + suffix;

    if (current >= target) {
      clearInterval(timer);
      el.classList.add('counted');
    }
  }, duration / steps);
};

const statObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      countUp(entry.target);
      statObserver.unobserve(entry.target); // run once only
    }
  });
}, { threshold: 0.5 });

statNumbers.forEach(el => statObserver.observe(el));



const container = document.querySelector('.marquee-container');
const content = document.querySelector('.marquee-content');
const bar = document.querySelector('.scroll-bar');

let isDown = false;
let startX;
let scrollLeft;

// Update Scrollbar Position
const syncBar = () => {
    const scrollPercentage = container.scrollLeft / (container.scrollWidth - container.clientWidth);
    bar.style.left = (scrollPercentage * 70) + "%"; // 70 to keep bar inside track
};

// Start Dragging
const startAction = (e) => {
    isDown = true;
    container.style.cursor = 'grabbing';
    // Pause animation when interacting
    content.style.animationPlayState = 'paused';
    startX = (e.pageX || e.touches[0].pageX) - container.offsetLeft;
    scrollLeft = container.scrollLeft;
};

// Stop Dragging
const stopAction = () => {
    isDown = false;
    container.style.cursor = 'grab';
    // Resume animation
    content.style.animationPlayState = 'running';
};

// Move logic
const moveAction = (e) => {
    if (!isDown) return;
    e.preventDefault();
    const x = (e.pageX || e.touches[0].pageX) - container.offsetLeft;
    const walk = (x - startX) * 2; // Sensitivity
    container.scrollLeft = scrollLeft - walk;
    syncBar();
};

// PC Listeners
container.addEventListener('mousedown', startAction);
container.addEventListener('mouseup', stopAction);
container.addEventListener('mouseleave', stopAction);
container.addEventListener('mousemove', moveAction);

// Mobile Listeners
container.addEventListener('touchstart', startAction);
container.addEventListener('touchend', stopAction);
container.addEventListener('touchmove', moveAction);

// Sync bar on scroll
container.addEventListener('scroll', syncBar);




///go to top

// Get the button
let mybutton = document.getElementById("myBtn");

// When the user scrolls down 20px from the top of the document, show the button
window.onscroll = function() {scrollFunction()};

function scrollFunction() {
  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    mybutton.style.display = "block";
  } else {
    mybutton.style.display = "none";
  }
}

        // When the user clicks on the button, scroll to the top of the document
        function topFunction() {
          document.body.scrollTop = 0;
          document.documentElement.scrollTop = 0;
        }
