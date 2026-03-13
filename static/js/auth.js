document.querySelectorAll(".auth-form input").forEach(input => {

input.addEventListener("focus", () => {
input.style.borderColor = "#10b981";
});

input.addEventListener("blur", () => {
input.style.borderColor = "#d1d5db";
});

});