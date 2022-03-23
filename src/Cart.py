from Order import Order
import hashlib
from util.TextTable import TextTable
from util import IOWrapper


class Cart:
    def __init__(self):
        self.orderList = []
        self.hash = ''

    def CreateOrderInCart(self, prevOrderNum, staffNum, customerNum, items, discounts):
        orderNum = prevOrderNum
        for i in range(0, len(items), 10):
            itemsInOrder = items[i:i+10]
            order = Order(orderNum, staffNum, customerNum,
                          itemsInOrder, discounts)
            orderNum = order.GetOrderNum()
            self._AddOrder(order)
        return orderNum

    def _AddOrder(self, order):
        if(len(self.orderList) >= 10):
            print("List has already full.")
            return
        self.orderList.append(order)

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
            table = self.orderList[i].GetOutputTable()\
                                     .AddHeading(f'Order {i} details -- {self.orderList[i].code()}')
            fullOutput += str(table)
        return fullOutput

    def GetJSONObj(self):
        if not self.hash:
            self.GenerateTotalHash()
        orders = []
        for order in self.orderList:
            orders.append(order.GetJSONObj())
        return orders
