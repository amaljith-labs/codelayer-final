document.addEventListener('DOMContentLoaded', function() {
    const landingForm = document.getElementById('landingPageForm');
    const successDiv = document.getElementById('formSuccess');

    if (landingForm) {
        landingForm.addEventListener('submit', function(e) {
            e.preventDefault();

            const submitBtn = document.getElementById('submitBtn');
            const formData = new FormData(this);

            // Disable button to prevent double submission
            submitBtn.disabled = true;
            submitBtn.innerHTML = '<span class="spinner-border spinner-border-sm"></span> Sending...';

            fetch('/capture-landing-lead/', { // This URL should match your urls.py path
                method: 'POST',
                body: formData,
                headers: {
                    'X-CSRFToken': formData.get('csrfmiddlewaretoken')
                }
            })
            .then(response => response.json())
            .then(data => {
                if (data.status === 'success') {
                    landingForm.style.display = 'none';
                    successDiv.style.display = 'block';
                } else {
                    alert("Error: " + data.message);
                    submitBtn.disabled = false;
                    submitBtn.innerHTML = 'Get Started Now <i class="bi bi-arrow-right"></i>';
                }
            })
            .catch(error => {
                console.error('Error:', error);
                submitBtn.disabled = false;
                submitBtn.innerHTML = 'Get Started Now <i class="bi bi-arrow-right"></i>';
            });
        });
    }
});