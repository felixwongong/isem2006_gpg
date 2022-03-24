from operator import itemgetter
from sys import argv
from util import IOWrapper, misc, db
from util.consoleInputter import\
    ErrorlessInput as elInput,\
    ClampInput as cInput,\
    OptionInput as optInput,\
    ConsoleMsg
from Cart import Cart
from Item import Item
from Customer import Customer
from Invoice import Invoice


def GetLastOrderID():
    lastOutput = IOWrapper.ReadFile('/output/output.txt')
    if not lastOutput:
        print("No previous output is found, defaulting to A-000000\n")
        return 'A-000000'
    return lastOutput


def DevFetchData():
    print('\n' + ConsoleMsg("In development stage") + '\n')

    orderData = db.GetAllData('order')
    customerData = db.GetAllData('customer')

    numOrders = cInput('How many orders you want to test?\t', [
                       1, len(orderData)], int)
    ordersEl = []

    for i in range(numOrders):
        staffID, customerID, orderItems, discounts = itemgetter(
            'staffID', "customerID", "items", "discounts")(orderData[i])

        items = mapItems(orderItems)
        customer = db.GetObjectByID(customerID, 'customer', Customer)
        ordersEl.append([staffID, customer, items, discounts])
    return ordersEl


def mapItems(orderItems):
    items = []
    for orderItem in orderItems:
        item = db.GetObjectByID(orderItem['id'], 'item', Item)
        items.append({"item": item, "quantity": orderItem['quantity']})
    return items


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
            id = elInput("Item ID:".ljust(25))
            quantity = elInput("Quantity:".ljust(25), int)
            items.append(
                {"item": db.GetObjectByID(id, 'item', Item), "quantity": quantity})
        print("-" * 65)
        discount1 = cInput("Discount 1:".ljust(25), [0.0, 0.01])
        discount2 = cInput("Discount 2:".ljust(25), [0.0, 0.05])

        customerID = elInput("Customer ID:".ljust(25), int)
        customer = db.GetObjectByID(customerID, 'customer', Customer)
        ordersEl.append([staffID, customer, items, [discount1, discount2]])
    return ordersEl


if __name__ == '__main__':
    ordersEl = []
    env = argv[1:]
    if len(env) > 0 and env[0].lower().strip() == 'dev':
        ordersEl = DevFetchData()
    else:
        ordersEl = ProdFetchData()

    lastOrderID = GetLastOrderID()
    cart = Cart(lastOrderID)
    for orderEl in ordersEl:
        order = cart.CreateOrder(*orderEl)
        InvoiceOption = optInput(
            "Do you want to check the invoice?", ['y', 'n'])
        if InvoiceOption == "y":
            print(Invoice.GetInvoice(order))

    IOWrapper.WriteFile('/output/output.txt', cart.orderNum)
    WriteFileOption = optInput(
        "Do you want to write to a txt audit file?", ['y', 'n'])
    if WriteFileOption == "y":
        IOWrapper.WriteFile('/output/audit.txt', cart.GetStrOutput())
    print("Byebye~")
