# FICHIER QUI CONTIENT LES CLASSES DES 12 ALGORITHMES PROPOSES A VISUALISER AINSI QUE QUELQUES FONCTIONS LIEES AUX DONNEES ET APP.PY

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
    elif nom_algo == 'tas':
        algo_class = TriParTas(donnees, vitesse)
    elif nom_algo == 'pigeon':
        algo_class = TriPigeon(donnees, vitesse)
    elif nom_algo == 'fusion':
        algo_class = TriFusion(donnees, vitesse)
    elif nom_algo == 'rapide':
        algo_class = TriRapide(donnees, vitesse)
    elif nom_algo == 'arborescent':
        algo_class = TriArborescent(donnees, vitesse)
    elif nom_algo == 'peigne':
        algo_class = TriPeigne(donnees, vitesse)
    elif nom_algo == 'pair-impair':
        algo_class = TriPairImpair(donnees, vitesse)
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


class TriPairImpair():
    def __init__(self, donnees, vitesse):
        donnees_copy_2d = copy.deepcopy(donnees)
        donnees_copy_3d = copy.deepcopy(donnees)

        self.traceur = TraceurGraphique("Tri pair-impair") 
        self.tri_pair_impair(donnees_copy_2d)
        self.video = self.traceur.animer(donnees_copy_2d, vitesse)
        self.infos_liste = ["<span style='color: red';>Principe :</span> variante du tri à bulles qui parcourt la liste en alternant les comparaisons entre éléments de rang pair et impair",
                            "Moyen",
                            "Complexité en moyenne : O(n^2)",
                            "Stable (un tri est dit stable s'il préserve l'ordre initial des éléments égaux)", 
                            "En place (un tri est dit en place s'il n'utilise qu'un nombre très limité de variables et qu'il modifie directement la structure qu'il est en train de trier)"]
        
        self.traceur3D = TraceurGraphique3D("Tri pair-impair 3D") 
        self.tri_pair_impair_3d(donnees_copy_3d)
        self.video3D = self.traceur3D.animer3D(donnees_copy_3d, vitesse)

    def tri_pair_impair(self, donnees):
        trie = False
        while not trie:
            trie = True
            for i in range(0, len(donnees)-1, 2):
                if donnees[i] > donnees[i+1]:
                    self.traceur.dessiner(donnees, i, i+1)
                    donnees[i], donnees[i+1] = donnees[i+1], donnees[i]
                    self.traceur.dessiner(donnees, i+1, i)
                    trie = False
            for i in range(1, len(donnees)-1, 2):
                if donnees[i] > donnees[i+1]:
                    self.traceur.dessiner(donnees, i, i+1)
                    donnees[i], donnees[i+1] = donnees[i+1], donnees[i]
                    self.traceur.dessiner(donnees, i+1, i)
                    trie = False

        return donnees
    
    def tri_pair_impair_3d(self, donnees):
        trie = False
        while not trie:
            trie = True
            for i in range(0, len(donnees)-1, 2):
                if donnees[i] > donnees[i+1]:
                    self.traceur3D.dessiner3D(donnees, i, i+1)
                    donnees[i], donnees[i+1] = donnees[i+1], donnees[i]
                    self.traceur3D.dessiner3D(donnees, i+1, i)
                    trie = False
            for i in range(1, len(donnees)-1, 2):
                if donnees[i] > donnees[i+1]:
                    self.traceur3D.dessiner3D(donnees, i, i+1)
                    donnees[i], donnees[i+1] = donnees[i+1], donnees[i]
                    self.traceur3D.dessiner3D(donnees, i+1, i)
                    trie = False

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
        
        self.traceur3D = TraceurGraphique3D("Tri Cocktail 3D") 
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
    

