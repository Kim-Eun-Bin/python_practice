class NegativePriceException(Exception):
    # constructor
    def __init__(self):
        print('Price는 can\'t be Negative')
        raise AttributeError

def calc_price(value):
    price = value * 1000
    if price < 0:
        raise NegativePriceException
    return price

print(calc_price(200))
print(calc_price(-100))