import pymongo

from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://phille2512:Maultier95@test01.9zwwyhf.mongodb.net/?retryWrites=true&w=majority")
db = cluster["Test01"]
collection = db["user"]

collection.insert_one({"_id": 0, "name": "Gerhard"})