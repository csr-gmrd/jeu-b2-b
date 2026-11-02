from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client["jeub2-b"]
collection = db["jeu"]

#afficher le choix du joueur 
    # 1- démarrer une partie
    # 2- quitter le jeu 

#récuperer le choix du joueur 
    #si choix 1

        #récupérer la liste des personnages

        #afficher au joueur la liste de personnage disponible 
        
        #choix du joueur
            #si joueur prend un personnage
                #enlever le personnage de la liste 
        #boucle pour 3 personnages

    #si choix 2 
        #fermer le jeu 
    
    #quand le joueur a finis de faire son équipe 
        #commencer un combat 
            #récupérer trois monstre facile 
                #random entre 3 monstre 
            # récupérer l'équipe du joueur 

            #tour du joueur 
                #
