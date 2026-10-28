class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def __str__(self):
        return f"Product = {self.name}, Price = {self.price}" 
    def __repr__(self):
        return f"Product(name = {self.name!r}, Price = {self.price})"
    def __eq__(self, other):
        if not isinstance(other, Product):
            return NotImplemented
        return self.name == other.name and self.price == other.price           
# product1 = Product("Laptop", 150000)
# product2 = Product("Laptop", 150000)
# print(product1)   
# print(repr(product1)) 
# print(product1 == product2)

product1 = Product("Laptop", 150000)
product2 = Product("Laptop", 150000)
product3 = Product("Mobile", 80000)

print(product1 == product2)
print(product1 == product3)
print(product1 == "Laptop")