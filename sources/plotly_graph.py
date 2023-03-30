# FICHIER QUI PERMET LE GRAPHIQUE INTERACTIF

import timeit
import plotly.graph_objs as go

def tri_selection(liste):
    n = len(liste)

    # Parcourir le tableau
    for i in range(n):
        # Trouver l'élément minimum restant
        min_idx = i
        for j in range(i+1, n):
            if liste[j] < liste[min_idx]:
                min_idx = j

        # Echanger l'élément minimum avec l'élément actuel
        liste[i], liste[min_idx] = liste[min_idx], liste[i]

    return liste


def tri_insertion(liste):
    n = len(liste)
    
    # Parcourir la liste à partir de la deuxième position
    for i in range(1, n):

        valeur_actuelle = liste[i]

        position = i
        
        # Parcourir la liste à partir de la position actuelle jusqu'au début de la liste
        # et décaler les éléments qui sont plus grands que la valeur actuelle vers la droite
        while position > 0 and liste[position - 1] > valeur_actuelle:
            liste[position] = liste[position - 1]
            position -= 1
        
        # Insérer la valeur actuelle
        liste[position] = valeur_actuelle

    return liste



def tri_bulles(liste):
    n = len(liste)
    # Parcourt le tableau
    for i in range(n):
        # Derniers éléments sont triés, donc réduire la boucle
        for j in range(0, n-i-1):
            # Echange les éléments si l'élément trouvé est plus grand que le suivant
            if liste[j] > liste[j+1] :
                liste[j], liste[j+1] = liste[j+1], liste[j]

    return liste


