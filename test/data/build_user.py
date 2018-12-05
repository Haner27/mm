from bson import ObjectId


class User:
    def __init__(self, name, age):
        self.id = ObjectId()
        self.name = name
        self.age = age

    def update_age(self, age):
        self.age = age