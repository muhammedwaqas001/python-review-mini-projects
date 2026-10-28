import re 

text = "Waqas email is waqas@example.com, age 25, salary 75000"
email = re.findall(r"\w+@\w+\.\w+", text)
numbers = re.findall(r"\d+", text)
clean_data = re.sub(r"\d+", "", text)
print(clean_data)
print(numbers)
print(email)
# text = "AI2026 Engineer123 Pakistan456"
# sub_re = re.sub(r"\d+", "", text)
# print(sub_re)

# text = "Waqas123AI456"

# text_without_digits = re.findall(r"[^0-9]+", text)
# print(text_without_digits)
# text = "I want to learn Java"

# result = re.search(r"Python|Java", text)
# if result:
#     print(result.group())

# text = "Waqas scored 95 marks in Python"

# score = re.search(r"Waqas scored (\d+)", text)
# if score:
#     print(score.group(0))
#     print(score.group(1))

# code = "12345"
# check_code = re.fullmatch(r"^\d{5}$", code)
# if check_code:
#     print("Valid code")
# else:
#     print("Invalid code")    
# Check karo ke code exactly 5 digits ka hai

# text = "AI is the future"

# start = re.findall(r"^AI", text)
# end = re.findall(r"future$", text)
# print(start)
# print(end)

# text = "ac abc abbc abbbc axc"

# result = re.findall(r"a*", text)
# print(result)

# text = "cat bat rat mat"

# result = re.findall(r"[cr]at", text)
# print(result)

# text = "AI Engineer 2026"

# text1 = re.findall(r"\s", text)
# print(text1)
# text2 = re.findall(r"\.", text)
# print(text2)

# text = "Waqas_123 is learning Python"

# word_gropus = re.findall(r"\w+",text )
# numbers = re.findall(r"\d+", text)
# print(numbers)
# print(word_gropus)

# text = "Waqas has 3 projects, 12 books and 2500 rupees"

# numbers = re.findall(r"\d+", text)
# print(numbers)

