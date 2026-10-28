square = lambda number: number **2
print(square(5))

maximum = lambda first_number, second_number: max(first_number, second_number)
print(maximum(10, 30))

check_number = lambda number: "Even" if number % 2 == 0 else "odd"
print(check_number(10))