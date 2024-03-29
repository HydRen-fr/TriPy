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



def tri_comptage(donnees):
            liste = [0] * (max(donnees) + 1)
            resultat = []
            for element in donnees:
                liste[element] += 1

            for index, element in enumerate(liste):
                if element != 0:
                    resultat.append(index)

            return resultat

def tri_gnome(liste):
        index = 0
        n = len(liste)
        while index < n:
            if index == 0:
                index = index + 1
            if liste[index] >= liste[index - 1]:
                index = index + 1
            else:
                liste[index], liste[index - 1] = liste[index - 1], liste[index]
                index = index - 1
        return liste


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
    temps_tri_pigeon = mesurer_temps_execution(tri_pigeon, liste_entiers)
    temps_tri_gnome = mesurer_temps_execution(tri_gnome, liste_entiers)
    temps_tri_comptage = mesurer_temps_execution(tri_comptage, liste_entiers)
    temps_tri_a_peigne = mesurer_temps_execution(tri_a_peigne, liste_entiers)
    temps_tri_de_shell = mesurer_temps_execution(tri_shell, liste_entiers)

    # Tri des temps d'exécution dans l'ordre croissant
    # Créer une liste de tuples (étiquette, temps) et trier les tuples par temps
    temps_croissants = sorted([
        ('Tri par sélection', temps_tri_selection),
        ('Tri par insertion', temps_tri_insertion),
        ('Tri à bulles', temps_tri_bulles),
        ('Tri cocktail', temps_tri_cocktail),
        ('Tri pigeon', temps_tri_pigeon),
        ('Tri gnome', temps_tri_gnome),
        ('Tri comptage', temps_tri_comptage),
        ('Tri à peigne', temps_tri_a_peigne),
        ('Tri de Shell', temps_tri_de_shell)
    ], key=lambda x: x[1])

    # Extraire les étiquettes triées et les temps triés dans des listes séparées
    x = [item[0] for item in temps_croissants]
    y = [item[1] for item in temps_croissants]

    # Créer le graphique de barres avec les étiquettes et les temps triés
    data = [go.Bar(x=x, y=y)]

    layout = go.Layout(
        title='Temps d\'exécution des algorithmes',
        xaxis={'title': 'Algorithmes', 'fixedrange': True},
        yaxis={'title': 'Temps d\'exécution', 'fixedrange': True},
        width=1900,
        height=490
    )

    fig = go.Figure(data=data, layout=layout)

    return fig

