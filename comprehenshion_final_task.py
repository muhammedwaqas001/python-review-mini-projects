numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_of_numbers_square = [number ** 2 for number in numbers]
print(list_of_numbers_square)
list_of_even_numbers = [number for number in numbers if number % 2 == 0]
print(list_of_even_numbers)
square_of_odd_numbers = [number ** 2 for number in numbers if number % 2 != 0]
print(square_of_odd_numbers)
label_for_numbers = ["Even" if number % 2 == 0 else "Odd" for number in numbers]
print(label_for_numbers)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
flatten_matrix = [number for row in matrix for number in row]
print(flatten_matrix)
matrix_of_even = [number for row in matrix for number in row if number % 2 == 0]
print(matrix_of_even)
matrix_of_squares = [number ** 2 for row in matrix for number in row]
print(matrix_of_squares)

numbers = [1, 2, 2, 3, 3, 4, 4, 5]

set_of_numbers = {number for number in numbers}
print(set_of_numbers)
square_of_numbers_in_set = {number ** 2 for number in numbers}
print(square_of_numbers_in_set)
set_of_even_numbers = {number for number in numbers if number % 2 == 0}
print(set_of_even_numbers)

numbers = [1, 2, 3, 4, 5]
dict_of_numbers_square = {number: number ** 2 for number in numbers}
print(dict_of_numbers_square)

scores = {
    "Python": 90,
    "Math": 85,
    "ML": 88,
    "Deep Learning": 92
}

passed = {
    subject: score
    for subject, score in scores.items()
    if score >= 90
}
print(passed)

add_number_in_eachsubject = {
    subject: score + 5
    for subject, score in scores.items()

}
print(add_number_in_eachsubject)