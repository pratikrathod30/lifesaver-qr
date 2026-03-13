const cards = document.querySelectorAll(".feature-box, .workflow-step, .info-card");

cards.forEach(card => {

card.addEventListener("mouseenter", () => {
card.style.transform = "translateY(-6px)";
card.style.transition = "0.3s";
});

card.addEventListener("mouseleave", () => {
card.style.transform = "translateY(0)";
});

});