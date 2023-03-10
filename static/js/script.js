// Cette fonction met à jour la valeur affichée de la longueur du tableau en fonction de la position du slider
function updateLength() {
    var value = document.getElementById("array-length").value;
    document.getElementById("array-length-value").innerHTML = value;
}

// Cette fonction est appelée lorsque la page est chargée
// Elle récupère la valeur du slider et appelle la fonction pour mettre à jour la valeur affichée
        window.onload = function() {
    var len = document.getElementById('array-length').value;
    updateLength(len);
}

// Cette fonction est appelée lors du chargement de la page de visualisation, elle cache le contenu et affiche l'icône de chargement
function loading() {
    document.getElementById("loading").style.display = "block";
    document.getElementById("content").style.display = "none";
}