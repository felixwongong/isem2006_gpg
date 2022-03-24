from util import IOWrapper


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
