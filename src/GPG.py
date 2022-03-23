from operator import itemgetter
from sys import argv
from util import IOWrapper, misc
from util.consoleInputter import\
    ErrorlessInput as elInput,\
    ClampInput as cInput,\
    OptionInput as optInput,\
    ConsoleMsg
from Cart import Cart


def GetLastOrderID():
    lastOutput = IOWrapper.LoadFileJSON('/output/output.json')
    if not lastOutput:
        print("No previous output is found, defaulting to A-000000\n")
        return 'A-000000'
    return lastOutput[len(lastOutput)-1]["id"]


def DevFetchData():
    print('\n' + ConsoleMsg("In development stage") + '\n')

    orderData = IOWrapper.LoadFileJSON('/testdata/order.json')
    peopleData = IOWrapper.LoadFileJSON('/testdata/people.json')

    numOrders = cInput('How many orders you want to test?\t', [
                       1, len(orderData)], int)
    ordersEl = []

    for i in range(numOrders):
        staffID, items, discounts = itemgetter(
            'staffID', "items", "discounts")(orderData[i])
        customerID = itemgetter('id')(peopleData[0])
        ordersEl.append([staffID, customerID, items, discounts])
    return ordersEl


def ProdFetchData():
    print('\n' + ConsoleMsg("Welcome to Tone Tone mall") + '\n')
    numOrders = cInput("Number of orders:".ljust(25), [0, 10], int)

    ordersEl = []
    for i in range(numOrders):
        print(misc.Heading(f"Order {i + 1}"))
        staffID = elInput("staff ID:".ljust(25))
        numItems = elInput("Number of items:".ljust(25), int)
        items = []
        for j in range(numItems):
            print("-" * 65)
            item = {}
            item["id"] = elInput("Item ID:".ljust(25))
            item["price"] = elInput("Price:".ljust(25))
            item["quantity"] = elInput("Quantity:".ljust(25))
            items.append(item)
        print("-" * 65)
        discount1 = cInput("Discount 1:".ljust(25), [0.0, 0.01])
        discount2 = cInput("Discount 2:".ljust(25), [0.0, 0.05])
        customerID = elInput("Customer ID:".ljust(25), int)
        ordersEl.append([staffID, customerID, items, [discount1, discount2]])
    return ordersEl


if __name__ == '__main__':
    ordersEl = []
    env = argv[1:]
    if len(env) > 0 and env[0].lower().strip() == 'dev':
        ordersEl = DevFetchData()
    else:
        ordersEl = ProdFetchData()

    lastOrderID = GetLastOrderID()
    cart = Cart()
    for orderEl in ordersEl:
        lastOrderID = cart.CreateOrderInCart(lastOrderID, *orderEl)

    previewOption = optInput(
        "Do you want to preview the audit content? (y/n) \n", ['y', 'n'])
    if previewOption == "y":
        print(ConsoleMsg("Preview"))
        print(cart.GetStrOutput())

    IOWrapper.WriteFileJSON('/output/audit.json', cart.GetJSONObj())
    WriteFileOption = optInput(
        "Do you want to write to a txt audit file? (y/n) \n", ['y', 'n'])
    if WriteFileOption == "y":
        IOWrapper.WriteFile('/output/audit.txt', cart.GetStrOutput())
