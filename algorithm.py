import random
from grapher import Plotter

# Fonction qui crée l'objet de tri en fonction de l'algorithme choisi et des données à trier
def create(algorithm_name, data):
    # Sélection de l'algorithme en fonction de son nom
    if algorithm_name == 'selection':
        sort_algo = SelectionSort(data)
    elif algorithm_name == 'insertion':
        sort_algo = InsertionSort(data)
    elif algorithm_name == 'bubble':
        sort_algo = BubbleSort(data)

    # Si l'algorithme n'est pas reconnu, on utilise le tri par sélection par défaut   
    else:
        sort_algo = SelectionSort(data)

    return sort_algo

# Fonction qui génère un tableau de données aléatoires de longueur donnée
def set_random_array(length):
    # Création d'un tableau de longueur "length" avec des valeurs aléatoires entre 10 et 200 car 1 était trop minuscule sur le graphe
    array = [random.randint(10, 200) for i in range(length)]
    # Mélange
    random.shuffle(array)
    return array


# Chaque class a le même fonctionnement
# Initialisation de la classe Plotter pour afficher les graphes
# Tri du tableau avec l'algorithme qui correspond à la class
# On récupère la vidéo à afficher

class SelectionSort():
    def __init__(self,data):
        self.plotter = Plotter("Tri par sélection") 
        self.selection_sort(data)
        self.video = self.plotter.animate(data)

    def selection_sort(self,data):
        for i in range(len(data)): 
            minimum = i 
            for j in range(i+1, len(data)): 
                if data[minimum] > data[j]: 
                    minimum = j         
            self.plotter.plot(data,minimum,i)
            data[i],data[minimum] = data[minimum],data[i] 
            self.plotter.plot(data,i,minimum)
        return data

class InsertionSort():
    def __init__(self,data):
        self.plotter = Plotter("Tri par insertion") 
        self.insertion_sort(data)
        self.video = self.plotter.animate(data)

    def insertion_sort(self,data):
        for i in range(len(data)):
            temp = data[i]
            j = i-1
            while  j >=0 and temp < data[j]:
                self.plotter.plot(data,j+1,j)

                data[j+1] = data[j]
                data[j] = temp

                self.plotter.plot(data,j,j+1)

                j -= 1

            data[j+1] = temp

        return data
    
class BubbleSort():
    def __init__(self,data):
        self.plotter = Plotter("Tri à bulles") 
        self.bubble_sort(data)
        self.video = self.plotter.animate(data)

    def bubble_sort(self,data):
        for i in range(len(data)):
            for j in range(0,len(data)-i-1):
                self.plotter.plot(data,j+1,j)
                if data[j+1]<data[j]:
                    data[j],data[j+1]=data[j+1],data[j]
                    self.plotter.plot(data,j,j+1)
        return data