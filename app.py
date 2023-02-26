import algorithm
from flask import Flask, render_template, request, redirect, url_for

# Initialisation de l'application Flask
app = Flask(__name__)

# Route pour la page d'accueil
@app.route('/')
def index():
    return render_template('index.html')

# Route pour la page de tri
@app.route('/tri', methods=['POST'])
def tri():
    # Récupération de la longueur du tableau et création d'un tableau aléatoire
    array_length = int(request.form.get('array-length'))
    array = algorithm.set_random_array(array_length)

    # Récupération du nom de l'algorithme de tri choisi
    sort_name = request.form.get('sort')

    # Récupération de la vitesse + mise à l'échelle
    video_speed = 1800 - int(request.form.get('speed'))

    # création de l'objet correspondant
    sort_algo = algorithm.create(sort_name, array, video_speed)

    # Récupération de la vidéo d'animation du tri et renvoi de la page tri.html
    template_content = sort_algo.video
    return render_template('tri.html', array=array, sort_algo=sort_algo, template_content=template_content)

if __name__ == "__main__":
    app.run(debug=True)