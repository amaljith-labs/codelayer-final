/**
 * contactForm.js
 */

// 1. Toggle Chip selection using your .selected class
function toggleChip(el) {
    el.classList.toggle('selected');
}

document.addEventListener('DOMContentLoaded', function() {
    const contactForm = document.getElementById('contactForm');

    if (contactForm) {
        contactForm.addEventListener('submit', function(e) {
            e.preventDefault();

            const form = this;
            const submitBtn = document.getElementById('submitBtn');
            const successDiv = document.getElementById('formSuccess');

            // --- 10-DIGIT PHONE VALIDATION ---
            const phoneInput = form.querySelector('input[name="phone"]');
            const phoneValue = phoneInput.value.replace(/\s+/g, ''); // Remove spaces
            const phonePattern = /^\d{10}$/; // Exactly 10 digits

            if (!phonePattern.test(phoneValue)) {
                alert("Please enter a valid 10-digit mobile number.");
                phoneInput.focus();
                return;
            }

            // --- COLLECT MULTIPLE INTERESTS ---
            // We look specifically for the .selected class now
            let interests = [];
            document.querySelectorAll('.int-chip.selected').forEach(chip => {
                interests.push(chip.innerText.trim());
            });

            if (interests.length === 0) {
                alert("Please select at least one interest.");
                return;
            }

            // --- PREPARE DATA ---
            const formData = new FormData(form);
            formData.append('interests', interests.join(', '));

            if (typeof CSRF_TOKEN !== 'undefined') {
                formData.append('csrfmiddlewaretoken', CSRF_TOKEN);
            }

            // UI Feedback
            submitBtn.innerHTML = "Sending... <i class='bi bi-hourglass-split'></i>";
            submitBtn.disabled = true;

            fetch(window.location.href, {
                method: 'POST',
                body: formData,
                headers: { 'X-Requested-With': 'XMLHttpRequest' }
            })
            .then(response => response.json())
            .then(data => {
                if (data.status === 'success') {
                    form.style.display = 'none';
                    successDiv.style.display = 'block';
                } else {
                    alert("Error: " + data.message);
                    submitBtn.innerHTML = "Send Message <i class='bi bi-arrow-right'></i>";
                    submitBtn.disabled = false;
                }
            })
            .catch(error => {
                console.error('Error:', error);
                submitBtn.disabled = false;
            });
        });
    }
});