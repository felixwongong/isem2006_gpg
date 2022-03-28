# This is for data creation during development only

from util import IOWrapper
import random

if __name__ == '__main__':
    peopleData = IOWrapper.LoadFileJSON("/db/people.json")
    itemData = IOWrapper.LoadFileJSON("/db/item.json")
    orderData = IOWrapper.LoadFileJSON("/db/order.json")
    isAppend = input("Do you want to append to existing file? (Y/n) \n")
    mode = 'a' if isAppend.lower() == 'y' else 'w'
    numItems = int(input("How many items do u want to generate?\n"))
    itemSelected = random.sample(itemData, k=numItems)
    peopleSelected = random.choice(peopleData)
    discounts = [random.randint(1, 10)/10 / 100, random.randint(0, 5)/100]
    print(peopleSelected)

    newOrder = {
        'staffID': peopleSelected['id'],
        "items": [],
        "discounts": discounts,
    }

    for item in itemSelected:
        quantity = 1 if item['price'] > 100 else random.randint(1, 7)
        newItem = {
            "id": item['id'],
            "quantity": quantity,
        }
        newOrder['items'].append(newItem)

    if mode == 'a':
        orderData.append(newOrder)
        IOWrapper.WriteFileJSON("db/order.json", orderData)
    else:
        IOWrapper.WriteFileJSON("db/order.json", [newOrder])