def tri_cocktail(liste):
    n = len(liste)
    for i in range(n//2):
        # Parcourir du début à la fin
        for j in range(i, n-i-1):
            if liste[j] > liste[j+1]:
                liste[j], liste[j+1] = liste[j+1], liste[j]
        
        # Parcourir de la fin au début
        for j in range(n-i-1, i, -1):
            if liste[j] < liste[j-1]:
                liste[j], liste[j-1] = liste[j-1], liste[j]

    return liste


def tri_tas(liste):
    # Fonction récursive pour entasser un sous-arbre en un tas
    def entasser(liste, n, i):
        plus_grand = i
        # Calculer les indices des enfants gauche et droite de l'élément i
        gauche = 2 * i + 1
        droite = 2 * i + 2
 
        if gauche < n and liste[i] < liste[gauche]:
            plus_grand = gauche

        if droite < n and liste[plus_grand] < liste[droite]:
            plus_grand = droite
 
        # Si le plus grand élément n'est pas la racine, échanger la racine avec le plus grand élément
        if plus_grand != i:
            liste[i], liste[plus_grand] = liste[plus_grand], liste[i]
 
            # Récursivement entasser le sous-arbre affecté par l'échange
            entasser(liste, n, plus_grand)
 
    n = len(liste)
 
    # Construire un tas en partant de la fin de la liste et en appelant la fonction entasser pour chaque élément
    for i in range(n, -1, -1):
        entasser(liste, n, i)
 
    # Extraire les éléments du tas un par un et les placer à leur position correcte dans la liste triée
    for i in range(n - 1, 0, -1):
        liste[i], liste[0] = liste[0], liste[i]
        entasser(liste, i, 0)

    return liste


def tri_pigeon(liste):
    # Trouver la valeur maximale et minimale dans la liste
    min_value, max_value = min(liste), max(liste)
    # Trouver la plage de valeurs à trier
    range_values = max_value - min_value + 1
    # Créer des trous de pigeon
    pigeon = [0] * range_values

    # Remplir les trous de pigeon avec les valeurs de la liste
    for value in liste:
        pigeon[value - min_value] += 1

    # Remettre les valeurs triées dans la liste
    index = 0
    for i in range(range_values):
        while pigeon[i] > 0:
            liste[index] = i + min_value
            pigeon[i] -= 1
            index += 1
    
    return liste


def tri_fusion(liste):
    if len(liste) <= 1:
        return liste
    
    # Diviser la liste en deux sous-listes
    milieu_index = len(liste) // 2
    gauche_liste = liste[:milieu_index]
    droite_liste = liste[milieu_index:]
    
    # Récursivement trier les sous-listes
    gauche_liste = tri_fusion(gauche_liste)
    droite_liste = tri_fusion(droite_liste)
    
    # Fusionner les sous-listes triées
    liste_triee = []
    gauche_index, droite_index = 0, 0
    while gauche_index < len(gauche_liste) and droite_index < len(droite_liste):
        if gauche_liste[gauche_index] < droite_liste[droite_index]:
            liste_triee.append(gauche_liste[gauche_index])
            gauche_index += 1
        else:
            liste_triee.append(droite_liste[droite_index])
            droite_index += 1
    
    liste_triee += gauche_liste[gauche_index:]
    liste_triee += droite_liste[droite_index:]
    
    return liste_triee



def tri_rapide(liste):
    if len(liste) <= 1:
        return liste

    pivot = liste[0]
    gauche = []
    droite = []

    # Partitionner la liste en deux sous-listes : les éléments inférieurs au pivot et les éléments supérieurs au pivot
    for i in range(1, len(liste)):
        if liste[i] < pivot:
            gauche.append(liste[i])
        else:
            droite.append(liste[i])

    # Trier récursivement les sous-listes gauche et droite, puis concaténer les résultats avec le pivot pour obtenir la liste triée finale
    return tri_rapide(gauche) + [pivot] + tri_rapide(droite)



def tri_arborescent(liste):
    # Fonction interne pour trier récursivement les éléments d'un tableau en les ajoutant dans un arbre binaire
    def tri_recursif(arbre, tableau):
        if tableau:
            arbre.append(tableau[0])
            tri_recursif(arbre, tableau[1:])
    
    # Fonction interne pour créer un arbre binaire à partir d'un tableau
    def creer_arbre(tableau):
        arbre = []
        tri_recursif(arbre, tableau)
        return arbre

    # Fonction interne pour parcourir récursivement un arbre binaire et fusionner ses sous-arbres triés
    def parcours_arbre(arbre):
        if len(arbre) == 1:
            return arbre
        fils_gauche = parcours_arbre(arbre[:len(arbre) // 2])
        fils_droit = parcours_arbre(arbre[len(arbre) // 2:])
        return fusion(fils_gauche, fils_droit)

    # Fonction interne pour fusionner deux arbres triés en un arbre trié
    def fusion(arbre_gauche, arbre_droit):
        fusion = []
        i, j = 0, 0
        while i < len(arbre_gauche) and j < len(arbre_droit):
            if arbre_gauche[i] < arbre_droit[j]:
                fusion.append(arbre_gauche[i])
                i += 1
            else:
                fusion.append(arbre_droit[j])
                j += 1
        fusion.extend(arbre_gauche[i:])
        fusion.extend(arbre_droit[j:])
        return fusion

    # Créer un arbre binaire à partir de la liste et parcourir l'arbre pour obtenir la liste triée finale
    arbre = creer_arbre(liste)
    return parcours_arbre(arbre)


def tri_a_peigne(liste):
    n = len(liste)
    gap = n
    swaps = True
    while gap > 1 or swaps:
        gap = max(1, int(gap / 1.25))  # Réduire le gap jusqu'à 1. On utilise 1.25 comme facteur pour le réduire.
        swaps = False
        for i in range(n - gap):
            if liste[i] > liste[i + gap]:  # Comparer les éléments distants de gap
                liste[i], liste[i + gap] = liste[i + gap], liste[i]
                swaps = True  # Indiquer qu'il y a eu un échange

    return liste
 

def tri_pair_impair(liste):
    trie = False
    while not trie:
        trie = True
        for i in range(0, len(liste) - 1, 2):  # Parcours des éléments pairs
            if liste[i] > liste[i+1]:
                liste[i], liste[i+1] = liste[i+1], liste[i]
                trie = False
        for i in range(1, len(liste) - 1, 2):  # Parcours des éléments impairs
            if liste[i] > liste[i+1]:
                liste[i], liste[i+1] = liste[i+1], liste[i]
                trie = False

    return liste



def tri_shell(liste):
    n = len(liste)
    # Déterminer l'intervalle d'écartement h
    h = 1
    while h < n // 3:
        h = 3 * h + 1

    # Continuer le tri tant que l'intervalle d'écartement est plus grand que 0
    while h > 0:
        for i in range(h, n):
            j = i
            while j >= h and liste[j] < liste[j-h]:
                liste[j], liste[j-h] = liste[j-h], liste[j]
                j -= h
        h //= 3

    return liste


# Fonction pour mesurer le temps d'exécution d'une fonction
def mesurer_temps_execution(fonc, *args):
    temps_depart = timeit.default_timer()
    fonc(*args)
    temps_arrivee = timeit.default_timer()
    return temps_arrivee - temps_depart


def plot_exec_temps(liste_entiers):
    # Mesurer le temps d'exécution pour chaque algorithme
    temps_tri_selection = mesurer_temps_execution(tri_selection, liste_entiers)
    temps_tri_insertion = mesurer_temps_execution(tri_insertion, liste_entiers)
    temps_tri_bulles = mesurer_temps_execution(tri_bulles, liste_entiers)
    temps_tri_cocktail = mesurer_temps_execution(tri_cocktail, liste_entiers)
    temps_tri_tas = mesurer_temps_execution(tri_tas, liste_entiers)
    temps_tri_pigeon = mesurer_temps_execution(tri_pigeon, liste_entiers)
    temps_tri_fusion = mesurer_temps_execution(tri_fusion, liste_entiers)
    temps_tri_rapide = mesurer_temps_execution(tri_rapide, liste_entiers)
    temps_tri_arborescent = mesurer_temps_execution(tri_arborescent, liste_entiers)
    temps_tri_a_peigne = mesurer_temps_execution(tri_a_peigne, liste_entiers)
    temps_tri_pair_impair = mesurer_temps_execution(tri_pair_impair, liste_entiers)
    temps_tri_de_shell = mesurer_temps_execution(tri_shell, liste_entiers)

    # Créer le graphique de barres
    data = [go.Bar(

    x=['Tri par sélection', 'Tri par insertion', 'Tri à bulles', 'Tri cocktail', 'Tri par tas',
    'Tri pigeon', 'Tri fusion', 'Tri rapide', 'Tri arborescent', 'Tri à peigne',
    'Tri pair-impair', 'Tri de Shell'],

    y=[temps_tri_selection, temps_tri_insertion, temps_tri_bulles, temps_tri_cocktail, temps_tri_tas,
    temps_tri_pigeon, temps_tri_fusion, temps_tri_rapide, temps_tri_arborescent, temps_tri_a_peigne,
    temps_tri_pair_impair, temps_tri_de_shell])]
    
    layout = go.Layout(
                title='Temps d\'exécution des algorithmes',
                xaxis={'title': 'Algorithmes','fixedrange':True},
                yaxis={'title': 'Temps d\'exécution','fixedrange':True},
                width=1900,  
                height=490
            )
    fig = go.Figure(data=data, layout=layout)

    return fig
