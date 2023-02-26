import algorithm
from flask import Flask, render_template, request, redirect, url_for

# Initialisation de l'application Flask
app = Flask(__name__)

# Route pour la page d'accueil
@app.route('/')
def index():
    return render_template('index.html')

# Route pour la page de tri
@app.route('/tri', methods=['GET'])
def tri():
    # Récupération de la longueur du tableau et création d'un tableau aléatoire
    array_length = int(request.args.get('array-length'))
    array = algorithm.set_random_array(array_length)

    # Récupération du nom de l'algorithme de tri choisi et création de l'objet de tri correspondant
    sort_name = request.args.get('sort')
    sort_algo = algorithm.create(sort_name, array)

    # Récupération de la vidéo d'animation du tri et renvoi de la page tri.html
    template_content = sort_algo.video
    return render_template('tri.html', array=array, sort_algo=sort_algo, template_content=template_content)

if __name__ == "__main__":
    app.run(debug=True)