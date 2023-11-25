import random
from pymongo import MongoClient

# додаємо теги в базу даних

client = MongoClient('mongodb://localhost')
db = client.Ten10
collection = db.quotes

def add_random_tags_to_quotes(quotes):
    # Рандомні теги
    tags = ["inspiration", 
            "motivation", 
            "wisdom", 
            "life", 
            "success", 
            "love", 
            "books"]

    # Додавання рандомних тегів до кожної цитати
    for quote in quotes:
        quote["tags"] = random.sample(tags, random.randint(1, 3))  # Виберіть випадкову кількість тегів для кожної цитати

    return quotes


def update_quotes_with_tags_in_database(quotes):

    # Оновлення кожної цитати з новими тегами у базі даних
    for quote in quotes:
        query = {"_id": quote["_id"]}  # Замініть це на вашу унікальну ідентифікацію
        update = {"$set": {"tags": quote["tags"]}}
        collection.update_one(query, update)

    print(f"Оновлено {len(quotes)} цитат з новими тегами у базі даних.")

# Отримання цитат з бази даних
existing_quotes = list(collection.find({}))

# Додавання рандомних тегів до існуючих цитат
quotes_with_tags = add_random_tags_to_quotes(existing_quotes)

# Оновлення цитат з новими тегами в базі даних
update_quotes_with_tags_in_database(quotes_with_tags)
