document.addEventListener('DOMContentLoaded', () => {
  const servicesAccordion = document.getElementById('servicesAccordion');

  if (!servicesAccordion) return;

  servicesAccordion.addEventListener('shown.bs.collapse', (e) => {
    const index = e.target.id.replace('service', '');
    document.querySelectorAll('.lottie-player').forEach(p => p.classList.remove('active'));
    const activePlayer = document.querySelector(`.lottie-player[data-index="${index}"]`);
    if (activePlayer) activePlayer.classList.add('active');
  });
});