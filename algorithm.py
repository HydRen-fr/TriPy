import random
from grapher import Plotter

def create(algorithm_name, data):
    if algorithm_name == 'selection':
        sort_algo = SelectionSort(data)
    elif algorithm_name == 'insertion':
        sort_algo = InsertionSort(data)
    elif algorithm_name == 'bubble':
        sort_algo = BubbleSort(data)
    else:
        sort_algo = SelectionSort(data)

    return sort_algo

def set_random_array(length):
    array = [random.randint(10, 200) for i in range(length)]
    random.shuffle(array)
    return array

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