def create_counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count
    return increment

counter = create_counter()
# print(counter())
# print(counter())
# print(counter())  
# counter = create_counter()

print(counter())  # 1
print(counter())  # 2

another_counter = create_counter()

print(another_counter())  # 1
print(counter())          # 3      