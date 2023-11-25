from pymongo import MongoClient
import os


client = MongoClient('mongodb://localhost')

db = client.Ten10

collection = db.quotes  

all_quotes = collection.find()

for quote in all_quotes:
    print(quote)
