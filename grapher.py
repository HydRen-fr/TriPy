import matplotlib
matplotlib.use('agg')
import os
import sys
import matplotlib.pyplot as plt
from celluloid import Camera

class Plotter():
    def __init__(self, title):
        self.title = title
        self.fig = plt.figure()
        self.ax = plt.axes()
        self.ax.get_xaxis().set_visible(False)
        self.ax.get_yaxis().set_visible(False)
        self.camera = Camera(self.fig)

    def plot(self, data, first_highlight, second_highlight=None):
        self.data = data
        self.length = len(data)
        colours = list('b'*self.length)

        colours[first_highlight] = 'r'
        if second_highlight is not None:
            colours[second_highlight] = 'g'

        plt.bar(list(range(self.length)), data, color=colours)
        plt.title(self.title)
        self.ax.get_xaxis().set_visible(False)
        self.ax.get_yaxis().set_visible(False)
        self.camera.snap()

    def animate(self, data, interval=200):
        colours = list('g'*len(data))
        plt.bar(list(range(len(data))), data, color=colours)
        plt.title(self.title)
        self.ax.get_xaxis().set_visible(False)
        self.ax.get_yaxis().set_visible(False)
        self.camera.snap()
        return self.camera.animate(repeat=False,interval=interval).to_html5_video()
        plt.close()
