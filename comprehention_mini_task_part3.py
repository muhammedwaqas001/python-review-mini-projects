matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

comprehension_matrix = [number for row in matrix for number in row]
print(comprehension_matrix)

# [2, 4, 6, 8]
even_number = [number for row in matrix for number in row if number % 2 == 0]
print(even_number)

square_of_numbers = [number ** 2 for row in matrix for number in row]
print(square_of_numbers)