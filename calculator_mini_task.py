number1 = input("Enter first number: ")
number2 = input("Enter second number: ")
operator = input("Enter operator (+, -, *, /): ")

try:
    number1 = int(number1)
    number2 = int(number2)
    if operator == "+":
        result =  number1 + number2
    elif operator == "-":
        result =  number1 - number2
    elif operator == "*":
        result = number1 * number2
    elif operator == "/":
        result = number1 / number2
    else:
        raise ValueError("Invalid operator")


   

except ValueError as error:
    print("Error:", error)

except ZeroDivisionError:
    print("Cannot divide by zero.")

else:
    print("Result : ", result)

finally:
    print("Calculation finished.")