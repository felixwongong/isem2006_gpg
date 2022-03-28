from util import db
import sys
import os


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
        if not data:
            print(f"No such item with id {id}. Program restart")
            os.execl(sys.executable, sys.executable, *sys.argv)
        return cls(**data)
