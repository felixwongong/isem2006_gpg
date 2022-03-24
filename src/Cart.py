from Order import Order
import hashlib
from util.TextTable import TextTable
from util.misc import a2zz


class Cart:
    def __init__(self, lastOrderNum):
        self.orderList = []
        self.hash = ''
        print(lastOrderNum)
        self.orderNum = lastOrderNum

# region Create and add order
    def CreateOrder(self, staffNum, customerNum, items, discounts):
        for i in range(0, len(items), 10):
            itemsInOrder = items[i:i+10]
            self.orderNum = Cart._CalcOrderNum(self.orderNum)
            order = Order(self.orderNum, staffNum, customerNum,
                          itemsInOrder, discounts)
            self._AddOrder(order)

    def _AddOrder(self, order):
        if(len(self.orderList) >= 10):
            print("List has already full.")
            return
        self.orderList.append(order)

    @staticmethod
    def _CalcOrderNum(prevNumStr):
        lead, id = prevNumStr.split('-')
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
# endregion

    def GenerateTotalHash(self):
        orderHash = 0
        for order in self.orderList:
            asciiSum = 0
            code = order.code()
            for c in code:
                asciiSum += ord(c)
            orderHash ^= asciiSum
        encoded = str(orderHash).encode()
        fullHash = hashlib.sha256(encoded).hexdigest()
        self.hash = fullHash[0:5]

    def GetStrOutput(self):
        if not self.hash:
            self.GenerateTotalHash()
        table = TextTable(2, 25)
        table.AddRow(['Number_of_orders', len(self.orderList)])\
             .AddRow(['Hash_total_of_orders', self.hash])

        fullOutput = str(table)

        for i in range(len(self.orderList)):
            table = self.orderList[i].GetAuditTable()\
                                     .AddHeading(f'Order {i} details -- {self.orderList[i].code()}')
            fullOutput += str(table)
        return fullOutput

    def GetDict(self):
        return self.orderList[-1].orderNum
