from functools import cache
from functools import reduce

numbers = [10, 20, 30, 40]
result = reduce(lambda total, number: total + number , numbers)
print(result)

# @cache
# def calculate_cube(number):
#     print("calculating cube...")
#     return number ** 3

# print(calculate_cube(3))
# print(calculate_cube(3))
# print(calculate_cube(4))
# print(calculate_cube(4))
# print(calculate_cube(5))