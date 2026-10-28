with open("data/student.txt", "w", encoding="utf-8") as file:
    file.write(
        "Name: Waqas"
        "\nCourse: AI Engineering"
        "\nGoal: AI Engineer"   
    )

with open("data/student.txt", "r", encoding="utf-8") as file:
    content = file.read()    
    print(content)
    current_position = file.tell()
    print("Cursor position:", current_position)
    file.seek(0)
    first_five_chars = file.read(5)
    print(first_five_chars)