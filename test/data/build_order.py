from bson import ObjectId


class Order:
    def __init__(self, cost):
        self.id = ObjectId()
        self.users = []
        self.cost = cost

    def add_user(self, user):
        for u in self.users:
            if u.id == user.id:
                return
        self.users.append(user)

    def update_cost(self, cost):
        self.cost = cost

    def rm_user(self, user):
        users = []
        for u in self.users:
            if u.id != user.id:
                users.append(u)
        self.users = users
