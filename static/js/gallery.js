
function openLightbox(imgUrl, title) {
    document.getElementById('lightboxImg').src = imgUrl;
    document.getElementById('lightboxCaption').innerHTML = title;
    document.getElementById('galleryLightbox').style.display = "block";
}

function closeLightbox() {
    document.getElementById('galleryLightbox').style.display = "none";
}

// Close on 'Esc' key
document.addEventListener('keydown', function(e) {
    if (e.key === "Escape") closeLightbox();
});