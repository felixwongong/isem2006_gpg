import math


def FindCheckDigit(staffNum, orderNum, alpha):
    alpha2ModDictionary = {
        "A": 9,
        "B": 8,
        "C": 7,
        "D": 6
    }
    sum = 0
    for i in range(len(staffNum)):
        sum += (int(staffNum[i]) * int(orderNum[i]))

    sumOverAlpha = sum / alpha2ModDictionary[alpha]
    checkDigit = (math.ceil(sumOverAlpha) - sumOverAlpha) * \
        alpha2ModDictionary[alpha]
    return int(checkDigit)


def FindTotalCost(orders, discounts):
    totalOrders = 0
    if len(orders) > 9:
        raise Exception(f"There are more than 9 items ({len(orders)})!")
    totalDiscounts = addSum(discounts)
    totalOrders = addSum(orders)

    if totalOrders < 600:
        return totalOrders - totalDiscounts + 50
    return totalOrders - totalDiscounts

print("Hello world")
print("hii")
print("hello")
print ("Ivan typing")

"""
Util
"""
def addSum(values):
    sum = 0
    for val in values:
        sum += val
    return sum
""""""

## print(FindCheckDigit('123456', '567878', "B"))

orders = [108, 198, 158.7, 280]
discounts = [2, 37.14]
print(FindTotalCost(orders, discounts))
