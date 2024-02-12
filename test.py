from tp1_ex1 import *
from tp1_ex2 import *
from tp1_ex3 import *
from tp1_ex4 import *
from tp1_ex5 import *

#Auteur : Le Floch Mael
#Date de création : 7 Fevrier 2024
#Objectif :Test pour les 4 premiers exercices du TP1

def main():

    #exo1
    x=Algèbre()
    n = int(input())
    print('somme :', x.somme_n(n))
    print(x.somme_n(-1))
    print('factorielle :',x.facto_n(n))

    #exo 2
    a=Vecteur(1,2,2)
    b=Vecteur(2,3,4)
    c=a.additionner(b)
    print("Addition de vecteur",c.x,c.y,c.z)
    print("Norme:",a.calculerNorme())
    print("Produit scalaire",a.calculerProduitScalaire(b))
    
    v = Vecteur(1, 0, 0)

    alpha = math.radians(90)
    result = v.tourner(alpha)
    print(f"Original Vecteur: ({v.x}, {v.y}, {v.z})")
    print(f"Rotated Vecteur: ({result.x}, {result.y}, {result.z})")
    a.afficher()

    #exo3
    point_a = Vecteur(1, 2, 3)
    point_b = Vecteur(4, 5, 6)
    point_c = Vecteur(7, 8, 9)
    triangle = Triangle(point_a, point_b, point_c)

    
    print("Original Triangle:")
    triangle.afficher()

    
    alpha = math.radians(45)
    triangle.tourner(alpha)

    
    print("\nRotated Triangle:")
    triangle.afficher()

    
    translation_vector = Vecteur(1, 1, 1)
    triangle.deplacer(translation_vector)

    
    print("Translated Triangle:")
    triangle.afficher()

    #exo4
    couleur = Couleur(255, 0, 0)

    # Create a 3D object with a center of gravity and color
    centre_grav = Vecteur(1, 2, 3)
    obj3d = Object3D(centre_grav, couleur)

    # Create three Triangles
    triangle1 = Triangle(Vecteur(0, 0, 0), Vecteur(1, 0, 0), Vecteur(0, 1, 0))
    triangle2 = Triangle(Vecteur(1, 0, 0), Vecteur(1, 1, 0), Vecteur(0, 1, 0))
    triangle3 = Triangle(Vecteur(0, 0, 0), Vecteur(1, 0, 0), Vecteur(0, 0, 1))

    # Add the Triangles to the 3D object
    obj3d.ajouterTriangle(triangle1)
    obj3d.ajouterTriangle(triangle2)
    obj3d.ajouterTriangle(triangle3)

    # Display the original 3D object
    print("Original 3D Object:")
    print("Nombre d'objet:",len(obj3d.list_triangles))
    obj3d.afficher()

    # Move the 3D object by a vector (1, 1, 1)
    translation_vector = Vecteur(2, 1, 20)
    obj3d.déplacer(translation_vector)

    # Display the translated 3D object

    #Test dé :
    dé1= Dé()
    dé1.lancer()
    print('valeur dé :',dé1.valeur)



if __name__ == '__main__':
    main()