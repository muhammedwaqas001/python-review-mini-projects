user_input = "   I Love Python and AI   "

text_without_spaces = user_input.strip()
print(text_without_spaces)
lower_string = text_without_spaces.lower()
print(lower_string)
replaced_string = lower_string.replace("python", "machine learning")
print(replaced_string)
converted_string = replaced_string.split()
print(converted_string)
joined_list = "-".join(converted_string)
print(joined_list)