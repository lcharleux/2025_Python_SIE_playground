import matplotlib.pyplot as plt
import numpy as np

class Plotter:
    def __init__(self, x=None, y=None):
        self.x = x
        self.y = y

    def plot(self):
        plt.plot(self.x, self.y)
        plt.show()