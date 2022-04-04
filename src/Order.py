import math
from util.TextTable import TextTable
from util.consoleInputter import OptionInput as optInput
from datetime import datetime
from Customer import Customer


class Order:
    def __init__(self, orderNum, staffNum, customer, items, discounts):
        self.orderNum = orderNum
        self.staffNum, self.customer = staffNum, customer
        self.items, self.discounts = items, discounts
        self.date = datetime.now().strftime("%Y-%m-%d")
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


# region Calculate total price of order

    def GetTotal(self):
        subtotal = self.CalcSubtotal()
        delivery = 0 if subtotal >= 600 else 50
        total = subtotal - self.CalcDiscounts(subtotal) + delivery
        return round(total, 1)

    def CalcSubtotal(self):
        subtotal = 0
        for item in self.items:
            subtotal += (item['item'].price * item['quantity'])
        return subtotal

    def CalcDiscounts(self, subtotal):
        if self.discounts[0] > subtotal * 0.01:
            print(
                "Discount 1 is more than 1 percent of subtotal, will set to 0 by default")
            self.discounts[0] = 0
        discountAmount = 0
        discountAmount += self.discounts[0] + subtotal * self.discounts[1]
        return discountAmount

    def GetHashTotal(self):
        hashTotal = 0
        for item in self.items:
            hashTotal += int(item['item'].id)
        return str(hashTotal)

    def mall(self):
        total = self.GetTotal()
        return round(total * 0.002 if total >= 800 else 0, 1)

    def delivery(self):
        return 0 if self.CalcSubtotal() >= 600 else 50

# endregion

    def code(self):
        """Generate order code

        Returns:
            string: order code 
        """
        checkDigit = self._FindCheckDigit(self.modMethod)
        lead, idStr = self.orderNum.split('-')
        return f'{lead}{self.staffNum}{self.modMethod}{idStr}{len(self.items)}({checkDigit})'

    def GetAuditTable(self):
        """Generate and return a no heading TextTable which store order audit content (get by Cart)

        Returns:
            TextTable: order audit content
        """
        table = TextTable(2, 25)
        table.AddRow(["Order_Number", self.orderNum])\
             .AddRow(["Agency_number", self.staffNum])\
             .AddRow(["Modulus_number", self._FindCheckDigit(self.modMethod)])\
             .AddRow(["Total", self.GetTotal()])\
             .AddRow(["Hash_Total", self.GetHashTotal()])
        return table
