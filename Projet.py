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

df = pd.read_csv("C:/Users/Engasser Ophélie/Desktop/Python-data-analyses-Project/Projet.csv")

print(df.head())


# vérification de la structure du dataset et des types de données
print(df.shape)
print(df.info())

# analyse univariée var. sleep efficiency, REM sleep, deep sleep, light sleep, awakenings

# ---- sleep efficiency ----
# sleep efficiency est une mesure de la qualité du sommeil exprimée sous forme de coefficient (théoriquement allant de 0 à 1)

print(df['Sleep efficiency'].describe().round(4))

# la distribution de l'échantillon s'étale de 0.5 (min) à 0.99 (max)
# moyenne 0.79, écart-type 0.13
# médiane 0.82
# 50% des sujets (intervalle inter-quartiles) ont une qualité de sommeil entre 0.7 et 0.9

# coefficient de variation
sd_sleep_efficiency = np.std(df['Sleep efficiency'], ddof=1) # écart-type non biaisé puisque nous le calculons sur l'échantillon
coef_variation_sleep_efficiency = sd_sleep_efficiency / df['Sleep efficiency'].mean() * 100
print(coef_variation_sleep_efficiency)

# le CV est faible et < 50% ce qui reflète une homogénéité de notre échantillon sur cette variable

# vérification des NaN
print(df['Sleep efficiency'].isna().sum()) 

# visualisons la distribution sur un boxplot et un density plot (avec plt)
print(plt.figure(figsize=(10, 5)))

plt.subplot(121)
df['Sleep efficiency'].plot(kind="box") # sns.boxplot(df['Sleep efficiency'])

plt.subplot(122)
df['Sleep efficiency'].plot(kind="density") # sns.kdeplot(df['Sleep efficiency'])

plt.show()

# sur le boxplot : pas d'outlier
# sur la courbe de densité : forme asymétrique (majorité des données à droite de la moyenne), vérifions cela avec les paramètres de forme

# skewness pour l'asymétrie
print(df['Sleep efficiency'].skew())

# skewness < 0 :
# la densité est inégalement répartie autour de la moyenne, la courbe est effectivement skewed à gauche (la moajorité des données à droite de la moy)
# cela signifie que la majorité de la population présente une qualité de sommeil plutôt bonne

# kurtosis pour l'aplatissement
df['Sleep efficiency'].kurtosis()

# kurtosis < 3 :
# la courbe est plus aplatie que la courbe de Gauss, càd que l'échantillon s'étale davantage autour de la moy

# vérifions avec le test de Shapiro-Wilk si cette variable suit une loi normale 
stat, p = shapiro(df['Sleep efficiency'])
print(stat, p)

# la statistique de test W est signiticative (p<.01) donc on rejette H0, la variable n'est pas distribuée normalement, et nous pouvons affirmer cela avec un degré très faible de nous tromper
# cela signifie que d'autres facteurs que le hasard, interviennent dans la qualité du sommeil de nos sujets, et nous allons vérifier lesquels sont déterminants 

# ---- REM sleep percentage ----
# le REM-sleep ou sommeil paradoxal est la phase du sommeil du rêve, caractérisée par une forte activité cérébrale et des ondes rapides avec des mouvements oculaires rapides 
# d'où le nom Rapid Eyes Movements (REM) et une complète atonique musculaire
# le REM-sleep est une phase de consolidation des souvenirs en mémoire à long terme et est donc responsable de la digestion des événements de vie et des émotions
# la part de REM-sleep augmente en cours de nuit, pour atteindre son max en fin de nuit
# ici il est mesuré en % càd la proportion de REM-sleep pendant une nuit d'un sujet (relativement aux autres stades de sommeil)
# pour un sujet moyen la phase de REM-sleep représente en moyenne 20% du temps de sommeil
# nous avons vérifié et chaque stade de sommeil additionné pour chaque sujet = 100%

df['REM sleep percentage'].describe().round(4)

