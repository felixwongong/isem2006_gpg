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


# region Development Environment


def DevFetchData():
    """Use to fetch development data from db

    Returns:
        list<list>: a list of order attributes
    """
    print('\n' + ConsoleMsg("In development stage") + '\n')

    orderData = db.GetAllData('order')

    orderNum = cInput('Which orders you want to test?\t', [
        0, len(orderData) - 1], int)

    staffID, customerID, orderItems, discounts = itemgetter(
        'staffID', "customerID", "items", "discounts")(orderData[orderNum])

    items = mapItems(orderItems)
    customer = Customer.GetObjectByID(customerID)
    return [staffID, customer, items, discounts]


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
# endregion


def ProdFetchData():
    """Draw and get input from users in cli

    Returns:
        list: a list of order attributes
    """

    print('\n' + ConsoleMsg("Welcome to Tone Tone Mall"))

    print(misc.Heading(f"Order"))
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
    discount1 = elInput("Discount < 1% subtotal:".ljust(25), float)
    discount2 = cInput("Discount 2 (%):".ljust(25), [0.0, 5]) / 100

    customerID = elInput("Customer ID:".ljust(25), int)
    customer = Customer.GetObjectByID(customerID)

    return [staffID, customer, items, [discount1, discount2]]


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


if __name__ == '__main__':
    orderEl = []
    env = argv[1:]  # [1:] from 1 to the end of the list
    """
    Dev mode:   py/python3 src/GPG.py dev
    Prod mode:  py/python3 src/GPG.py

    DevFetchData and ProdFetchData both return a list of order attributes
    DevFetchData will pre-input some data, ProdFetchData require user input data
    Input with id that not exist in database is not allowed (and will not be catched)
    """
    # Initialize a shopping cart with last orderID
    lastOrderID = GetLastOrderID()
    cart = Cart(lastOrderID)

    # Get order data, from prestored(Dev), or user-inputted(Prod) data
    if len(env) > 0 and env[0].lower().strip() == 'dev':
        orderEl = DevFetchData()
    else:
        orderEl = ProdFetchData()

    # Add order detail into cart, and let cart to create the order
    cart.CreateOrder(*orderEl)

    # Let user to check the cart invoice
    invoiceOption = optInput(
        f"Do you want to check the invoice for this cart order(s)?", ['y', 'n'])
    if invoiceOption == "y":
        invoice = cart.GenerateInvoice()
        print(invoice)

    IOWrapper.WriteFile('/output/invoice.txt', invoice)

    IOWrapper.WriteFile('/output/output.txt', cart.orderNum)
    WriteFileOption = optInput(
        "Do you want to write to a txt audit file?", ['y', 'n'])
    if WriteFileOption == "y":
        IOWrapper.WriteFile('/output/audit.txt', cart.GetStrOutput())
    print("Byebye~")
