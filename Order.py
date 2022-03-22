import math
from util import a2zz


class Order:
    def __init__(self, prevOrderNum, staffNum, items):
        self.orderNum = Order.GetNum(prevOrderNum)
        self.staffNum = staffNum
        self.items = items

    def FindCheckDigit(self, alpha):
        alpha2ModDictionary = {
            "A": 9,
            "B": 8,
            "C": 7,
            "D": 6
        }
        sum = 0
        for i in range(len(self.staffNum)):
            sum += (int(self.staffNum[i]) * int(self.orderNum[i]))

        sumOverAlpha = sum / alpha2ModDictionary[alpha]
        checkDigit = (math.ceil(sumOverAlpha) - sumOverAlpha) * \
            alpha2ModDictionary[alpha]
        return int(checkDigit)

    @staticmethod
    def GetNum(prevNumStr):
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
        return f'{lead}-{idStr}'
