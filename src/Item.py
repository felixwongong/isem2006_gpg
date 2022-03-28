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
        """Simulate database in NoSQL environment
        if no data found in db, program will restart.

        Args:
            id (string): id of Item object store in db file

        Returns:
            Item: an instance of Item object created from data fetched from database
        """

        data = db.GetDataByID(id, 'item')
        if not data:
            print(f"No such item with id {id}. Program restart")
            os.execl(sys.executable, sys.executable, *sys.argv)
        return cls(**data)
