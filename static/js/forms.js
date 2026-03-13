document.querySelectorAll(".form-fields input, .form-fields textarea, .form-fields select")
.forEach(field=>{
field.addEventListener("focus",()=>{
field.style.borderColor="#2563eb";
});
});
