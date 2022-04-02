from Order import Order
import hashlib
from util.TextTable import TextTable
from util.misc import a2zz


class Cart:
    def __init__(self, lastOrderNum):
        self.orderList = []
        self.orderNum = lastOrderNum

# region Create and add order
    def CreateOrder(self, staffNum, customer, items, discounts):
        # use for loop to split orders into 10 in a piece
        for i in range(0, len(items), 10):
            itemsInOrder = items[i:i+10]
            # set orderNum state to the newest orderNum in Cart
            self.orderNum = Cart._CalcOrderNum(self.orderNum)
            order = Order(self.orderNum, staffNum, customer,
                          itemsInOrder, discounts)
            self._AddOrder(order)
        return self.orderList

    def _AddOrder(self, order):
        """Add order in Cart's orderList, if orderList full, it will be dump automatically

        Args:
            order (Order): Order generated from CreateOrder
        """
        if(len(self.orderList) >= 10):
            print("List has already full.")
            return
        self.orderList.append(order)

    @staticmethod
    def _CalcOrderNum(prevNumStr):
        """Generate new order number based on previous order number string

        Args:
            prevNumStr (string): previous order number string. e.g. "A-123456"

        Returns:
            string: new order number string
        """
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
        """
        for every order, sum up their ascii sum of each character in order number
        ASCII sum of every order will XOR each other accordingly
        Do SHA256 on XOR sum to get hash
        Get first 5 digit of hex value of the hash
        It should ensure integrity of overall cart and orders
        Verifiable if perform this hash function again.
        """
        orderHash = 0
        for order in self.orderList:
            asciiSum = 0
            code = order.code()
            for c in code:
                asciiSum += ord(c)
            orderHash ^= asciiSum
        encoded = str(orderHash).encode()
        fullHash = hashlib.sha256(encoded).hexdigest()
        return fullHash[0:5]

    def GetStrOutput(self):
        """Use for generating string output on the audit file

        Add Heading which contain number of orders and total cart hash

        Get audit content from each order, append them together and add them below the heading

        Returns:
            string: audit file content of this cart
        """
        hash = self.GenerateTotalHash()
        table = TextTable(2, 25)
        table.AddRow(['Number_of_orders', len(self.orderList)])\
             .AddRow(['Hash_total_of_orders', hash])

        fullOutput = str(table)

        for i in range(len(self.orderList)):
            table = self.orderList[i].GetAuditTable()\
                                     .AddHeading(f'Order {i} details -- {self.orderList[i].code()}')
            fullOutput += str(table)
        return fullOutput
