# DATAPROC

import numpy as np
import pandas as pd
from math import pi
import json

from scipy.optimize import curve_fit

def say_hi():
    out = "Hi buddies"
    print(out)
    return out

class DataCreator:
    #créer la fonction du signal
    def func (t,amp,freq):
        x = amp * np.cos(2* pi * freq * t)
        return x
    
    def __init__(self, amp = 5, freq = 2, noise=0.1, duration=10.):
        self.amp = amp
        self.freq = freq
        self.noise = noise
        self.duration = duration

    def __repr__(self):
        amp = self.amp
        freq = self.freq
        noise = self.noise
        duration = self.duration
        return f"<DataCreator: freq={freq}, amp={amp}, noise={noise}, duration={duration}>"
    
    def create_data(self):
        amp = self.amp
        freq = self.freq
        noise = self.noise
        duration = self.duration
        t = np.linspace(0., duration, 1000)
        x = self.func (t, amp, freq) 
        x += noise * np.random.randint(0, 1, size=1000)
        self.data = {"t":t, "x":x}

    def To_CSV(self, path = "data.csv"):
        data = self.data
        pd.DataFrame(data).to_csv(path, index=False)

class BatchCreator:
    def __init__(self, metadata = {}):
        self.data = []
        self.metadata = metadata
    
    def create_data(self, ntests = 1):
        for i in range(ntests):
            self.data.append(DataCreator(**self.metadata))
    
    def to_csv(self, workdir = "./"):
        for i, d in enumerate(self.data):
            d.create_data()
            pos = str(i).zfill(3)
            path = f"{workdir}data_{pos}.csv"
            d.To_CSV(path=path)

    
    def dump_metadata(self, workdir = "./"):
        md = self.metadata
        with open(f"{workdir}metadata.json", "w") as f:
            f.write(json.dumps(md))



def recognize_amplitude_frequence (path_file : str):
    #identifie si le fichier .csv a déjà des headers : si oui, on les garde, si non, on les ajoute
    temp=pd.read_csv(path_file,sep=",", header=None)
    if temp.iloc[0,0]=="t":
        data=pd.read_csv(path_file,sep=",", header=0)
    else:
        data=pd.read_csv(path_file,sep=",", header=None, names=["t", "x"])

    dim=data.shape
    print(data)
    #lire les données et les afficher sous forme de phrases
    for i in range(dim[0]):
        t=data.iloc[i,data.columns.get_loc("t")]
        x=data.iloc[i,data.columns.get_loc("x")]
        print (f"Signal {i} au temps {t} a une valeur de {x} ")



class Plotter:
    def __init__(self, x=None, y=None):
        self.x = x
        self.y = y

    def set_labels(self, xlabel, ylabel):
        self.xlabel = xlabel
        self.ylabel = ylabel
    def plot(self):
        plt.plot(self.x, self.y)
        plt.show()
    def save(self,name="plot.png"):
        plt.plot(self.x, self.y)
        plt.savefig(name)
