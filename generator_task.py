# def countdown():
#     yield 5
#     yield 4
#     yield 3
#     yield 2
#     yield 1
# for number in countdown():
#     print(number)    


# def count(start):
#     while start > 0:
#         yield start
#         start -= 1
# for num in count(7):
#     print(num)            


# def even_numbers(limit):
#     for number in range(1,limit + 1):
#         if number % 2 == 0:
#             yield number
# for even in even_numbers(10):
#     print(even)        


sequare_generator = ( number ** 2 for number in range(1,11)  if number % 2 == 0 )

for square in sequare_generator:
    print(square)