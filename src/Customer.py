from util import IOWrapper


class Customer:
    @staticmethod
    def name_address(customer_number):
        # will replace by db query if db is used
        peopleData = IOWrapper.LoadFileJSON('/testdata/people.json')
        for people in peopleData:
            if people['id'] == customer_number:
                return (people['name'], people['address'])
