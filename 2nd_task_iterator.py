numbers = [10, 20, 30]

iterator = iter(numbers)
print(next(iterator))
print(next(iterator))
print(next(iterator))

try:
    print(next(iterator))
except StopIteration:
    print("Iteration Fininshed.")
