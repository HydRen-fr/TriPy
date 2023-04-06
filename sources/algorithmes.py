# FICHIER QUI CONTIENT LES CLASSES DES 9 ALGORITHMES PROPOSES A VISUALISER AINSI QUE QUELQUES FONCTIONS LIEES AUX DONNEES ET APP.PY

import random
from traceurs_graphique import TraceurGraphique, TraceurGraphique3D
import copy

# Fonction qui crée l'objet de tri en fonction de l'algorithme choisi et des données à trier
def creer(nom_algo, donnees, vitesse):
    # Sélection de l'algorithme en fonction de son nom
    if nom_algo == 'selection':
        algo_class = TriSelection(donnees, vitesse)
    elif nom_algo == 'insertion':
        algo_class = TriInsertion(donnees, vitesse)
    elif nom_algo == 'bulles':
        algo_class = TriBulles(donnees, vitesse)
    elif nom_algo == 'cocktail':
        algo_class = TriCocktail(donnees, vitesse)
    elif nom_algo == 'pigeon':
        algo_class = TriPigeon(donnees, vitesse)
    elif nom_algo == 'gnome':
        algo_class = TriGnome(donnees, vitesse)
    elif nom_algo == 'comptage':
        algo_class = TriComptage(donnees, vitesse)
    elif nom_algo == 'peigne':
        algo_class = TriPeigne(donnees, vitesse)
    elif nom_algo == 'shell':
        algo_class = TriShell(donnees, vitesse)

    # Si l'algorithme n'est pas reconnu, on utilise le tri par sélection par défaut   
    else:
        algo_class = TriSelection(donnees, vitesse)

    return algo_class

# Fonction qui génère un tableau de données aléatoires de longueur donnée
def donnees_aleatoires(longueur):
    # Création d'un tableau de longueur "length" avec des valeurs aléatoires entre 10 et 200 car 1 était trop minuscule sur le graphe
    donnees = [random.randint(10, 200) for i in range(longueur)]
    # Mélange
    random.shuffle(donnees)
    return donnees

# CLASSES
    
class TriPigeon():
    def __init__(self, donnees, vitesse):
        donnees_copy_3d = copy.deepcopy(donnees)
        donnees_copy_2d = copy.deepcopy(donnees)
        
        self.traceur = TraceurGraphique("Tri pigeon") 
        self.tri_pigeon(donnees_copy_2d)
        self.video = self.traceur.animer(donnees_copy_2d, vitesse)
        self.infos_liste = ["<span style='color: red';>Principe :</span> répartit chaque élément dans des trous en fonction de sa valeur, puis les rassemble en ordre croissant (non-comparatif)",
                            "Lent", 
                            "Complexité : O(n + 2^k) avec k l'écart entre la plus grande et la plus petite valeur proportionellement à n", 
                            "Stable (un tri est dit stable s'il préserve l'ordre initial des éléments égaux)", 
                            "Pas en place (un tri est dit en place s'il n'utilise qu'un nombre très limité de variables et qu'il modifie directement la structure qu'il est en train de trier)"]
        
        self.traceur3D = TraceurGraphique3D("Tri pigeon 3D") 
        self.tri_pigeon_3d(donnees_copy_3d)
        self.video3D = self.traceur3D.animer3D(donnees_copy_3d, vitesse)

    def tri_pigeon(self, donnees):
        min_value, max_value = min(donnees), max(donnees)
        range_values = max_value - min_value + 1
        pigeon = [0] * range_values

        for value in donnees:
            pigeon[value - min_value] += 1

        index = 0
        for i in range(range_values):
            while pigeon[i] > 0:
                self.traceur.dessiner(donnees, index)
                donnees[index] = i + min_value
                self.traceur.dessiner(donnees, index)
                pigeon[i] -= 1
                index += 1
        
        return donnees

    def tri_pigeon_3d(self, donnees):
        min_value, max_value = min(donnees), max(donnees)
        range_values = max_value - min_value + 1
        pigeon = [0] * range_values

        for value in donnees:
            pigeon[value - min_value] += 1

        index = 0
        for i in range(range_values):
            while pigeon[i] > 0:
                self.traceur3D.dessiner3D(donnees, index)
                donnees[index] = i + min_value
                self.traceur3D.dessiner3D(donnees, index)
                pigeon[i] -= 1
                index += 1
        
        return donnees
    

