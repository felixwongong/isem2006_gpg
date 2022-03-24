import math
from util.TextTable import TextTable
from util.consoleInputter import OptionInput as optInput
from datetime import datetime
from Customer import Customer


class Order:
    def __init__(self, orderNum, staffNum, customerNum, items, discounts):
        self.orderNum = orderNum
        self.staffNum, self.customerNum = staffNum, customerNum
        self.items, self.discounts = items, discounts
        self.date = datetime.now()
        self.modMethod = optInput(
            f"Select mod method for order number {self.orderNum}", ['A', 'B', 'C', 'D'], True)

    def _FindCheckDigit(self, alpha):
        alpha2ModDictionary = {
            "A": 9,
            "B": 8,
            "C": 7,
            "D": 6
        }
        sum = 0
        lead, id = self.orderNum.split('-')
        for i in range(len(self.staffNum)):
            sum += (int(self.staffNum[i]) * int(id[i]))

        sumOverAlpha = sum / alpha2ModDictionary[alpha]
        checkDigit = (math.ceil(sumOverAlpha) - sumOverAlpha) * \
            alpha2ModDictionary[alpha]
        return int(checkDigit)

    def GetCustomer(self):
        print(Customer.name_address(self.customerNum))

# region Calculate total price of order

    def _GetTotal(self):
        subtotal = self._CalcSubtotal()
        delivery = 0 if subtotal >= 600 else 50
        total = subtotal - self._CalcDiscounts(subtotal) + delivery
        self.mall = total * 0.002 if total >= 800 else 0
        return round(total, 1)

    def _CalcSubtotal(self):
        subtotal = 0
        for item in self.items:
            subtotal += (item['price'] * item['quantity'])
        return subtotal

    def _CalcDiscounts(self, subtotal):
        discountAmount = 0
        for discount in self.discounts:
            discountAmount += subtotal * discount
        return discountAmount

    def GetHashTotal(self):
        hashTotal = 0
        for item in self.items:
            hashTotal += int(item['id'])
        return str(hashTotal)
# endregion

    def code(self):
        checkDigit = self._FindCheckDigit(self.modMethod)
        lead, idStr = self.orderNum.split('-')
        return f'{lead}{self.staffNum}{self.modMethod}{idStr}{len(self.items)}({checkDigit})'

    def GetAuditTable(self):
        table = TextTable(2, 25)
        table.AddRow(["Order_Number", self.orderNum])\
             .AddRow(["Agency_number", self.staffNum])\
             .AddRow(["Modulus_number", self._FindCheckDigit(self.modMethod)])\
             .AddRow(["Total", self._GetTotal()])\
             .AddRow(["Hash_Total", self.GetHashTotal()])

        return table

    def GetJSONObj(self):
        JSONObj = {
            "id": self.orderNum,
            "staffID": self.staffNum,
            "items": self.items,
            "discounts": self.discounts,
        }
        return JSONObj
