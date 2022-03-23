import math
from util.misc import a2zz
from util.TextTable import TextTable
from datetime import datetime
from Customer import Customer


class Order:
    def __init__(self, prevOrderNum, staffNum, customerNum, items, discounts):
        self.orderNum = Order._GetNum(prevOrderNum)
        self.staffNum, self.customerNum = staffNum, customerNum
        self.items, self.discounts = items, discounts
        self.date = datetime.now()
        self.modMethod = input(
            f"Select mod method for order number {'-'.join(self.orderNum)} (A, B, C, D)\n").strip().upper()
        if self.modMethod not in ('A', 'B', 'C', 'D'):
            self.modMethod = 'A'

    def _FindCheckDigit(self, alpha):
        alpha2ModDictionary = {
            "A": 9,
            "B": 8,
            "C": 7,
            "D": 6
        }
        sum = 0
        for i in range(len(self.staffNum)):
            sum += (int(self.staffNum[i]) * int(self.orderNum[1][i]))

        sumOverAlpha = sum / alpha2ModDictionary[alpha]
        checkDigit = (math.ceil(sumOverAlpha) - sumOverAlpha) * \
            alpha2ModDictionary[alpha]
        return int(checkDigit)

    @staticmethod
    def _GetNum(prevNumStr):
        (lead, id) = prevNumStr.split('-')
        id = int(id.strip())
        if id < 999999:
            id += 1
        else:
            a2zzGen = a2zz()
            while lead != next(a2zzGen):
                pass
            lead = next(a2zzGen)
            id = 0

        idStr = str(id).rjust(6, '0')
        return (lead, idStr)

    def GetCustomer(self):
        print(Customer.name_address(self.customerNum))

    def GetOrderNum(self):
        return '-'.join(self.orderNum)
# region Calculate total price of order

    def _GetTotal(self):
        subtotal = self._CalcSubtotal()
        delivery = 0 if subtotal >= 600 else 50
        total = subtotal - self._CalcDiscounts(subtotal) + delivery
        mall = total * 0.002 if total >= 800 else 0
        return round(total + mall, 1)

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
        lead, idStr = self.orderNum
        return f'{lead}{self.staffNum}{self.modMethod}{idStr}{len(self.items)}({checkDigit})'

    def GetOutputTable(self):
        table = TextTable(2, 25)
        table.AddRow(["Order_Number", '-'.join(self.orderNum)])\
             .AddRow(["Agency_number", self.staffNum])\
             .AddRow(["Modulus_number", self._FindCheckDigit(self.modMethod)])\
             .AddRow(["Total", self._GetTotal()])\
             .AddRow(["Hash_Total", self.GetHashTotal()])

        return table

    def GetJSONObj(self):
        JSONObj = {
            "id": '-'.join(self.orderNum),
            "staffID": self.staffNum,
            "items": self.items,
            "discounts": self.discounts,
        }
        return JSONObj