class TriBulles():
    def __init__(self, donnees, vitesse):
        donnees_copy_3d = copy.deepcopy(donnees)
        donnees_copy_2d = copy.deepcopy(donnees)

        self.traceur = TraceurGraphique("Tri à bulles") 
        self.tri_bulles(donnees_copy_2d)
        self.video = self.traceur.animer(donnees_copy_2d, vitesse)
        self.infos_liste = ["<span style='color: red';>Principe :</span> comparaison et échange successifs des éléments adjacents de la liste du début à la fin",
                            "But pédagogique",
                            "Complexité en moyenne : O(n^2)",
                            "Stable (un tri est dit stable s'il préserve l'ordre initial des éléments égaux)",
                            "En place (un tri est dit en place s'il n'utilise qu'un nombre très limité de variables et qu'il modifie directement la structure qu'il est en train de trier)"]

        self.traceur3D = TraceurGraphique3D("Tri à bulles 3D") 
        self.tri_bulles_3d(donnees_copy_3d)
        self.video3D = self.traceur3D.animer3D(donnees_copy_3d, vitesse)

    def tri_bulles(self, donnees):
        for i in range(len(donnees)):
            for j in range(0, len(donnees)-i-1):
                self.traceur.dessiner(donnees, j+1, j)
                if donnees[j+1] < donnees[j]:
                    donnees[j], donnees[j+1] = donnees[j+1], donnees[j]
                    self.traceur.dessiner(donnees, j, j+1)

        return donnees

    def tri_bulles_3d(self, donnees):
        for i in range(len(donnees)):
            for j in range(0, len(donnees)-i-1):
                self.traceur3D.dessiner3D(donnees, j+1, j)
                if donnees[j+1] < donnees[j]:
                    donnees[j], donnees[j+1] = donnees[j+1], donnees[j]
                    self.traceur3D.dessiner3D(donnees, j, j+1)

        return donnees


class TriSelection():
    def __init__(self, donnees, vitesse):
        donnees_copy_3d = copy.deepcopy(donnees)
        donnees_copy_2d = copy.deepcopy(donnees)

        self.traceur = TraceurGraphique("Tri par sélection") 
        self.tri_selection(donnees_copy_2d)
        self.video = self.traceur.animer(donnees_copy_2d, vitesse)
        self.infos_liste = ["<span style='color: red';>Principe :</span> consiste à parcourir plusieurs fois le tableau et à placer le plus petit élément à sa place, puis le 2e, puis le 3e...",
                            "Lent", 
                            "Complexité en moyenne : O(n^2)", 
                            "Non-stable (un tri est dit stable s'il préserve l'ordre initial des éléments égaux)", 
                            "En place (un tri est dit en place s'il n'utilise qu'un nombre très limité de variables et qu'il modifie directement la structure qu'il est en train de trier)"]
        
        self.traceur3D = TraceurGraphique3D("Tri par sélection 3D") 
        self.tri_selection_3d(donnees_copy_3d)
        self.video3D = self.traceur3D.animer3D(donnees_copy_3d, vitesse)
        
    def tri_selection(self, donnees):
        for i in range(len(donnees)): 
            minimum = i 
            for j in range(i+1, len(donnees)): 
                if donnees[minimum] > donnees[j]: 
                    minimum = j         
            self.traceur.dessiner(donnees, minimum, i)
            donnees[i], donnees[minimum] = donnees[minimum], donnees[i] 
            self.traceur.dessiner(donnees, i, minimum)

        return donnees
    
    def tri_selection_3d(self, donnees):
        for i in range(len(donnees)): 
            minimum = i 
            for j in range(i+1, len(donnees)): 
                if donnees[minimum] > donnees[j]: 
                    minimum = j         
            self.traceur3D.dessiner3D(donnees, minimum, i)
            donnees[i], donnees[minimum] = donnees[minimum], donnees[i] 
            self.traceur3D.dessiner3D(donnees, i, minimum)

        return donnees

    
    
