document.addEventListener('DOMContentLoaded', function() {
    // Get all video buttons
    const videoButtons = document.querySelectorAll('.video-btn');
    const videoModal = document.getElementById('videoModal');

    if (videoModal) {
        // Handle video modal events
        videoModal.addEventListener('show.bs.modal', function (event) {
            const button = event.relatedTarget;
            const videoId = button.getAttribute('data-video-id');
            const iframeSrc = `https://www.youtube.com/embed/${videoId}?autoplay=1`;
            const modalIframe = this.querySelector('iframe');
            modalIframe.setAttribute('src', iframeSrc);
        });

        // Clear iframe source when modal is closed
        videoModal.addEventListener('hide.bs.modal', function () {
            const modalIframe = this.querySelector('iframe');
            modalIframe.setAttribute('src', '');
        });
    }
});
