student = {
    "name": "Waqas",
    "scores": {
        "Python": 90,
        "Math": 85,
        "ML": 88
    }
}

try:
    subject = input("Enter subject: ")

    score = student["scores"][subject]

    if score < 0 or score > 100:
        raise ValueError("Score must be between 0 and 100.")

    divisor = int(input("Enter divisor: "))

    result = score / divisor

except KeyError:
    print("Subject not found.")

except ValueError as error:
    print("Invalid input:", error)

except ZeroDivisionError:
    print("Divisor cannot be zero.")

else:
    print("Subject:", subject)
    print("Score:", score)
    print("Result:", result)

finally:
    print("Calculation attempt finished.")