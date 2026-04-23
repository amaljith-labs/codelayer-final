function switchTab(index) {
    const tabs = document.querySelectorAll('.dd-tab');
    const panels = document.querySelectorAll('.dd-panel');

    // Remove active class from all tabs and panels
    tabs.forEach(tab => tab.classList.remove('active'));
    panels.forEach(panel => panel.classList.remove('active'));

    // Set clicked tab and corresponding panel to active
    tabs[index].classList.add('active');
    panels[index].classList.add('active');
}