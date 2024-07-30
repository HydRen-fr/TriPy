# FICHIER PRINCIPAL QUI FAIT LA LIAISON ENTRE LES ALGORITHMES ET L'INTERFACE

import algorithmes
from traceurs_graphique import plot_complexite
from config import (algo_2_3D_template, algo_3D_template, algo_tri, algo_tri_2,
                    deuxieme_algo_template, donnees_init, explications_1,
                    explications_2, algo_complexite, algo_2_complexite, premiere_algo_template, video_speed)

import re

from flask import Flask, render_template, request, send_file


app = Flask(__name__)

def reset_global_variables():
    global premiere_algo_template, deuxieme_algo_template, algo_3D_template, algo_2_3D_template, donnees_init, video_speed, algo_tri, algo_tri_2, explications_1, explications_2, algo_complexite, algo_2_complexite
    premiere_algo_template = None
    deuxieme_algo_template = None
    algo_3D_template = None
    algo_2_3D_template = None
    donnees_init = None
    video_speed = None
    algo_tri = None
    algo_tri_2 = None
    explications_1 = None
    explications_2 = None
    algo_complexite = None
    algo_2_complexite = None

# La clé c'est d'accorder les liens html aux liens flask après on return le bon chemin simplement

# VISUALISER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/preparation')
def preparation():

    reset_global_variables()

    return render_template('visualiser/preparation.html')


@app.route('/preparation/visualizer', methods=['POST', 'GET'])
def tri():
    global donnees_init, video_speed, algo_tri, algo_tri_2, algo_3D_template, algo_2_3D_template, premiere_algo_template, deuxieme_algo_template, explications_1, explications_2, algo_complexite, algo_2_complexite

    if request.method == 'POST':
        if request.form.get('choix') == "1":
            # Récupération de la longueur du tableau et création d'un tableau aléatoire
            longueur_donnees = int(request.form.get('array-length'))
            donnees_init = algorithmes.donnees_aleatoires(longueur_donnees)

        if request.form.get('choix') == "2":
            # Récupération de la liste de l'utilisateur + ajustement
            donnees_input = str(request.form.get('array-values'))
            donnees_init = donnees_input.split()
            donnees_init = [int(x) for x in donnees_init]
            donnees_init = [x + 10 for x in donnees_init]

        # Récupération du nom de l'algorithme de tri choisi
        nom_algo = request.form.get('tri')

        # Récupération de la vitesse + mise à l'échelle
        video_speed = 1800 - int(request.form.get('speed'))

        # Création de l'objet correspondant
        algo_tri = algorithmes.creer(nom_algo, donnees_init, video_speed)

        # Récupération de la vidéo d'animation du tri et renvoi de la page tri.html
        premiere_algo_template = algo_tri.video

        # Récupération des explications
        explications_1 = algo_tri.infos_liste

        # Recherche de tous les motifs O(...) dans les éléments
        regex = r"O\([^)]+\)"
        match = re.search(regex, explications_1[2])
        algo_complexite = match.group()

        explications_1[2] = re.sub(regex, r"<span class='highlight'>\g<0> <img/> </span>", explications_1[2])

    return render_template('visualiser/visualizer.html', premiere_algo_template=premiere_algo_template,
                           explications_1=explications_1)

