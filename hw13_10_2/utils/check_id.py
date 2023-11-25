# тест прямого запиту до бази даних
from pymongo import MongoClient
from bson import ObjectId  # Додайте імпорт ObjectId


client = MongoClient('mongodb://localhost')
db = client.Ten10
collection = db.quotes  



def find_document_id_by_author_id(author_id):

    document = collection.find_one({"author": ObjectId(author_id)})

    if document:
        document_id = str(document["_id"])
        print(f"Document ID for author_id {author_id}: {document_id}")
        return document_id
    else:
        print(f"No document found for author_id {author_id}")
        return None

if __name__ == "__main__":
    author_id = "654ce4bbbdba200b100aad47"  
    find_document_id_by_author_id(author_id)



# def find_quote_by_author_id(author_id):

#     document = collection.find_one({"author": ObjectId(author_id)})

#     if document:
#         quote = document.get("quote")
#         if quote:
#             print(f"Quote for author_id {author_id}: {quote}")
#             return quote
#         else:
#             print(f"No quote found for author_id {author_id}")
#             return None
#     else:
#         print(f"No document found for author_id {author_id}")
#         return None

# if __name__ == "__main__":
#     author_id = "654ce4bbbdba200b100aad4a"  
#     find_quote_by_author_id(author_id)

# utils/check_id.py


def find_quote_by_author_id(author_id):
    client = MongoClient('mongodb://localhost')
    db = client.Ten10
    collection = db.quotes

    document = collection.find_one({"author": ObjectId(author_id)})

    if document:
        quote = document.get("quote")
        if quote:
            return quote
        else:
            return None
    else:
        return None
