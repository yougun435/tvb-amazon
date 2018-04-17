from pymongo import MongoClient
import re
from bson.objectid import ObjectId


class Product:
    def __init__(self):
        client = MongoClient('localhost', 27017)
        self.db = client.tvb_amazon

    def save(self, product):
        self.db.products.insert_one(product)

    def search_by_name(self, name):
        query = {
            'name': re.compile(name, re.IGNORECASE)
        }
        result = self.db.products.find(query)
        matches = []
        for product in result:
            matches.append(product)
        return matches

    def delete_by_id(self, _id):
        self.db.products.delete_one({'_id': ObjectId(_id)})

    def update_by_id(self, _id, updated_product):
        condition = dict()
        condition['_id'] = ObjectId(_id)

        self.db.products.update_one(filter=condition, update={'$set': updated_product})