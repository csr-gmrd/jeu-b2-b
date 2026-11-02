#insérer les personnages et monstres dans MongoDB.

# Creation de la base de données et des collections
# Creer une liste de monstres 
liste_monstres = [
    {"name": "GOBELIN", "health": 45, "attack": 12, "defense": 4}, #facile
    {"name": "ZOMBIE", "health": 60, "attack": 13, "defense": 5}, #facile
    {"name": "SKELETON", "health": 55, "attack": 15, "defense": 6}, #facile
    {"name": "ORC", "health": 75, "attack": 16, "defense": 7}, #moyen
    {"name": "LOUPGAROU", "health": 85, "attack" : 18, "defense": 7}, #moyen
    {"name": "SPECTRE", "health": 60, "attack": 17, "defense": 9}, #moyen
    {"name": "VAMPIRE", "health": 90, "attack": 19, "defense": 9}, #difficile
    {"name": "TROLL", "health": 130, "attack": 18, "defense": 8}, #difficile
    {"name": "GOLEM", "health": 150, "attack": 16, "defense": 12},#difficile
    {"name": "DRAGON", "health": 160, "attack": 22, "defense": 11} #boss
]
# Creer une liste de personnages
liste_characters = [
    {"name": "KNIGHT", "health": 120, "attack": 17, "defense": 15}, 
    {"name": "SQUIRE", "health": 60, "attack": 8, "defense": 7}, 
    {"name": "ARCHER", "health": 90, "attack": 18, "defense": 7}, 
    {"name": "MAGE", "health": 80, "attack": 20, "defense": 5},
    {"name": "ROGUE", "health": 85, "attack": 22, "defense": 8},
    {"name": "DUELIST", "heatlh": 100, "attack": 15, "defense": 10},
    {"name": "BBERSERKER", "health": 105, "attack": 23, "defense": 6},
    {"name": "MONK", "health": 95, "attack": 19, "defense": 9}
]

# Inserer les monstres dans la collection "monstres"
# Se connecter à la base de données MongoDB
from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017/")
db = client["jeub2-b"]
# Obtenir la collection "monstres" de la base de données
db.monstres.drop()
db.monstres.insert_many(liste_monstres)

# insertMany
# Inserer les personnages dans la collection "personnages"
db.characters.drop()
db.characters.insert_many(liste_characters)
