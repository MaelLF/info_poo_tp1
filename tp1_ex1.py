import math

#Auteur : Le Floch Mael
#Date de création : 7 Fevrier 2024

#Objectif du programme : Création d'une classe Algèbre permettant la somme des n premiers entiers et de factoriel de n

class Algèbre (object): #Définition de la classe
    def __init__(self): #La classe algèbre n'a pas de composants
        pass

    def somme_n(self,n):    # Méthode de somme des n premiers entiers
        sum=0
        if n>0 :    # si n positif on traite la requête
            sum = (n*(n+1))/2
        else :      #gestion de l'erreur si n négatif
            sum = -1
        return sum
    
    def facto_n(self,n):    #Méthode de factoriel de n
        if n == 0 :
            return 1    #Cas de base de la récursivité
        else :
            return n * self.facto_n(n-1)    #Cas dans tout les autres appels à la fonction
        