class TriInsertion():
    def __init__(self, donnees, vitesse):
        donnees_copy_3d = copy.deepcopy(donnees)
        donnees_copy_2d = copy.deepcopy(donnees)

        self.traceur = TraceurGraphique("Tri par insertion") 
        self.tri_insertion(donnees_copy_2d)
        self.video = self.traceur.animer(donnees_copy_2d, vitesse)
        self.infos_liste = ["<span style='color: red';>Principe :</span> souvent utilisé pour les cartes à jouer, insertion de chaque élément à sa place dans la liste triée",
                            "Moyen",
                            "Complexité en moyenne : O(n^2)", 
                            "Stable (un tri est dit stable s'il préserve l'ordre initial des éléments égaux)",
                            "En place (un tri est dit en place s'il n'utilise qu'un nombre très limité de variables et qu'il modifie directement la structure qu'il est en train de trier)"]
        
        self.traceur3D = TraceurGraphique3D("Tri par insertion 3D") 
        self.tri_insertion_3d(donnees_copy_3d)
        self.video3D = self.traceur3D.animer3D(donnees_copy_3d, vitesse)

    def tri_insertion(self, donnees):
        for i in range(len(donnees)):
            temp = donnees[i]
            j = i - 1
            while j >= 0 and temp < donnees[j]:
                
                self.traceur.dessiner(donnees, j+1, j)

                donnees[j+1] = donnees[j]
                donnees[j] = temp

                self.traceur.dessiner(donnees, j, j+1)

                j -= 1

        return donnees
    
    def tri_insertion_3d(self, donnees):
        for i in range(len(donnees)):
            temp = donnees[i]
            j = i - 1
            while j >= 0 and temp < donnees[j]:
                self.traceur3D.dessiner3D(donnees, j+1, j)

                donnees[j+1] = donnees[j]
                donnees[j] = temp

                self.traceur3D.dessiner3D(donnees, j, j+1)

                j -= 1

        return donnees


class TriCocktail():
    def __init__(self, donnees, vitesse):
        donnees_copy_3d = copy.deepcopy(donnees)
        donnees_copy_2d = copy.deepcopy(donnees)

        self.traceur = TraceurGraphique("Tri cocktail") 
        self.tri_cocktail(donnees_copy_2d)
        self.video = self.traceur.animer(donnees_copy_2d, vitesse)
        self.infos_liste = ["<span style='color: red';>Principe :</span> variante du tri à bulles qui parcourt la liste dans les deux sens", 
                            "Moyen",
                            "Complexité en moyenne : O(n^2)", 
                            "Stable (un tri est dit stable s'il préserve l'ordre initial des éléments égaux)", 
                            "En place (un tri est dit en place s'il n'utilise qu'un nombre très limité de variables et qu'il modifie directement la structure qu'il est en train de trier)"]
        
        self.traceur3D = TraceurGraphique3D("Tri cocktail 3D") 
        self.tri_cocktail_3d(donnees_copy_3d)
        self.video3D = self.traceur3D.animer3D(donnees_copy_3d, vitesse)

    def tri_cocktail(self, donnees):
        n = len(donnees)
        permutation = True
        debut = 0
        fin = n-1

        while permutation:
            permutation = False

            for i in range(debut, fin):
                if donnees[i] > donnees[i+1]:
                    self.traceur.dessiner(donnees, i, i+1)
                    donnees[i], donnees[i+1] = donnees[i+1], donnees[i]
                    self.traceur.dessiner(donnees, i+1, i)
                    permutation = True

            if not permutation:
                break

            permutation = False

            fin -= 1

            for i in range(fin-1, debut-1, -1):
                if donnees[i] > donnees[i+1]:
                    self.traceur.dessiner(donnees, i, i+1)
                    donnees[i], donnees[i+1] = donnees[i+1], donnees[i]
                    self.traceur.dessiner(donnees, i+1, i)
                    permutation = True

            debut += 1

        return donnees
    
    def tri_cocktail_3d(self, donnees):
        n = len(donnees)
        permutation = True
        debut = 0
        fin = n-1

        while permutation:
            permutation = False

            for i in range(debut, fin):
                if donnees[i] > donnees[i+1]:
                    self.traceur3D.dessiner3D(donnees, i, i+1)
                    donnees[i], donnees[i+1] = donnees[i+1], donnees[i]
                    self.traceur3D.dessiner3D(donnees, i+1, i)
                    permutation = True

            if not permutation:
                break

            permutation = False

            fin -= 1

            for i in range(fin-1, debut-1, -1):
                if donnees[i] > donnees[i+1]:
                    self.traceur3D.dessiner3D(donnees, i, i+1)
                    donnees[i], donnees[i+1] = donnees[i+1], donnees[i]
                    self.traceur3D.dessiner3D(donnees, i+1, i)
                    permutation = True

            debut += 1

        return donnees



