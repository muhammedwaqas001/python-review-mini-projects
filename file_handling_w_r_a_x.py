with open("student_info.txt", "w") as file:
    file.write(
        "Name: Waqas"
        "\nCourse: AI Engineering"
        "\nGoal: AI Engineer"
        )
with open("student_info.txt", "a") as file:
    file.write(
        "\nSkill: Python"
        "\nSkill: NumPy"
    )

with open("student_info.txt", "r") as file:
        content = file.read()
        print(content)
with open("student_info.txt", "rb") as file:
    content = file.read()

print(type(content))
print(content)        