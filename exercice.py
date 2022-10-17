#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO: Importez vos modules ici
import numpy as np
from turtle import *
import random

# TODO: Définissez vos fonction ici
def calculer_volume_masse_ellipsoide(a=2, b=4, c=6, masse_volumique=1):
    volume = np.pi * a * b * c * 4 / 3
    masse = masse_volumique * volume

    return volume, masse

def frequence(chaine):
    historigramme = {}
    for char in set(chaine):
        if char.isalpha():
            historigramme[char] = chaine.count(char)

    return historigramme

def dessiner_une_branche(longueur, grosseur, angle):
    if longueur > 10:
        random.random()
        pensize(grosseur)
        forward(longueur)
        right(angle)
        dessiner_une_branche(longueur/(0.95+random.random()), grosseur/1.1, angle/1.25)
        left(angle*2)
        dessiner_une_branche(longueur/(0.95+random.random()), grosseur/1.1, angle/1.25)
        right(angle)
        backward(longueur)

def dessiner_arbre():
    setheading(90)
    color("green")
    dessiner_une_branche(100, 5, 35)
    done()

def adn_est_valide(chaine):
    char_valides = "atgc"
    for char in chaine:
        if char not in char_valides:
            return False
    return True

def saisie_adn(texte):
    print(texte)
    while True:
        saisie = input(">")
        if adn_est_valide(saisie):
            return saisie
        else:
            print("Entree invalide, reessayez:")

def analyse_adn():
    chaine = saisie_adn("Entrez une chaine d'ADN")
    sequence = saisie_adn("Entrez une sequence a quantifier dans la chaine")
    frequence = chaine.count(sequence) / (len(chaine)/len(sequence))
    print(f"Il y a {round(frequence*100,2)} % de {sequence} dans {chaine}")

if __name__ == '__main__':
    print((lambda sentence: sorted(frequence(sentence), key=frequence(sentence).__getitem__)[-1])("hvhvhjhjhjhjvjvvvvvvvvvvvvvvvvv"))
    analyse_adn()
    dessiner_arbre()
