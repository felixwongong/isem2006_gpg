from operator import itemgetter
from sys import argv
from Order import Order
from util import jsonWrapper


def GetLastOrderID():
    lastOutput = jsonWrapper.LoadFile('/output/output.json')
    if not lastOutput:
        return 'A-000000'
    return lastOutput[len(lastOutput)-1]["id"]


if __name__ == '__main__':
    print(f"{'=' * 65}\nProgram started at development environment. \n{'=' * 65}\n")

    orderData = jsonWrapper.LoadFile('/testdata/order.json')
    peopleData = jsonWrapper.LoadFile('/testdata/people.json')

    staffID, items, discounts = itemgetter(
        'staffID', "items", "discounts")(orderData[0])
    customerID = itemgetter('id')(peopleData[0])

    lastOrderID = GetLastOrderID()

    order = Order(lastOrderID, staffID, customerID, items,  discounts)
    print(order.code())
