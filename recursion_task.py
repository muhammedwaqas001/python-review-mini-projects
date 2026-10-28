def countdown(number):
    if number == 0:
        return

    print(number)
    countdown(number - 1)    

countdown(5)


#Factorial Function

def factorial(number):
    if number == 0:
        return 1
    return number * factorial(number - 1)
result = factorial(5)
print(result)        