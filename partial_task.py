from functools import partial
def calculate_tax(amount, tax_rate):
    return amount * tax_rate

taxrate = partial(calculate_tax, tax_rate=  0.20)
print(taxrate(5000))
print(taxrate(1000))
print(taxrate(2000))