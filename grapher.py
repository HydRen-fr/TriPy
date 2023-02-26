import matplotlib
matplotlib.use('agg') # Configuration pour matplotlib pour être utilisé sans interface 
import os
import sys
import matplotlib.pyplot as plt
from celluloid import Camera

class Plotter():
    def __init__(self, title):
        self.title = title
        self.fig = plt.figure()
        self.ax = plt.axes()
        self.ax.get_xaxis().set_visible(False) # Masque l'axe x
        self.ax.get_yaxis().set_visible(False) # Masque l'axe y
        self.camera = Camera(self.fig) # Crée un objet Camera pour l'animation

    def plot(self, data, first_highlight, second_highlight=None):
        self.data = data  # Données à tracer
        self.length = len(data)  # Longueur des données
        colours = list('b'*self.length)  # Initialise les couleurs à bleu pour chaque barre

        colours[first_highlight] = 'r'  # Met en rouge la première barre à mettre en évidence
        if second_highlight is not None:  # S'il y a une deuxième barre à mettre en évidence
            colours[second_highlight] = 'g'  # Met en vert la deuxième barre à mettre en évidence

        # Trace un graphe en barres avec les couleurs
        plt.bar(list(range(self.length)), data, color=colours)
        plt.title(self.title)  # Titre de la figure
        self.ax.get_xaxis().set_visible(False)  # Masque l'axe x
        self.ax.get_yaxis().set_visible(False)  # Masque l'axe y
        self.camera.snap()  # Capture l'image courante pour l'animation

    def animate(self, data, interval):
        colours = list('g'*len(data))  # Initialise les couleurs à vert pour chaque barre
        plt.bar(list(range(len(data))), data, color=colours)  # Trace un graphe en barres avec les couleurs
        plt.title(self.title)  # Titre de la figure
        self.ax.get_xaxis().set_visible(False)  # Masque l'axe x
        self.ax.get_yaxis().set_visible(False)  # Masque l'axe y
        self.camera.snap()  # Capture l'image courante pour l'animation
        return self.camera.animate(repeat=False,interval=interval).to_html5_video()  # Anime la figure et retourne une vidéo HTML5
        plt.close()  # Ferme la figure