class TriFusion():
    def __init__(self, donnees, vitesse):
        donnees_copy_3d = copy.deepcopy(donnees)
        donnees_copy_2d = copy.deepcopy(donnees)

        self.traceur = TraceurGraphique("Tri fusion")
        self.tri_fusion(donnees_copy_2d, 0, len(donnees_copy_2d)-1)
        self.video = self.traceur.animer(donnees_copy_2d, vitesse)
        self.infos_liste = ["<span style='color: red';>Principe :</span> repose sur le principe « diviser pour régner », on divise la liste en deux, trie chaque moitié, puis les fusionne",
                            "Rapide", 
                            "Complexité : O(n log n)", 
                            "Stable (un tri est dit stable s'il préserve l'ordre initial des éléments égaux)", 
                            "Pas en place (un tri est dit en place s'il n'utilise qu'un nombre très limité de variables et qu'il modifie directement la structure qu'il est en train de trier)"]
        
        self.traceur3D = TraceurGraphique3D("Tri fusion 3D")
        self.tri_fusion_3d(donnees_copy_3d, 0, len(donnees_copy_3d)-1)
        self.video3D = self.traceur3D.animer3D(donnees_copy_3d, vitesse)

    def tri_fusion(self, donnees, debut, fin):
        if debut < fin:
            milieu = (debut+fin) // 2

            self.tri_fusion(donnees, debut, milieu)

            self.tri_fusion(donnees, milieu+1, fin)

            i = debut
            j = milieu + 1
            temp = []

            while i <= milieu and j <= fin:
                if donnees[i] < donnees[j]:
                    temp.append(donnees[i])
                    i += 1
                else:
                    temp.append(donnees[j])
                    j += 1

            while i <= milieu:
                temp.append(donnees[i])
                i += 1

            while j <= fin:
                temp.append(donnees[j])
                j += 1
            
            self.traceur.dessiner(donnees, debut, fin)

            for i, valeur in enumerate(temp):
                donnees[debut + i] = valeur

            self.traceur.dessiner(donnees, debut, fin)

        return donnees
    
    def tri_fusion_3d(self, donnees, debut, fin):
        if debut < fin:
            milieu = (debut+fin) // 2

            self.tri_fusion_3d(donnees, debut, milieu)

            self.tri_fusion_3d(donnees, milieu+1, fin)

            i = debut
            j = milieu + 1
            temp = []

            while i <= milieu and j <= fin:
                if donnees[i] < donnees[j]:
                    temp.append(donnees[i])
                    i += 1
                else:
                    temp.append(donnees[j])
                    j += 1

            while i <= milieu:
                temp.append(donnees[i])
                i += 1

            while j <= fin:
                temp.append(donnees[j])
                j += 1
            
            self.traceur3D.dessiner3D(donnees, debut, fin)

            for i, valeur in enumerate(temp):
                donnees[debut + i] = valeur

            self.traceur3D.dessiner3D(donnees, debut, fin)

        return donnees


