# FICHIER QUI CONTIENT LE CODE QUI PERMET DE VISUALISER LES DIFFERENTS ALGORITHMES EN 2D ET 3D AINSI QUE DE TRACER LES COMPLEXITES

import matplotlib
matplotlib.use('agg') # Configuration pour matplotlib pour être utilisé sans interface 
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import numpy as np
import io 
from celluloid import Camera
from matplotlib import style

class TraceurGraphique():
    def __init__(self, titre):
        style.use("fivethirtyeight")

        self.fig = plt.figure()
        self.fig.set_size_inches(7.5, 4.27) # Taille
        self.ax = plt.axes()
        self.ax.get_xaxis().set_visible(False) # Masque l'axe x
        self.ax.get_yaxis().set_visible(False) # Masque l'axe y
        self.titre = titre
        self.camera = Camera(self.fig) # Crée un objet Camera pour l'animation
        

    def dessiner(self, donnees, premiere_highlight, deuxieme_highlight=None):
        self.donnees = donnees  # Données à tracer
        self.longueur = len(donnees)  # Longueur des données
        couleurs = ['b']*self.longueur  # Initialise les couleurs à bleu pour chaque barre

        if deuxieme_highlight is not None:  # S'il y a une deuxième barre à mettre en évidence
            couleurs[deuxieme_highlight] = 'mediumseagreen'
        
        couleurs[premiere_highlight] = 'gold' 
    
        # Trace un graphe en barres avec les couleurs
        for i in range(self.longueur):
            plt.bar(i, self.donnees[i], color=couleurs[i])

        plt.title(self.titre, color="black")  # Titre de la figure
        self.ax.get_xaxis().set_visible(False)  # Masque l'axe x
        self.ax.get_yaxis().set_visible(False)  # Masque l'axe y

        self.camera.snap()  # Capture l'image courante pour l'animation


    def animer(self, donnees, speed_interval):
        couleurs = list('c'*len(donnees))  # Initialise les couleurs à cyan pour chaque barre
        plt.bar(list(range(len(donnees))), donnees, color=couleurs)  # Trace un graphe en barres avec les couleurs
        plt.title(self.titre, color="black")  # Titre de la figure

        self.ax.get_xaxis().set_visible(False)  # Masque l'axe x
        self.ax.get_yaxis().set_visible(False)  # Masque l'axe y

        self.camera.snap()  # Capture l'image courante pour l'animation
        plt.close()  # Ferme la figure
        return self.camera.animate(repeat=False,interval=speed_interval).to_html5_video()  # Anime la figure et retourne une vidéo HTML5
        



class TraceurGraphique3D():
    def __init__(self, titre):
        style.use("classic")

        self.fig = plt.figure()
        self.fig.set_size_inches(9.25, 8.65) # Taille
        self.ax = self.fig.add_subplot(111, projection='3d')
        self.titre = titre
        self.camera = Camera(self.fig) # Crée un objet Camera pour l'animation
        self.ax.set_xticks([])
        self.ax.set_yticks([])
        self.ax.set_zticks([])
        self.ax.view_init(12, 6)
        
    def dessiner3D(self, donnees, premiere_highlight, deuxieme_highlight=None):
        self.donnees = donnees  # Données à tracer
        self.longueur = len(donnees)  # Longueur des données
        x = np.arange(self.longueur)
        y = np.arange(self.longueur)
        z = np.zeros(self.longueur)  # Barres au sol
        couleurs = ['b']*self.longueur  # Initialise les couleurs à bleu pour chaque barre

        if deuxieme_highlight is not None:  # S'il y a une deuxième barre à mettre en évidence
            couleurs[deuxieme_highlight] = 'mediumseagreen'
        
        couleurs[premiere_highlight] = 'gold'
    
        # Trace un graphe en barres avec les couleurs
        self.ax.bar3d(x, y, z, 0.5, 0.5, donnees, color=couleurs)

        self.ax.set_title(self.titre)  # Titre de la figure

        self.camera.snap()  # Capture l'image courante pour l'animation

    def animer3D(self, donnees, speed_interval):
        x = np.arange(len(donnees))
        y = np.arange(len(donnees))
        z = np.zeros(len(donnees))  # Barres au sol
        couleurs = list('c'*len(donnees))  # Initialise les couleurs à cyan pour chaque barre
        self.ax.bar3d(x, y, z, 0.5, 0.5, donnees, color=couleurs)  # Trace un graphe en barres avec les couleurs
        self.ax.set_title(self.titre)  # Titre de la figure

        self.camera.snap()  # Capture l'image courante pour l'animation
        plt.close()  # Ferme la figure
        return self.camera.animate(repeat=False,interval=speed_interval).to_html5_video()  # Anime la figure et retourne une vidéo HTML5
    


def plot_complexite(complexite):
    style.use("dark_background")
    # Différents grands o possibles
    n = np.linspace(1, 10, 100)
    k = np.linspace(1, 10, 100)
    grands_o = {
        'O(1)': np.ones(n.shape),
        'O(log n)': np.log(n),
        'O(n)': n,
        'O(n log n)': n * np.log(n),
        'O(n^2)': n**2,
        'O(n^3)': n**3,
        'O(2^n)': 2**n,
        'O(n + 2^k)': n + 2**k
    }

    f = grands_o[complexite]

    # Plot
    fig, ax = plt.subplots()
    ax.plot(n, f)
    ax.set_title(complexite)
    ax.set_xlabel('Taille des données')
    ax.set_ylabel('Temps d\'exécution')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    # Masquer les valeurs des axes x et y
    ax.set_xticklabels([])
    ax.set_yticklabels([])

    # Taille des axes
    ax.set_xlim(1, 10)
    ax.set_ylim(0, 70)

    # Redimensionner l'image
    fig.set_size_inches(4.5, 4.5)

    # Sauvegarder avec io
    buffer = io.BytesIO()
    fig.savefig(buffer, format='png', bbox_inches='tight', pad_inches=0)
    buffer.seek(0)

    return buffer
        


