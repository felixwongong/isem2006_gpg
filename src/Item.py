from re import L


from util import db


class Item:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

    def GetAttr(self):
        return [self.id, self.name, self.price]

    @classmethod
    def GetObjectByID(cls, id):
        data = db.GetDataByID(id, 'item')
        return cls(**data)
