import math

#Auteur : Le Floch Mael
#Date de création : 7 Fevrier 2024

#Objectif du programme : Création d'une classe Vecteur permettant :
# -l'addition et le produit scalaire du Vecteur de référence à un autre élément du même type,
# -le calcul de la Norme du vecteur
# -la rotation du vecteur autour de son axe z d'un angle alpha
# -l'affichage des composants du vecteur

class Vecteur (object):
    def __init__(self,x=0,y=0,z=0): #Définition des composants de la classe : x, y et z. Par défaut mis à zéro.
        self.x=x
        self.y=y
        self.z=z
    
    def additionner(self,v) : #Méthode d'addition du Vecteur à un autre Vecteur mis en paramètre (v)
        return Vecteur(self.x + v.x,self.y + v.y,self.z + v.z)
    
    def calculerNorme(self):  #Méthode de calcul de la norme du Vecteur
        return math.sqrt(self.x**2+self.y**2+self.z**2)
    
    def calculerProduitScalaire (self,v):   #Méthode de calcul du produit scalaire du Vecteur à un autre Vecteur mis en paramètre (v)
        return (self.x * v.x) + (self.y * v.y) + (self.z * v.z)
    
    def tourner (self,alpha) :  #Méthode de rotation du Vecteur autour de z selon un angle alpha
        return Vecteur(self.x*math.cos(alpha)-self.y*math.sin(alpha),self.y*math.cos(alpha)+self.x*math.sin(alpha),self.z)
    
    def afficher (self): #Méthode d'affichage des composants de la classe Vecteur
        print("Coordonées du vecteur:",self.x,self.y,self.z)