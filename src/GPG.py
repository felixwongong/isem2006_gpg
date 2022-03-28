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

'''Program method are documented, if need help in any function, use help(<function name>)
e.g. help(ConsoleMsg)
'''


def GetLastOrderID():
    """Get the last order ID from file using *IOWrapper*, dir: <__dirname__>/output/output.txt

    Returns:
        string: string of last order ID, if not ID found, default return "A-000000" 
    """
    lastOutput = IOWrapper.ReadFile('/output/output.txt')
    if not lastOutput:
        print("No previous output is found, defaulting to A-000000\n")
        return 'A-000000'
    return lastOutput


def DevFetchData():
    """Use to fetch development from db

    Returns:
        list<list>: a list of order attributes
    """
    print('\n' + ConsoleMsg("In development stage") + '\n')

    orderData = db.GetAllData('order')

    numOrders = cInput('How many orders you want to test?\t', [
                       1, len(orderData)], int)
    ordersEl = []

    for i in range(numOrders):
        staffID, customerID, orderItems, discounts = itemgetter(
            'staffID', "customerID", "items", "discounts")(orderData[i])

        items = mapItems(orderItems)
        customer = Customer.GetObjectByID(customerID)
        ordersEl.append([staffID, customer, items, discounts])
    return ordersEl


def mapItems(orderItems):
    """Get all item from id inputs (only for development purpose)

    Args:
        orderItems (list<int>): list of item ids from orders. 

    Returns:
        list<Item>: all the items from db which have ids same as input
    """
    items = []
    for orderItem in orderItems:
        item = Item.GetObjectByID(orderItem["id"])
        items.append({"item": item, "quantity": orderItem['quantity']})
    return items


def ProdFetchData():
    """Draw and get input from users in cli

    Returns:
        list<list>: a list of order attributes
    """
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
                {"item": Item.GetObjectByID(id), "quantity": quantity})
        print("-" * 65)
        discount1 = cInput("Discount 1:".ljust(25), [0.0, 0.01])
        discount2 = cInput("Discount 2:".ljust(25), [0.0, 0.05])

        customerID = elInput("Customer ID:".ljust(25), int)
        customer = Customer.GetObjectByID(customerID)

        ordersEl.append([staffID, customer, items, [discount1, discount2]])
    return ordersEl


if __name__ == '__main__':
    ordersEl = []
    env = argv[1:]
    """
    Dev mode:   py/python3 src/GPG.py dev
    Prod mode:  py/python3 src/GPG.py
    
    DevFetchData and ProdFetchData both return a list of order attributes
    DevFetchData will pre-input some data, ProdFetchData require user input data
    Input with id that not exist in database is not allowed (and will not be catched)
    """
    if len(env) > 0 and env[0].lower().strip() == 'dev':
        ordersEl = DevFetchData()
    else:
        ordersEl = ProdFetchData()

    lastOrderID = GetLastOrderID()

    # Initialize a shopping cart with last orderID
    cart = Cart(lastOrderID)
    for orderEl in ordersEl:
        # Add orders' detail into cart, and let cart to create the order
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
