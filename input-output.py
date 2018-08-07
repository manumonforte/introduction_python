# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 16:32:31 2018

@author: Manu
"""

#INPUT-OUTPUT

#%%

import os
#Create folder

os.makedirs("input-output/",exist_ok = True)

#%% 

#create txt

from pathlib import Path

folder = Path("input-output/")

numbers = [1,2,3,4,5,6,7,8,9,100000]
#%%       
def longestSentence():
    archive = open("input-output/list.txt","r")
    content = archive.readlines()
    maxTam = 0
    line = ""
    for lines in content:
        if(len(lines) > maxTam):
            maxTam = len(lines)
            line = lines
    return line

print(longestSentence())

#%%

def nLines(nombre,n):
    with open (nombre,"r") as fname:
        lineas = [linea.strip("\n") for linea in fname.readlines()]
        return lineas[-n:]
    
#%%

diccionario = {
        "edad": [12,13],
        "Nombre": ["Oskar","Lorenzo"]
        }

def csv(diccionario,archive):
    claves = diccionario.keys()
    items = len([claves[0]])
    with open(archive,"r") as fname:
        """writting keys in columns"""
        fname.write(",".join(claves))
        """writting \n"""
        fname.write("\n")
        """writting values in columns"""
        for i in range(items):
            line = ",".join(str(diccionario[clave][i]) for clave in claves)
            fname.write(line,"\n")

            