class TriGnome():
    def __init__(self, donnees, vitesse):
        donnees_copy_3d = copy.deepcopy(donnees)
        donnees_copy_2d = copy.deepcopy(donnees)

        self.traceur = TraceurGraphique("Tri gnome") 
        self.tri_gnome(donnees_copy_2d)
        self.video = self.traceur.animer(donnees_copy_2d, vitesse)
        self.infos_liste = ["<span style='color: red';>Principe :</span> similaire au tri par insertion, sauf que, au lieu d'insérer directement l'élément à sa bonne place, l'algorithme effectue une série de permutations", 
                            "Moyen",
                            "Complexité en moyenne : O(n^2)", 
                            "Stable (un tri est dit stable s'il préserve l'ordre initial des éléments égaux)", 
                            "En place (un tri est dit en place s'il n'utilise qu'un nombre très limité de variables et qu'il modifie directement la structure qu'il est en train de trier)"]
        
        self.traceur3D = TraceurGraphique3D("Tri gnome 3D") 
        self.tri_gnome_3d(donnees_copy_3d)
        self.video3D = self.traceur3D.animer3D(donnees_copy_3d, vitesse)

    def tri_gnome(self, donnees):
        index = 0
        n = len(donnees)
        while index < n:
            if index == 0:
                index = index + 1
            self.traceur.dessiner(donnees, index, index - 1)
            if donnees[index] >= donnees[index - 1]:
                index = index + 1
            else:
                donnees[index], donnees[index - 1] = donnees[index - 1], donnees[index]
                self.traceur.dessiner(donnees, index - 1, index)
                index = index - 1
        return donnees
    
    def tri_gnome_3d(self, donnees):
        index = 0
        n = len(donnees)
        while index < n:
            if index == 0:
                index = index + 1
            self.traceur3D.dessiner3D(donnees, index, index - 1)
            if donnees[index] >= donnees[index - 1]:
                index = index + 1
            else:
                donnees[index], donnees[index - 1] = donnees[index - 1], donnees[index]
                self.traceur3D.dessiner3D(donnees, index - 1, index)
                index = index - 1
        return donnees
    

class TriComptage():
    def __init__(self, donnees, vitesse):
        donnees_copy_3d = copy.deepcopy(donnees)
        donnees_copy_2d = copy.deepcopy(donnees)

        self.traceur = TraceurGraphique("Tri comptage") 
        donnees_copy_2d = self.tri_comptage(donnees_copy_2d) # Ne modifie pas directement les donnees sinon
        self.video = self.traceur.animer(donnees_copy_2d, vitesse)
        self.infos_liste = ["<span style='color: red';>Principe :</span> utilisation d'une seconde liste de même longueur que la liste à trier", 
                            "Moyen",
                            "Complexité : O(n)", 
                            "Stable (un tri est dit stable s'il préserve l'ordre initial des éléments égaux)", 
                            "Pas en place (un tri est dit en place s'il n'utilise qu'un nombre très limité de variables et qu'il modifie directement la structure qu'il est en train de trier)"]
        
        self.traceur3D = TraceurGraphique3D("Tri comptage 3D") 
        donnees_copy_3d = self.tri_comptage_3d(donnees_copy_3d)
        self.video3D = self.traceur3D.animer3D(donnees_copy_3d, vitesse)

    def tri_comptage(self, donnees):
            liste = [0] * (max(donnees) + 1)
            resultat = []
            self.traceur.dessiner(donnees, len(donnees) - 1)
            for element in donnees:
                liste[element] += 1

            for index, element in enumerate(liste):
                if element != 0:
                    resultat.append(index)
                    self.traceur.dessiner(resultat, len(resultat) - 1)

            return resultat
    
    def tri_comptage_3d(self, donnees):
        liste = [0] * (max(donnees) + 1)
        resultat = []
        self.traceur3D.dessiner3D(donnees, len(donnees) - 1)
        for element in donnees:
            liste[element] += 1

        for index, element in enumerate(liste):
            if element != 0:
                resultat.append(index)
                self.traceur3D.dessiner3D(resultat, len(resultat) - 1)

        return resultat