# la distribution de l'échantillon s'étale de 15% (min) 30% (max)
# moyenne 22.61, écart-type 3.52%
# médiane 22%
# 50% des sujets (intervalle inter-quartiles) ont une proportion de REM-sleep entre 20 et 25% par nuit

# coefficient de variation
sd_rem_sleep = np.std(df['REM sleep percentage'], ddof=1) # écart-type non biaisé puisque nous le calculons sur l'échantillon
coef_variation_rem_sleep = sd_rem_sleep / df['REM sleep percentage'].mean() * 100
coef_variation_rem_sleep

# le CV est faible et < 50% ce qui reflète une homogénéité de notre échantillon sur cette variable

# vérification des NaN
df['REM sleep percentage'].isna().sum() 

# visualisons la distribution sur un boxplot et un density plot
plt.figure(figsize=(10, 5))

plt.subplot(121)
df['REM sleep percentage'].plot(kind="box") # sns.boxplot(df['REM sleep percentage'])

plt.subplot(122)
df['REM sleep percentage'].plot(kind="density") # sns.kdeplot(df['REM sleep percentage'])

plt.show()

# sur le boxplot : pas d'outlier
# sur la courbe de densité : forme asymétrique (majorité des données à gauche de la moyenne), vérifions cela avec les paramètres de forme

# skewness pour l'asymétrie
df['REM sleep percentage'].skew()

# skewness > 0 :
# la densité est inégalement répartie autour de la moyenne, la courbe est effectivement skewed à droite (la moajorité des données à gauche de la moy)
# cela signifie que la majorité de la population présente une proportion de REM-sleep en-deçà de la moy

# kurtosis pour l'aplatissement
df['REM sleep percentage'].kurtosis()

# kurtosis < 3 :
# la courbe est plus aplatie que la courbe de Gauss, càd que l'échantillon s'étale davantage autour de la moy (mais cela me paraît bizarre car la courbe a l'air pointue visuellement)

# vérifions avec le test de Shapiro-Wilk si cette variable suit une loi normale 
stat, p = shapiro(df['REM sleep percentage'])
print(stat, p)

# la statistique de test W est signiticative (p<.01) donc on rejette H0, la variable n'est pas distribuée normalement, et nous pouvons affirmer cela avec un degré très faible de nous tromper
# cela signifie que d'autres facteurs que le hasard, interviennent dans l'apparition et la durée du REM-sleep (ce sont des facteurs physiologiques, sociaux, hygiène de vie qui le déterminent)

# ---- Deep sleep percentage ----
# le sommeil lent profond est un stade pendant lequel il est difficile de réveiller le dormeur
# le stade est caractérisé par une régénération des cellules et du corps, les ondes cérébrales sont lentes
# la mesure est la même que pour le REM-sleep (% de temps par rapport aux autres stades)
# un sujet moyen passe 25% de son temps de sommeil en sommeil lent profond

df['Deep sleep percentage'].describe().round(4)

# la moyenne et la médiane semblent élevées

# coefficient de variation
sd_deep_sleep = np.std(df['Deep sleep percentage'], ddof=1) # écart-type non biaisé puisque nous le calculons sur l'échantillon
coef_variation_deep_sleep = sd_deep_sleep / df['Deep sleep percentage'].mean() * 100
coef_variation_deep_sleep

# le CV est < 50% ce qui reflète une homogénéité de notre échantillon sur cette variable

# vérification des NaN
df['Deep sleep percentage'].isna().sum() 

# visualisons la distribution sur un boxplot et un density plot
plt.figure(figsize=(10, 5))

plt.subplot(121)
df['Deep sleep percentage'].plot(kind="box") # sns.boxplot(df['Deep sleep percentage'])

plt.subplot(122)
df['Deep sleep percentage'].plot(kind="density") # sns.kdeplot(df['Deep sleep percentage'])

plt.show()

# sur le boxplot : il y a des outliers qui ont un % bas de deep sleep
# sur la courbe de densité : forme bimodale

# skewness pour l'asymétrie
df['Deep sleep percentage'].skew()

