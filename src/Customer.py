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
        # Unused method
        peopleData = IOWrapper.LoadFileJSON('/db/people.json')
        for people in peopleData:
            if people['id'] == customer_number:
                return (people['name'], people['address'])

    @classmethod
    def GetObjectByID(cls, id):
        """Simulate database in NoSQL environment
        if no data found in db, program will restart.

        Args:
            id (string): id of Customer object store in db file

        Returns:
            Customer: an instance of Customer object created from data fetched from database
        """
        data = db.GetDataByID(id, 'customer')
        if not data:
            print(f"No such customer with id {id}. Program restart")
            os.execl(sys.executable, sys.executable, *sys.argv)
        return cls(**data)