class TriRapide():
    def __init__(self, donnees, vitesse):
        donnees_copy_3d = copy.deepcopy(donnees)
        donnees_copy_2d = copy.deepcopy(donnees)

        self.traceur = TraceurGraphique("Tri rapide")
        self.tri_rapide(donnees_copy_2d, 0, len(donnees_copy_2d) - 1)
        self.video = self.traceur.animer(donnees_copy_2d, vitesse)
        self.infos_liste = ["<span style='color: red';>Principe :</span> repose sur le principe « diviser pour régner », on partitionne la liste en deux autour d'un pivot et trie les deux parties de manière récursive",
                            "Rapide", 
                            "Complexité en moyenne : O(n log n)", 
                            "Non-stable (un tri est dit stable s'il préserve l'ordre initial des éléments égaux)", 
                            "En place (un tri est dit en place s'il n'utilise qu'un nombre très limité de variables et qu'il modifie directement la structure qu'il est en train de trier)"]
        
        self.traceur3D = TraceurGraphique3D("Tri rapide 3D") 
        self.tri_rapide_3d(donnees_copy_3d, 0, len(donnees_copy_3d) - 1)
        self.video3D = self.traceur3D.animer3D(donnees_copy_3d, vitesse)

    def tri_rapide(self, donnees, debut, fin):
        if debut < fin:
            pivot = self.partitionner(donnees, debut, fin)

            self.tri_rapide(donnees, debut, pivot)
            self.tri_rapide(donnees, pivot + 1, fin)
            
    def partitionner(self, donnees, debut, fin):
        pivot = donnees[debut]
        i = debut - 1
        j = fin + 1

        while True:
            i += 1
            while donnees[i] < pivot:
                i += 1

            j -= 1
            while donnees[j] > pivot:
                j -= 1

            if i >= j:
                return j

            self.traceur.dessiner(donnees, j, i)
            donnees[i], donnees[j] = donnees[j], donnees[i]
            self.traceur.dessiner(donnees, i, j)
    
    def tri_rapide_3d(self, donnees, debut, fin):
        if debut < fin:
            pivot = self.partitionner_3d(donnees, debut, fin)

            self.tri_rapide_3d(donnees, debut, pivot)
            self.tri_rapide_3d(donnees, pivot + 1, fin)
            
    def partitionner_3d(self, donnees, debut, fin):
        pivot = donnees[debut]
        i = debut - 1
        j = fin + 1

        while True:
            i += 1
            while donnees[i] < pivot:
                i += 1

            j -= 1
            while donnees[j] > pivot:
                j -= 1

            if i >= j:
                return j

            self.traceur3D.dessiner3D(donnees, j, i)
            donnees[i], donnees[j] = donnees[j], donnees[i]
            self.traceur3D.dessiner3D(donnees, i, j)