# skewness < 0 :
# la densité est inégalement répartie autour de la moyenne, il y a plus de données à droite de la moy

# kurtosis pour l'aplatissement
df['Deep sleep percentage'].kurtosis()

# kurtosis < 3 :
# courbe plus aplatie

# vérifions avec le test de Shapiro-Wilk si cette variable suit une loi normale 
stat, p = shapiro(df['Deep sleep percentage'])
print(stat, p)

# même conclusion que pour le REM-sleep

# ---- Light sleep percentage ----
# il s'agit d'un stade de sommeil lent léger, pendant lequel le dormeur entre progressivement dans le sommeil profond, il peut être réveillé plus facilement
# physiologiquement, les ondes cérébrales sont plus rapides
# en moyenne cela représente environ la moitié du temps de sommeil généralement
# même mesure que pour les 2 précédantes variables

df['Light sleep percentage'].describe().round(4)

# ici la moyenne et la médiane me semblent anormalement basses

# coefficient de variation
sd_light_sleep = np.std(df['Light sleep percentage'], ddof=1) # écart-type non biaisé puisque nous le calculons sur l'échantillon
coef_variation_light_sleep = sd_light_sleep / df['Light sleep percentage'].mean() * 100
coef_variation_light_sleep

# le CV est > 50% ce qui reflète une hétérogénéité de notre échantillon sur cette variable

# vérification des NaN
df['Light sleep percentage'].isna().sum() 

# visualisons la distribution sur un boxplot et un density plot
plt.figure(figsize=(10, 5))

plt.subplot(121)
df['Light sleep percentage'].plot(kind="box") # sns.boxplot(df['Light sleep percentage'])

plt.subplot(122)
df['Light sleep percentage'].plot(kind="density") # sns.kdeplot(df['Light sleep percentage'])

plt.show()

# sur le boxplot : il y a des outliers qui ont un % + élevé de light sleep
# sur la courbe de densité : forme bimodale

# skewness pour l'asymétrie
df['Light sleep percentage'].skew()

# skewness > 0 :
# la densité est inégalement répartie autour de la moyenne, il y a plus de données à gauche de la moy

# kurtosis pour l'aplatissement
df['Light sleep percentage'].kurtosis()

# kurtosis < 3 :
# courbe plus aplatie

# vérifions avec le test de Shapiro-Wilk si cette variable suit une loi normale 
stat, p = shapiro(df['Light sleep percentage'])
print(stat, p)

# idem

# ---- Awakenings ----
# il s'agit du nb de réveils nocturnes (on ne sait pas si ce sont des réveils conscients ou des micro réveils)
# exprimés en unités mais type de données float

df['Awakenings'].describe().round(4)

# coefficient de variation
sd_awakenings = np.std(df['Awakenings'], ddof=1) # écart-type non biaisé puisque nous le calculons sur l'échantillon
coef_variation_awakenings = sd_awakenings / df['Awakenings'].mean() * 100
coef_variation_awakenings

# très > à 50% donc importante hétérogénéité dans les données de l'échantillon

# vérification des NaN
df['Awakenings'].isna().sum() 

# visualisons la distribution sur un boxplot et un density plot
plt.figure(figsize=(10, 5))

plt.subplot(121)
df['Awakenings'].plot(kind="box") # sns.boxplot(df['Awakenings'])

plt.subplot(122)
df['Awakenings'].plot(kind="density") # sns.kdeplot(df['Awakenings'])

plt.show()

# sur le boxplot : pas d'outliers mais un IIQ très large
# sur la courbe de densité : forme étalée

# skewness pour l'asymétrie
df['Awakenings'].skew()

# > 0 donc plus de données à gauche

# kurtosis pour l'aplatissement
df['Awakenings'].kurtosis()

# < 3 donc plus étalée et aplatie

# vérifions avec le test de Shapiro-Wilk si cette variable suit une loi normale 
df_clean = df.dropna()
stat, p = shapiro(df_clean['Awakenings'])
print(stat, p)

# même conclusion

