import math
from tp1_ex2 import Vecteur #Librairie de définition de la classe Vecteur : relation de composition

#Auteur : Le Floch Mael
#Date de création : 7 Fevrier 2024

#Objectif du programme : Création d'une classe Triangle permettant :
# -le déplacement du triangle selon un Vecteur passé en argument
# -la rotation du Triangle autour de son axe z d'un angle alpha
# -l'affichage des composants du Triangle

class Triangle (object):
    def __init__(self,a:Vecteur,b:Vecteur,c:Vecteur):   #Définition de la classe et de ces composants trois veccteurs : point1, point2 et point3
        self.point1=a
        self.point2=b
        self.point3=c

    def tourner (self,alpha):   #Méthode de rotation du Triangle autour de son axe z d'un angle alpha
        self.point1=self.point1.tourner(alpha)  #s'appuie sur la définition de la méthode tourner de la classe Vecteur
        self.point2=self.point2.tourner(alpha)
        self.point3=self.point3.tourner(alpha)

    def afficher (self):    #Méthode d'affichage des points composants le rectangle
        self.point1.afficher() #s'appuie sur la définition de la méthode afficher de la classe Vecteur
        self.point2.afficher()
        self.point3.afficher()
    
    def deplacer (self,v:Vecteur):  #Méthode de déplacement du Triangle selon un vecteur v passé en argument
        self.point1=self.point1.additionner(v)  #s'appuie sur la définition de la méthode additionner de la classe Vecteur
        self.point2=self.point2.additionner(v)
        self.point3=self.point3.additionner(v)