document.addEventListener("DOMContentLoaded", function() {
    const surpriseBtn = document.getElementById("surpriseBtn");
    const birthdayContainer = document.getElementById("birthdayContainer");
    const surpriseContainer = document.getElementById("surpriseContainer");

    surpriseBtn.addEventListener("click", function() {
        birthdayContainer.style.display = "none";
        surpriseContainer.style.display = "block";
    });

    const balloonsContainer = document.getElementById("balloonsContainer");
    for (let i = 0; i < 20; i++) {
        const balloon = document.createElement("div");
        balloon.classList.add("balloon");
        balloon.style.left = `${Math.random() * 100}%`;
        balloonsContainer.appendChild(balloon);
    }
});