@app.route('/preparation/visualizer-2', methods=['POST', 'GET'])
def tri_2():
    global donnees_init, video_speed, algo_tri, algo_tri_2, algo_3D_template, algo_2_3D_template, premiere_algo_template, deuxieme_algo_template, explications_1, explications_2, algo_complexite, algo_2_complexite

    if request.method == 'POST':
        # Récupération du nom de l'algorithme de tri choisi
        nom_algo_2 = request.form.get('tri2')

        # Création de l'objet correspondant
        algo_tri_2 = algorithmes.creer(nom_algo_2, donnees_init, video_speed)

        # Récupération de la vidéo d'animation du tri et renvoi de la page tri.html
        deuxieme_algo_template = algo_tri_2.video

        # Récupération des explications
        explications_2 = algo_tri_2.infos_liste

        # Recherche de tous les motifs O(...) dans les éléments
        regex = r"O\([^)]+\)"
        match = re.search(regex, explications_2[2])
        algo_2_complexite = match.group()

        explications_2[2] = re.sub(regex, r"<span class='highlight'>\g<0> <img/> </span>", explications_2[2])

        # Supprime les définitions entre parenthèses car elles sont déjà données dans le premier texte
        explications_2[3] = re.sub(r"\([^()]*\)", "", explications_2[3])
        explications_2[4] = re.sub(r"\([^()]*\)", "", explications_2[4])

    return render_template('visualiser/visualizer-2.html', premiere_algo_template=premiere_algo_template,
                           deuxieme_algo_template=deuxieme_algo_template,
                            explications_1=explications_1, explications_2=explications_2)


@app.route('/preparation/complexite')
def complexite_image():
    global donnees_init, video_speed, algo_tri, algo_tri_2, algo_3D_template, algo_2_3D_template, premiere_algo_template, deuxieme_algo_template, explications_1, explications_2, algo_complexite, algo_2_complexite

    algo_complexite_img = plot_complexite(algo_complexite)

    # Envoi de l'image en tant que réponse HTTP
    return send_file(algo_complexite_img, mimetype='image/png')

@app.route('/preparation/complexite_2')
def complexite_2_image():
    global donnees_init, video_speed, algo_tri, algo_tri_2, algo_3D_template, algo_2_3D_template, premiere_algo_template, deuxieme_algo_template, explications_1, explications_2, algo_complexite, algo_2_complexite

    algo_2_complexite_img = plot_complexite(algo_2_complexite)

    # Envoi de l'image en tant que réponse HTTP
    return send_file(algo_2_complexite_img, mimetype='image/png')




@app.route('/preparation/visualizer-3D')
def tri_3d():
    global donnees_init, video_speed, algo_tri, algo_tri_2, algo_3D_template, algo_2_3D_template, premiere_algo_template, deuxieme_algo_template, explications_1, explications_2, algo_complexite, algo_2_complexite

    if algo_3D_template == None:
        algo_3D_template = algo_tri.video3D

    return render_template('visualiser/visualizer-3D.html', algo_3D_template=algo_3D_template)

@app.route('/preparation/visualizer-3D-2')
def tri_3d_2():
    global donnees_init, video_speed, algo_tri, algo_tri_2, algo_3D_template, algo_2_3D_template, premiere_algo_template, deuxieme_algo_template, explications_1, explications_2, algo_complexite, algo_2_complexite

    if algo_3D_template == None:
        algo_3D_template = algo_tri.video3D

    algo_2_3D_template = algo_tri_2.video3D # Peut être changé sans reset donc pas de conditions

    return render_template('visualiser/visualizer-3D-2.html', algo_3D_template=algo_3D_template, algo_2_3D_template=algo_2_3D_template)





# INTERAGIR

from plotly_graph import *
from plotly.offline import plot


@app.route('/graph', methods=['POST', 'GET'])
def graph():
    if request.method == 'POST':
        donnees_txt_str = request.form.get('donnees-interactives')
        donnees_txt_liste = [int(x) for x in donnees_txt_str.split()] # Convertir en liste d'entiers

        fig_exec_time = plot_exec_temps(donnees_txt_liste) # Fonction importée de plotly_graph
        exec_time_graph = fig_exec_time.to_html(full_html=False, include_plotlyjs='cdn', config={'displayModeBar': False}) # Conversion html et paramètres adéquats
        return render_template('interagir/graph.html', exec_time_graph=exec_time_graph)

    else:
        reset_global_variables()
        return render_template('interagir/graph.html', exec_time_graph="")




if __name__ == "__main__":
    app.run(debug=True)

