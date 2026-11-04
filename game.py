from pymongo import MongoClient
import random
client = MongoClient("mongodb://localhost:27017")
db = client["jeub2-b"]
collection = db["jeu"]


print("1- démarrer une partie")
print("2- quitter le jeu")
#afficher le choix du joueur 
    # 1- démarrer une partie
    # 2- quitter le jeu 

#while True:
#    choix = input("Ton choix (1-2): ") TODO
#    if choix.isdigit() and 1<=int(choix) <=2: TODO
#        choix = int(choix) TODO
#        break TODO
#    print("choix invalide, veuillez rentrer le bon numéro") TODO


def recuperer_choix_joueur(min_value, max_value):
    while True :
        choix = input()
        if verifier_choix_valide(choix):
            return int(choix)
        else :
            print("veuillez entrer un numéro valide!!")


def verifier_choix_valide(a_verifier, minimum,maximum):
    # si pas un chiffre
    #   return false
    # si minimum <= averifier et maximum >= averifier
    #   return true
    # return false
    if not a_verifier.isdigit():
        return False
    if minimum <= a_verifier and maximum >= a_verifier:
        return True 
    return False
    


choix = recuperer_choix_joueur(1,2)


#récuperer le choix du joueur 
#   boucle infini
#       input()
#       verifier si le choix est valide
#       si choix valide
#           retourner int(choix)
#       sinon
#           afficher ("veuillez rentrer un numéro valide !!")
#si choix 1
    # dire au joueur de creer equipe
        #récupérer la liste des personnages
        #tant que taille équipe < 3
            #afficher au joueur la liste de personnage disponible     
            #choix du joueur
                #récuperer le choix du joueur
                #si joueur prend un personnage
                    #enlever le personnage de la liste
                    #mettre le personnage pris dans equipe



def commencer(equipe):  

    #commencer un combat (equipe)
        #récupérer trois monstre 
            #random entre 3 monstre 
    monsters = select_monsters(3)

    while not est_equipe_en_vie(monsters) or not est_equipe_en_vie(equipe):
            tour_joueur()
            for i in [equipe]:
                random.choice(monsters)
                for each in [monsters]:
                    if en_vie:
                        +1 in est_equipe_en_vie
                    return True
                
            tour_equipe_monsters()
        
        #boucle jusqu'a ce que not equipe_en_vie(monstre) ou not equipe_en_vie(equipe) 
            #tour du joueur 
                # recuperer membres en vie
                # pour chaque membre en vie 
                    # attaquer monstre en vie au hasard
                        # recuperer les monstres en vie a partir de la liste des monstres
                            # pour chaque mosntre
                                # verifier si en vie
                                # si en vie 
                                    # ajoute a la liste en_vie
                            # renvoyer en_vie
                        # random sur les monstres en vie
            #tour de l'équipe de monstre
                    #monstre attaque un personnage dans l'équipe du joueur 




    #si le joueur gagne 
        #afficher : 
            # 1- continuer
            # 2- quitter le jeu 

            #si le joueur choisis option 1 
                # lancer le prochain combat
            #sinon 
                #fermer le jeu 
    
    #si le joueur perd 
        # afficher ("vous avez perdu !!")
        # afficher :
            # 1- recommencer une partie
            # 2- quitter le jeu 

    #   boucle infini
    #       input()
    #       verifier si le choix est valide
    #       si choix valide
    #           retourner int(choix)
    #       sinon
    #           afficher ("veuillez rentrer un numéro valide !!")


#si choix 2 
    #fermer le jeu 