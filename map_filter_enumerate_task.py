numbers = [1, 2, 3, 4, 5, 6]
names = ["Ali", "Waqas", "Ahmed"]
scores = [85, 95, 78]

map_numbers = map(lambda number: number ** 2, numbers)
print(list(map_numbers))

filtered_even_numbers = filter(lambda number: number % 2 == 0, numbers)
print(list(filtered_even_numbers))

zip_of_lists = dict(zip(names, scores))
print(zip_of_lists)

for index, name in enumerate(names, start=1):
    print(index, name)