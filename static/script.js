// JavaScript functionality for Daria's Digest

// Function to navigate to an article
function navigateToArticle(articleId) {
    window.location.href = `/article/${articleId}`;
}

// Add smooth scrolling for better user experience
document.addEventListener('DOMContentLoaded', function() {
    // Add click animations to buttons
    const buttons = document.querySelectorAll('.blog-button, .back-button');
    buttons.forEach(button => {
        button.addEventListener('click', function(e) {
            // Add a subtle click effect
            this.style.transform = 'scale(0.95)';
            setTimeout(() => {
                this.style.transform = 'scale(1)';
            }, 150);
        });
    });

    // Add hover effects to article cards
    const articleCards = document.querySelectorAll('.article-card');
    articleCards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-5px)';
        });
        
        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0)';
        });
    });

    // Add loading animation
    document.body.style.opacity = '0';
    window.addEventListener('load', function() {
        document.body.style.transition = 'opacity 0.3s ease';
        document.body.style.opacity = '1';
    });
});