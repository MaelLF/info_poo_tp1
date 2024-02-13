from tp1_ex3 import *   #Librairie de définition de la classe Triangle : relation de composition

#Auteur : Le Floch Mael
#Date de création : 7 Fevrier 2024

#Objectif du programme : Création d'une classe Object3D permettant :
# -l'affichage de la liste de triangle composant cet object
# -l'ajout de triangle à cette liste
# -le déplacement de l'objet selon un Vecteur passé en paramètre

# Création d'une classe couleur à 3 composants : r,g et b des entiers

class Couleur (object):
    def __init__(self,r,g,b):
        self.r = r
        self.g = g
        self.b = b

class Object3D (object):
    def __init__(self,centre_grav : Vecteur, couleur : Couleur) : #Définition de la classe et de ces composants une couleur, une liste de triangle et un centre de gravité
        self.centre_grav = centre_grav #relation d'agrégation à la classe Vecteur
        self.couleur = couleur  #relation de composition à la classe Couleur
        self.list_triangles = []    #relation de composition à la classe triangle

    def afficher (self): #Méthode d'affichage de la liste des triangles composants l'object
        for i in range(0,len(self.list_triangles)): #itération sur la liste des triangles
            self.list_triangles[i].afficher()   #s'appuie sur la méthode d'affichage des triangles de la classe Triangle

    def ajouterTriangle (self,newTriangle : Triangle) : #Méthode d'ajout d'un élément mis en paramètre à la liste de triangle
        self.list_triangles.append(newTriangle)
    
    def déplacer (self,v : Vecteur) :   #Méthode de déplacement des éléments de la liste de triangle selon un Vecteur  passé en paramètre
        for i in range(0,len(self.list_triangles)): #itération sur la liste des triangle
            self.list_triangles[i].deplacer(v)  #s'appuie sue la méthode déplacer de la classe Triangle
    
