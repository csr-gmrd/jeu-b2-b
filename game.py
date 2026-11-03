from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client["jeub2-b"]
collection = db["jeu"]

#afficher le choix du joueur 
    # 1- démarrer une partie
    # 2- quitter le jeu 

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
        #tant que équipe < 3
            #afficher au joueur la liste de personnage disponible     
            #choix du joueur
                #si joueur prend un personnage
                    #enlever le personnage de la liste
                    #mettre le personnage pris dans equipe
                #redonner la liste de personnage 



def commencer(equipe):
    monsters = select_monsters(3)
    alive_team = get_alive_entities(equipe)
    for hero in alive_team:
        attack_random_enemy(monsters)

    alive_monster = get_alive_entities(monsters)
    for monster in alive_monster:
        attack_random_enemy(equipe)
    #commencer un combat (equipe)
        #récupérer trois monstre 
            #random entre 3 monstre 

        #tour du joueur 
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

        #boucle jusqu'a ce que une des équipes n'est plus de personnage

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
