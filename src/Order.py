import math
from util.misc import a2zz


class Order:
    def __init__(self, prevOrderNum, staffNum, customerNum, items, discounts):
        self.orderNum = Order._GetNum(prevOrderNum)
        self.staffNum, self.customerNum = staffNum, customerNum
        self.items, self.discounts = items, discounts
        self.modMethod = input("Select mod method (A, B, C, D)\n").strip()
        if self.modMethod not in ('A', 'B', 'C', 'D'):
            self.modMethod = 'A'

    def _FindCheckDigit(self, alpha):
        alpha2ModDictionary = {
            "A": 9,
            "B": 8,
            "C": 7,
            "D": 6
        }
        print(f'Modulus method ({alpha}) is used.')
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

# region Calculate total price of order
    def _GetTotal(self):
        subtotal = self._CalcSubtotal()
        delivery = 0 if subtotal >= 600 else 50
        return subtotal - self._CalcDiscounts(subtotal) + delivery

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

    def _GetHashTotal(self):
        hashTotal = 0
        for item in self.items:
            hashTotal += int(item['id'])
        return hashTotal
# endregion

    def code(self):
        checkDigit = self._FindCheckDigit(self.modMethod)
        lead, idStr = self.orderNum
        return f'{lead}{self.staffNum}{self.modMethod}{idStr}{len(self.items)}({checkDigit})'
