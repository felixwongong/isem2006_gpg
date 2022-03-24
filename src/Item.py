from re import L


class Item:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

    def GetAttr(self):
        return [self.id, self.name, self.price]
