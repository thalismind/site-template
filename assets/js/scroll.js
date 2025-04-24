document.addEventListener('DOMContentLoaded', function() {
    // Get the button element
    const scrollButton = document.getElementById('scroll-to-top');

    // Show the button when the user scrolls down 100px
    window.onscroll = function() {
        if (document.body.scrollTop > 100 || document.documentElement.scrollTop > 100) {
            scrollButton.style.display = 'block';
        } else {
            scrollButton.style.display = 'none';
        }
    };

    // Scroll to the top of the page when the button is clicked
    scrollButton.onclick = function() {
        window.scrollTo({ top: 0, behavior: 'smooth' });
    };
});
