# with open("student.txt", "r") as file:
#     content2 = file.read()
#     print("Read")
#     print(content2)

#     file.seek(0)
#     content = file.readline()
#     print("First Line")
#     print(content)

#     file.seek(0)
#     all_lines = file.readlines()
#     print("All lines")
#     print(all_lines)
    

with open("student.txt","r") as file:
    curser_starting_position = file.tell()
    first_five_chars = file.read(5) 
    current_curser_position = file.tell()
    file.seek(0)
    five_chars_again = file.read(5)
    final_curser_position = file.tell()

    print("Starting position: ", curser_starting_position)
    print("First 5 characters: ", first_five_chars)
    print("Position after reading: ", current_curser_position)
    print("First 5 characters again: ", five_chars_again)
    print("Final position: ", final_curser_position)

