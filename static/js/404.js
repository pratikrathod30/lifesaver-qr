document.addEventListener("DOMContentLoaded", () => {

const code = document.querySelector(".error-code");

code.style.opacity = "0";
code.style.transform = "translateY(20px)";

setTimeout(() => {
code.style.transition = "0.6s";
code.style.opacity = "1";
code.style.transform = "translateY(0)";
}, 200);

});