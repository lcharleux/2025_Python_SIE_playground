# import numpy as np
import os
import pandas as pd
# import data_creation as dc
from dataproc.core import recognize_amplitude_frequence

#cette fonction créé un dataframe à partir du fichier .csv et l'affiche



if __name__ == "__main__":
    #on récupère la liste des fichiers .csv dans un dossier donné
    liste_fichiers=os.listdir(r"../doc/data_processing/data")
   

    # liste_fichiers_csv=[]

    # for element in liste_fichiers:
    #     if not element.endswith(".csv"):
    #         continue        
    #     liste_fichiers_csv.append(element)

    liste_fichiers_csv = [element for element in liste_fichiers if element.endswith(".csv")]
    print(liste_fichiers_csv)

    #on applique la fonction sur tous les fichiers .csv pour en faire des dataframes
    for element in liste_fichiers_csv:
        recognize_amplitude_frequence(element)
    