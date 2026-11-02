from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client["jeub2-b"]
collection = db["jeu"]

#