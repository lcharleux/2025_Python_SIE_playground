# DATAPROC

import numpy as np
import pandas as pd
from math import pi

def say_hi():
    out = "Hi buddies"
    print(out)
    return out

class DataCreator:
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
        x = amp * np.cos(2* pi * freq * t) 
        x += noise * np.random.randint(0, 1, size=1000)
        self.data = {"t":t, "x":x}

    def To_CSV(self):
        data = self.data
        pd.DataFrame(data).to_csv("data.csv", index=False)


def recognize_amplitude_frequence (path_file : str):
    #identifie si le fichier .csv a déjà des headers : si oui, on les garde, si non, on les ajoute
    temp=pd.read_csv(path_file,sep=",", header=None)
    if temp.iloc[0,0]=="t":
        data=pd.read_csv(path_file,sep=",", header=0)
    else:
        data=pd.read_csv(path_file,sep=",", header=None, names=["t", "x"])

    dim=data.shape
    print(data)
    for i in range(dim[0]):
        t =data.iloc[i,data.columns.get_loc("t")]
        x=data.iloc[i,data.columns.get_loc("x")]
        print (f"Signal {i} au temps {t} a une valeur de {x} ")