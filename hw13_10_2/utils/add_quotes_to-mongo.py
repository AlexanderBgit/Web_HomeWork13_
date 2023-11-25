import json
from bson import ObjectId

from pymongo import MongoClient
import os


client = MongoClient('mongodb://localhost')

db = client.Ten10

# повний шлях до файлу quotes.json
file_path = os.path.join(os.path.dirname(__file__), 'quotes.json')  

with open(file_path, 'r', encoding='utf-8') as fd: #file description
    quotes = json.load(fd)


for quote in quotes:
    author = db.authors.find_one({'fullname': quote['author']})
    if author:
        db.quotes.insert_one({
           'quote': quote['quote'], 
        #    'tag': quote['tag'] 
            'author': ObjectId(author['_id'])

        })
    
