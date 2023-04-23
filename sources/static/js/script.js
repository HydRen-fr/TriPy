// Cette fonction permet de switcher entre données manuelles et aléatoires
function data_switch() {
    var toggle = document.getElementById("data-toggle");
    var values = document.getElementById("array-values");
    var length = document.getElementById("array-length");
    var text = document.getElementById("data-text");
    
    if (toggle.innerHTML === "<strong>Choisir les données</strong>") {
        toggle.innerHTML = "<strong>Générer aléatoirement</strong>";
        values.style.display = "block";
        values.required = true;
        values.pattern = "^(?:1[0-8][0-9]|[1-9][0-9]|[1-9]|190)(?: (?:1[0-8][0-9]|[1-9][0-9]|[1-9]|190)){0,15} ?$";
        length.style.display = "none";
        text.innerHTML = "Entiers séparés par des espaces | entre 1 et 190 | limité à 16 nombres";
        text.style.fontSize = "30px";
        document.getElementById("choix").value = "2";
        
    } else {
        toggle.innerHTML = "<strong>Choisir les données</strong>";
        values.style.display = "none";
        values.required = false;
        values.pattern = ".*";
        length.style.display = "block";
        text.innerHTML = "Taille des données (voir le bouton vert à gauche pour choisir les nombres)";
        text.style.fontSize = "26px";
        document.getElementById("choix").value = "1";
    }
}

// -------------------------------------------------------------------------

// Cette fonction est appelée lors du chargement de la page de visualisation, elle cache le contenu et affiche l'icône de chargement
function loading() {
    document.getElementById("loader").style.display = "block";
    document.getElementById("content").style.display = "none";
    document.querySelector('.button-container').style.display = "none";
}


function loading_2() {
    document.getElementById("loader-2").style.display = "block";
    document.getElementById("popup-comp").style.display = "none";
    document.querySelector(".compare-btn").style.display = "none";
}

// -------------------------------------------------------------------------

window.onload = function() {
  var modal = document.getElementById("monModal");
  var span = document.getElementsByClassName("close")[0];

  // Vérifie si le modal a déjà été affiché
  var isModalDisplayed = sessionStorage.getItem("isModalDisplayed");
  if (!isModalDisplayed) {
      modal.style.display = "flex";
      // Marque le modal comme étant affiché
      sessionStorage.setItem("isModalDisplayed", true);
  }

  span.onclick = function() {
      modal.style.display = "none";
  }

  window.onclick = function(event) {
      if (event.target == modal) {
          modal.style.display = "none";
      }
  }
}


// Récupération des pages et des boutons de navigation
var pages = document.querySelectorAll('.page');
var prevButton = document.getElementById('prev-page');
var nextButton = document.getElementById('next-page');
var currentPage = 0;

// Affichage de la page actuelle
function showPage(pageIndex) {
// Cacher toutes les pages
for (var i = 0; i < pages.length; i++) {
pages[i].classList.remove('active');
}
// Afficher la page actuelle
pages[pageIndex].classList.add('active');
// Mettre à jour le numéro de page actuelle
currentPage = pageIndex;
// Vérifier si la page actuelle est la première
if (currentPage === 0) {
prevButton.style.display = 'none';
} else {
prevButton.style.display = 'block';
}
// Vérifier si la page actuelle est la dernière
if (currentPage === pages.length - 1) {
nextButton.style.display = 'none';
} else {
nextButton.style.display = 'block';
}
}

// Navigation vers la page précédente
function prevPage() {
if (currentPage > 0) {
showPage(currentPage - 1);
}
}

// Navigation vers la page suivante
function nextPage() {
if (currentPage < pages.length - 1) {
showPage(currentPage + 1);
}
}

// Ajout des événements de clic pour les boutons de navigation
prevButton.addEventListener('click', prevPage);
nextButton.addEventListener('click', nextPage);

// Ajout des événements de touche pour la navigation avec les touches fléchées
document.addEventListener('keydown', function(event) {
if (event.keyCode === 37) {
// Touche gauche
prevPage();
} else if (event.keyCode === 39) {
// Touche droite
nextPage();
}
});

// Cacher le bouton prev à la première page
prevButton.style.display = 'none';
// Affichage de la première page au chargement de la page
showPage(0);



// -------------------------------------------------------------------------



// Test RegEx de textarea car ce n'est pas input donc pas de pattern possible
function testFunc() {
    var donnees_interactives_check = /^(\d{1,3}\s){1,398}\d{1,3}\s?$/;
    var val = document.getElementById('donnees-interactives').value;
    var lines = val.split('\n');
    for(var i = 0; i < lines.length; i++) {
      if(!lines[i].match(donnees_interactives_check)) {
        alert ('Suivez le format demandé dans le titre...');
        return false;
      } 
    }
    return true;
  }
  




