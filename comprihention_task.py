numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
square_numbers = [number ** 2 for number in numbers]
even_numbers = [number for number in numbers if number % 2 == 0]
odd_numbers = [number for number in numbers if number % 2 != 0]
even_and_odd_numbers = ["Even" if number % 2 == 0 else "Odd" for number in numbers]
print(f"Square of numbers: {square_numbers}")
print(f"Even numbers: {even_numbers}")
print(f"Odd numbers: {odd_numbers}")
print(f"Even and Odd numbers: {even_and_odd_numbers}")