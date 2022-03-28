import os
import sys
from util import IOWrapper, db


class Customer:
    def __init__(self, id, name, address):
        self.id = id
        self.name = name
        self.address = address

    @staticmethod
    def name_address(customer_number):
        # will replace by db query if db is used
        peopleData = IOWrapper.LoadFileJSON('/testdata/people.json')
        for people in peopleData:
            if people['id'] == customer_number:
                return (people['name'], people['address'])

    @classmethod
    def GetObjectByID(cls, id):
        data = db.GetDataByID(id, 'customer')
        if not data:
            print(f"No such customer with id {id}. Program restart")
            os.execl(sys.executable, sys.executable, *sys.argv)
        return cls(**data)
