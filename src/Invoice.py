from util.consoleInputter import ConsoleMsg
from util.TextTable import TextTable


class Invoice:
    @staticmethod
    def GetInvoice(order):
        invoice = ''
        invoice += ConsoleMsg("Invoice")
        invoice += str(TextTable(3, 25)
                       .AddRow(['Invoice Date', "Order No.", "Mall Dollar"])
                       .AddRow([order.date, order.code(), f"${order.mall()}"]))
        itemsTable = TextTable(4, 19)
        itemsTable.AddHeading(f"Customer Number: {order.customer.id}")
        for item in order.items:
            id, name, price = item["item"].GetAttr()
            itemsTable.AddRow(
                [id, name, item["quantity"], price * item["quantity"]])
        invoice += str(itemsTable)
        subtotal = order.CalcSubtotal()
        invoice += str(TextTable(2, 25)
                       .AddHeading("Shipping to")
                       .AddRow([f"Customer Number:", order.customer.name])
                       .AddRow([f"Customer Address:", order.customer.address])
                       .AddRow([f"", ""])
                       .AddRow([f"SubTotal:", subtotal])
                       .AddRow([f"Discount1:", order.discounts[0] * subtotal])
                       .AddRow([f"Discount2:", order.discounts[1] * subtotal])
                       .AddRow([f"Delivery Fee:", order.delivery()])
                       .AddRow(["Total", order.GetTotal()]))

        return invoice
