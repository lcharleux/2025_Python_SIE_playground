# import numpy as np
import os
import pandas as pd
# import data_creation as dc


#cette fonction créé un dataframe à partir du fichier .csv et l'affiche
def recognize_amplitude_frequence (path_file : str):
    #identifie si le fichier .csv a déjà des headers : si oui, on les garde, si non, on les ajoute
    temp=pd.read_csv(path_file,sep=",", header=None)
    if temp.iloc[0,0]=="signal":
        data=pd.read_csv(path_file,sep=",", header=0)
    else:
        data=pd.read_csv(path_file,sep=",", header=None, names=["signal", "amplitude","frequence","noise"])

    dim=data.shape
    print(data)
    for i in range(dim[0]):
        print (f"Signal {data.iloc[i,data.columns.get_loc("signal")]} a une amplitude de {data.iloc[i,data.columns.get_loc("amplitude")]} et une fréquence de {data.iloc[i,data.columns.get_loc("frequence")]} ")


if __name__ == "__main__":
    #on récupère la liste des fichiers .csv dans un dossier donné
    liste_fichiers=os.listdir(r"C:\Users\BA251988\Documents\Python\cours_annecy")

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
    