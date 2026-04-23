function setFilter(dept, btn) {
  const jobs = document.querySelectorAll('.job-card');
  const buttons = document.querySelectorAll('.filter-btn');

  // Remove active class from all buttons
  buttons.forEach(b => b.classList.remove('active'));

  // Add active class to clicked button
  btn.classList.add('active');

  jobs.forEach(job => {
    const jobDept = job.getAttribute('data-dept');

    if (dept === 'all' || jobDept === dept) {
      job.style.display = 'flex'; // or 'block' depending on your layout
    } else {
      job.style.display = 'none';
    }
  });
}