import random

#Auteur : Le Floch Mael
#Date de création : 7 Fevrier 2024

#Objectif du programme : Création d'une classe Jeu permettant :
# -l'affichage des score des différents joueurs
# -l'ajout d'un joueur à la liste des joueurs
# -la simulation d'une manche de 421 et la mise à jour des points des différents joueurs selon les résultats de cette manche



class Dé (object):  #Définition de la classe Dé
    def __init__(self): #Définition des composants de la classe (la valeur du dé), par défaut une valeur inategnable : 0
        self.valeur = 0
    def lancer (self):  #Méthode de lancer du dé qui met à jour la valeur de la classe
        self.valeur = random.randint(1,6)




class Joueur (object) : #Définition de la classe Joueur : Hérédité à la classe Dé
    def __init__(self,dé1 = Dé(),dé2 = Dé(), dé3 = Dé()):   #Définition des composants de la classe trois dé initialisé à 0 par défaut, une liste de valeur des dé et les points
        self.déliste=[dé1,dé2,dé3]
        self.result=[0,0,0]
        self.points = 0
    
    def lancer_joueur (self):   #Méthode de lancer des dé de l'objet joueur et mise à jour de son tableau de résultat
        for i in range (0, len(self.déliste)):
            self.déliste[i].lancer()
            self.result[i]=self.déliste[i].valeur
    
    def relancer_joueur (self): #Méthode de relance d'un joueur (il ne peur relancer que deux dé et jamais le meme)
        choix = -2  #Choix du joueur
        islocked = -2 #Choix au tour précédent du joueur
        i = 0   #nombre de tours 
        for i in range (0,2) :
            while choix == islocked :   #tant que le choix n'est pas identique au tour précédant
                choix = int(input("Quel dé voulez vous relancer [1 2 3] -1?  "))   #-1 : ne rien relancer
            if choix != -1 :    #si relance
                self.déliste[choix-1].lancer()
                print('la nouvelle valeur du dé N°',choix,'est',self.déliste[choix-1].valeur)
                self.result[choix-1]=self.déliste[choix-1].valeur   #relance seulement le dé selectioné
                self.affiche_dé()
                islocked = choix #choix à ne pas faire au tour suivant
            else : #si pas de relance au tour 1 on sort de la boucle
                break

    def affiche_dé (self):  #Méthode d'affichage des dé du Joueur
        print('Vos dé sont :',self.result[0],self.result[1],self.result[2])






class Jeu (object): #Définition de la Classe Jeu
    def __init__(self,j = Joueur()) :   #Initialisation des composant de la classe Jeu : Une liste de Joueur, initialisé à 1 Joueur au début
        self.liste_joueur = [j]
    
    def ajouter_joueur (self,j=Joueur()):  #Méthode d'ajout de joueur passé en argument
        self.liste_joueur.append(j)
    
    def result (self):     #Méthode de simulation d'une manche de 421
        i=1
        for joueur in self.liste_joueur :   #itération sur la liste de Joueur
            print('Cest au joueur',i,'de joueur')
            joueur.lancer_joueur()  #premier jet du Joueur
            joueur.affiche_dé()
            joueur.relancer_joueur()    #relance possible du Joueur
            res = sorted(joueur.result) #On trie le résultat
            print(res[0],res[1],res[2])

            if res==[4,5,6]:
                joueur.points += 2
            elif res.count(1)==2:   #si deux fois 1 alors on ajoute la troisième valeur de "result"
                joueur.points += res[2]
            elif res==[1,2,4]:
                joueur.points += 10
            i+=1
        self.tableau_score() # A la fin du tour on affiche le score des joueurs

    def tableau_score(self):    #Méthode d'affichage des scores
        i=0
        for joueur in self.liste_joueur :   #Itération sur la liste des joueurs
            i+=1
            print('joueur N' ,i, 'point', joueur.points)
        