class TriPeigne():
    def __init__(self, donnees, vitesse):
        donnees_copy_3d = copy.deepcopy(donnees)
        donnees_copy_2d = copy.deepcopy(donnees)

        self.traceur = TraceurGraphique("Tri à peigne")
        self.tri_peigne(donnees_copy_2d)
        self.video = self.traceur.animer(donnees_copy_2d, vitesse)
        self.infos_liste = ["<span style='color: red';>Principe :</span> variante plus efficace du tri à bulles, ne comparant pas uniquement des éléments consécutifs, cela permet de déplacer plus rapidement les éléments qui sont loin de leur position finale",
                            "Rapide",
                            "Complexité en moyenne : O(n log n)",
                            "Non-stable (un tri est dit stable s'il préserve l'ordre initial des éléments égaux)",
                            "En place (un tri est dit en place s'il n'utilise qu'un nombre très limité de variables et qu'il modifie directement la structure qu'il est en train de trier)"]
        
        self.traceur3D = TraceurGraphique3D("Tri à peigne 3D") 
        self.tri_peigne_3d(donnees_copy_3d)
        self.video3D = self.traceur3D.animer3D(donnees_copy_3d, vitesse)

    def tri_peigne(self, donnees):
        intervalle = len(donnees)
        echange = True
        while intervalle > 1 or echange:
            intervalle = max(1, int(intervalle / 1.25))
            echange = False
            for i in range(len(donnees) - intervalle):
                j = i + intervalle
                self.traceur.dessiner(donnees, i, j)
                if donnees[i] > donnees[j]:
                    donnees[i], donnees[j] = donnees[j], donnees[i]
                    echange = True
                    self.traceur.dessiner(donnees, j, i)

        return donnees
    
    def tri_peigne_3d(self, donnees):
        intervalle = len(donnees)
        echange = True
        while intervalle > 1 or echange:
            intervalle = max(1, int(intervalle / 1.25))
            echange = False
            for i in range(len(donnees) - intervalle):
                j = i + intervalle
                self.traceur3D.dessiner3D(donnees, i, j)
                if donnees[i] > donnees[j]:
                    donnees[i], donnees[j] = donnees[j], donnees[i]
                    echange = True
                    self.traceur3D.dessiner3D(donnees, j, i)

        return donnees
    
class TriShell():
    def __init__(self, donnees, vitesse):
        donnees_copy_3d = copy.deepcopy(donnees)
        donnees_copy_2d = copy.deepcopy(donnees)

        self.traceur = TraceurGraphique("Tri de Shell")
        self.tri_shell(donnees_copy_2d)
        self.video = self.traceur.animer(donnees_copy_2d, vitesse)
        self.infos_liste = ["<span style='color: red';>Principe :</span> variante du tri par insertion qui utilise des gaps qui diminuent à chaque étape pour trier des sous-listes du tableau",
                            "Rapide",
                            "Complexité en moyenne : O(n log^2 n) dans le pire des cas, mais peut être amélioré avec différentes séquences de pas", 
                            "Non-stable (un tri est dit stable s'il préserve l'ordre initial des éléments égaux)", 
                            "En place (un tri est dit en place s'il n'utilise qu'un nombre très limité de variables et qu'il modifie directement la structure qu'il est en train de trier)"]
        
        self.traceur3D = TraceurGraphique3D("Tri de Shell 3D") 
        self.tri_shell_3d(donnees_copy_3d)
        self.video3D = self.traceur3D.animer3D(donnees_copy_3d, vitesse)

    def tri_shell(self, donnees):
        n = len(donnees)
        h = 1
        while h < n // 3:
            h = 3 * h + 1

        while h >= 1:
            for i in range(h, n):
                j = i
                while j >= h and donnees[j] < donnees[j-h]:
                    self.traceur.dessiner(donnees, j, j-h)
                    donnees[j], donnees[j-h] = donnees[j-h], donnees[j]
                    j -= h
                    self.traceur.dessiner(donnees, j, i)

            h = h // 3

        return donnees
    
    def tri_shell_3d(self, donnees):
        n = len(donnees)
        h = 1
        while h < n // 3:
            h = 3 * h + 1

        while h >= 1:
            for i in range(h, n):
                j = i
                while j >= h and donnees[j] < donnees[j-h]:
                    self.traceur3D.dessiner3D(donnees, j, j-h)
                    donnees[j], donnees[j-h] = donnees[j-h], donnees[j]
                    j -= h
                    self.traceur3D.dessiner3D(donnees, j, i)

            h = h // 3

        return donnees



















