def create_multiplier(factor):
    def multiply(number):
        result = number * factor
        return result
    return multiply

double = create_multiplier(2)
triple = create_multiplier(3)
print(double(5))
print(triple(5))
print(double(10))        
