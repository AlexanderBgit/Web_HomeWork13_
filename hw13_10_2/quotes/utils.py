from pymongo import MongoClient

def get_mongodb():
    client = MongoClient('mongodb://localhost')

    db = client.Ten10
    return db

# тепер маємо доступ для виведення