class TriParTas():
    def __init__(self, donnees, vitesse):
        donnees_copy_3d = copy.deepcopy(donnees)
        donnees_copy_2d = copy.deepcopy(donnees)

        self.traceur = TraceurGraphique("Tri par tas")
        self.tri_par_tas(donnees_copy_2d)
        self.video = self.traceur.animer(donnees_copy_2d, vitesse)
        self.infos_liste = ["<span style='color: red';>Principe :</span> amélioration du tri par sélection avec une structure de tas",
                            "Rapide", 
                            "Complexité : O(n log n)", 
                            "Non-stable (un tri est dit stable s'il préserve l'ordre initial des éléments égaux)", 
                            "En place (un tri est dit en place s'il n'utilise qu'un nombre très limité de variables et qu'il modifie directement la structure qu'il est en train de trier)"]

        
        self.traceur3D = TraceurGraphique3D("Tri par tas 3D") 
        self.tri_par_tas_3d(donnees_copy_3d)
        self.video3D = self.traceur3D.animer3D(donnees_copy_3d, vitesse)

    def tri_par_tas(self, donnees):

        def echanger(donnees, i, j):
            """
            Échange les éléments des indices i et j dans le tableau de données
            """
            donnees[i], donnees[j] = donnees[j], donnees[i]

        def entasser_max(donnees, n, i):
            """
            Entasse le sous-arbre enraciné à l'indice i du tableau de données
            pour s'assurer qu'il satisfait la propriété du tas max.
            """
            racine = i
            gauche = 2 * i + 1
            droite = 2 * i + 2

            if gauche < n and donnees[gauche] > donnees[racine]:
                racine = gauche

            if droite < n and donnees[droite] > donnees[racine]:
                racine = droite

            if racine != i:
                self.traceur.dessiner(donnees, racine, i)
                echanger(donnees, i, racine)
                self.traceur.dessiner(donnees, i, racine)
                entasser_max(donnees, n, racine)

        n = len(donnees)

        for i in range(n // 2 - 1, -1, -1):
            entasser_max(donnees, n, i)

        for i in range(n - 1, 0, -1):
            echanger(donnees, 0, i)
            self.traceur.dessiner(donnees, 0, i)
            entasser_max(donnees, i, 0)

        return donnees
    
    def tri_par_tas_3d(self, donnees):

        def echanger_3d(donnees, i, j):
            donnees[i], donnees[j] = donnees[j], donnees[i]

        def entasser_max_3d(donnees, n, i):
            racine = i
            gauche = 2 * i + 1
            droite = 2 * i + 2

            if gauche < n and donnees[gauche] > donnees[racine]:
                racine = gauche

            if droite < n and donnees[droite] > donnees[racine]:
                racine = droite

            if racine != i:
                self.traceur3D.dessiner3D(donnees, racine, i)
                echanger_3d(donnees, i, racine)
                self.traceur3D.dessiner3D(donnees, i, racine)
                entasser_max_3d(donnees, n, racine)

        n = len(donnees)

        for i in range(n // 2 - 1, -1, -1):
            entasser_max_3d(donnees, n, i)

        for i in range(n - 1, 0, -1):
            echanger_3d(donnees, 0, i)
            self.traceur3D.dessiner3D(donnees, 0, i)
            entasser_max_3d(donnees, i, 0)

        return donnees
    

class TriArborescent():
    def __init__(self, donnees, vitesse):
        donnees_copy_3d = copy.deepcopy(donnees)
        donnees_copy_2d = copy.deepcopy(donnees)

        self.traceur = TraceurGraphique("Tri arborescent") 
        self.tri_arborescent(donnees_copy_2d)
        self.video = self.traceur.animer(donnees_copy_2d, vitesse)
        self.infos_liste = ["<span style='color: red';>Principe :</span> insère les éléments un à un dans un arbre binaire de recherche, puis lit l'arbre selon un parcours en profondeur", 
                            "Rapide",
                            "Complexité en moyenne : O(n log n)", 
                            "Non-stable (un tri est dit stable s'il préserve l'ordre initial des éléments égaux)", 
                            "Pas en place (un tri est dit en place s'il n'utilise qu'un nombre très limité de variables et qu'il modifie directement la structure qu'il est en train de trier)"]
        
        self.traceur3D = TraceurGraphique3D("Tri arborescent 3D") 
        self.tri_arborescent_3d(donnees_copy_3d)
        self.video3D = self.traceur3D.animer3D(donnees_copy_3d, vitesse)

    def tri_arborescent(self, donnees):

        def tri_recursif(donnees, i, taille):
            """
            Trie récursivement les sous-arbres en partant de la racine i
            """
            gauche = 2 * i + 1
            droite = 2 * i + 2
            max = i

            if gauche < taille and donnees[gauche] > donnees[max]:
                max = gauche

            if droite < taille and donnees[droite] > donnees[max]:
                max = droite

            if max != i:
                self.traceur.dessiner(donnees, max, i)

                donnees[i], donnees[max] = donnees[max], donnees[i]

                self.traceur.dessiner(donnees, i, max)

                tri_recursif(donnees, max, taille)

        n = len(donnees)

        for i in range(n // 2 - 1, -1, -1):
            tri_recursif(donnees, i, n)

        for i in range(n-1, 0, -1):
            self.traceur.dessiner(donnees, 0, i)

            donnees[0], donnees[i] = donnees[i], donnees[0]

            self.traceur.dessiner(donnees, i, 0)

            tri_recursif(donnees, 0, i)

        return donnees
    
    def tri_arborescent_3d(self, donnees):

        def tri_recursif_3d(donnees, i, taille):

            gauche = 2 * i + 1
            droite = 2 * i + 2
            max = i

            if gauche < taille and donnees[gauche] > donnees[max]:
                max = gauche

            if droite < taille and donnees[droite] > donnees[max]:
                max = droite

            if max != i:
                self.traceur3D.dessiner3D(donnees, max, i)

                donnees[i], donnees[max] = donnees[max], donnees[i]

                self.traceur3D.dessiner3D(donnees, i, max)

                tri_recursif_3d(donnees, max, taille)

        n = len(donnees)

        for i in range(n // 2 - 1, -1, -1):
            tri_recursif_3d(donnees, i, n)

        for i in range(n-1, 0, -1):
            self.traceur3D.dessiner3D(donnees, 0, i)

            donnees[0], donnees[i] = donnees[i], donnees[0]

            self.traceur3D.dessiner3D(donnees, i, 0)

            tri_recursif_3d(donnees, 0, i)

        return donnees


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



















