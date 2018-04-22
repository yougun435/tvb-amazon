from pymongo import MongoClient


class UserModel:
    def __init__(self):
        client = MongoClient('localhost', 27017)
        self.db = client.tvb_amazon

    def add_new_user(self, name, email, username, password):
        user = {
            'name': name,
            'email': email,
            'username': username,
            'password': password
        }
        self.db.users.insert_one(user)

    def authenticate(self, username, password):
        query = {
            'username': username,
            'password': password
        }
        cursor = self.db.users.find(query)
        if cursor.count() == 0:
            return False
        else:
            return True
