# -*- coding: utf-8 -*-
"""
Created on Mon May  1 15:21:59 2023

@author: Khedoudja Rym Merad Mike Duran Ophélie Engasser

"""


"""
Instalation des packages 
"""
#!pip install csv
#!pip install matplotlib


"""
Importation des biliothèques 
"""
import csv
import matplotlib as plt 
import seaborn as sns
import numpy as np 


"""
Import des Données du sommeil
"""

import csv

with open('Projet.csv', 'r') as f:
    csv_reader = csv.reader(f)
    for row in csv_reader:
        print(row)

