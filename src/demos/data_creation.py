import numpy as np
import pandas as pd
from math import pi

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
# dc = DataCreator(amp = 3), index
# dc.create_data()

    

