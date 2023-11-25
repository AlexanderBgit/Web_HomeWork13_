# templatetags/extract.py
import logging
from django import template
from bson import ObjectId
from ..utils import get_mongodb

logger = logging.getLogger(__name__)

register = template.Library()

@register.filter(name='author')
def get_author(id_):
    logger.debug("Retrieving author with ID: %s", id_)
    db = get_mongodb()
    author_data = db.authors.find_one({'_id': ObjectId(id_)})

    if author_data:
        author = {
            'fullname': author_data['fullname'],
            'description': author_data.get('description', ''),
        }
        logger.info("Successfully retrieved author: %s", author['fullname'])
        return author
    else:
        logger.warning("Author with ID %s not found", id_)
        return None



def get_author_and_quotes(author_id):
    logger.debug("Retrieving author with ID: %s", author_id)
    db = get_mongodb()
    author_data = db.authors.find_one({'_id': ObjectId(author_id)})

    if author_data:
        author = {
            'fullname': author_data['fullname'],
            'description': author_data.get('description', ''),
        }
        logger.info("Successfully retrieved author: %s", author['fullname'])

        # Отримати цитати для автора
        quotes = find_quote_by_author_id(author_id)
        logger.debug("Quotes for author %s: %s", author_id, quotes)

        return author, quotes
    else:
        logger.warning("Author with ID %s not found", author_id)
        return None, None


def find_quote_by_author_id(author_id):
    db = get_mongodb()
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
