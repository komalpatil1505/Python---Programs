
def calculateCallingGST(a, b):
    amount = a + b
    gst = amount * 18 / 100
    return amount + gst


def calculateDataGST(c, d):
    amount = c + d
    gst = amount * 12 / 100
    return amount + gst


def calculateSMSGST(e):
    gst = e * 5 / 100
    return e + gst


def totalBill(a, b, c, d, e):
    calling = calculateCallingGST(a, b)
    data = calculateDataGST(c, d)
    sms = calculateSMSGST(e)

    return calling + data + sms


def calculateDiscountedBill(a, b, c, d, e):
    total = totalBill(a, b, c, d, e)
    discount = total * 10 / 100
    return total - discount


# Sample values
a = 100
b = 50
c = 200
d = 100
e = 50

total = totalBill(a, b, c, d, e)
discount = total * 10 / 100
final_amount = calculateDiscountedBill(a, b, c, d, e)

print(f"Total after GST = {total:.2f}")
print(f"Discount = {discount:.2f}")
print(f"Final payable amount = {final_amount:.2f}")
