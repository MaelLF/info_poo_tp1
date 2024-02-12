from tp1_ex5 import *

#Auteur : Le Floch Mael
#Date de création : 7 Fevrier 2024
#Objectif :Test pour l'exercice 5 du TP1'

def main() :

    #Test dé :

    #dé1= Dé()
    #dé1.lancer()
    #print('valeur dé :',dé1.valeur)

    #Test joeur :

    #j1 =Joueur()
    #j1.affiche_dé()
    #j1.lancer_joueur()
    #j1.affiche_dé()
    #j1.relancer_joueur()

    #Test jeu avec deux joueurs sur dix manches:
    
    jeu =Jeu()
    jeu.ajouter_joueur()
    for i in range (0,10) :
        jeu.result()

if __name__ == '__main__':
    main()