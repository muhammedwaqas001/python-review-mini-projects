with open("student_utf.txt", "w",encoding="utf-8") as file:
    file.write(
        "Name: Waqas"
        "\nLanguage: Urdu"
        "\nMessage: میرا نام وقاص ہے"
    )
with open("student_utf.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print(content)    