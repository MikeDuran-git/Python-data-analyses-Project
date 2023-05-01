# -*- coding: utf-8 -*-
"""
Created on Mon May  1 15:21:59 2023

@author: Khedoudja Rym Merad Mike Duran Ophélie Engasser

"""


"""
Instalation des libraries
"""
import importlib
import pkg_resources
import subprocess

libraries = ['pandas', 'matplotlib', 'numpy', 'seaborn', 'scipy', 'statsmodels']

for libname in libraries:
    # Vérifier si la bibliothèque est déjà installée
    if libname in [dist.project_name for dist in pkg_resources.working_set]:
        print(f"{libname} est déjà installé.")
    # Si la bibliothèque n'est pas installée, l'installer
    else:
        print(f"{libname} n'est pas installé. Installation en cours...")
        subprocess.call(['pip', 'install', libname])
        print(f"{libname} a été installé avec succès !")




"""
Importation des biliothèques 
"""
import csv
import pandas as pd
import matplotlib as plt 
import seaborn as sns
import numpy as np 
import statsmodels as stm
import scipy as sp



"""
Import des Données du sommeil
"""

with open('Projet.csv', 'r') as f:
    csv_reader = csv.reader(f)




