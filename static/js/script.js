function updateValue() {
    var value = document.getElementById("array-length").value;
    document.getElementById("array-length-value").innerHTML = value;
}

        // Récupère la valeur du slider au chargement de la page
        window.onload = function() {
    var value = document.getElementById('array-length').value;
    updateValue(value);
}

function loading() {
    document.getElementById("loading").style.display = "block";
    document.getElementById("content").style.display = "none";
}