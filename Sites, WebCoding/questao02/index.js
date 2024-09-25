const toggleButton = document.getElementById("toggle");
const body = document.body;


toggleButton.addEventListener('click', () => {
    body.classList.toggle('dark-mode');

    if (body.classList.contains('dark-mode')) {
        toggleButton.textContent = "Trocar para light mode";

    } else {
        toggleButton.textContent = "Trocar para dark mode";
    }

});