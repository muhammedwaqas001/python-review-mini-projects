user_text = "   Python is powerful and Python is easy   "
text_without_spaces = user_text.strip()
lower_text = text_without_spaces.lower()
python_times = lower_text.count("python")
replaced_text = lower_text.replace("python","ai")
splited_text = replaced_text.split()
lenght_of_text = len(splited_text)
joined_text = "-".join(splited_text)
print(f"Python appears {python_times} times.\n Total words: {lenght_of_text}\n Processed text: {joined_text}")