import pymongo
from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.v5ddl1q.mongodb.net/"
client = MongoClient(url)
db = client.pytech
print("-- Pytech COllection List --")
print(db.list_collection_names())


