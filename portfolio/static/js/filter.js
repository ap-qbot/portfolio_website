document.addEventListener('DOMContentLoaded', function() {
    const categoryLinks = document.querySelectorAll('.nav-pills .nav-link');

    categoryLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            // Remove active class from all links
            categoryLinks.forEach(l => l.classList.remove('active'));
            // Add active class to clicked link
            this.classList.add('active');
        });
    });
});