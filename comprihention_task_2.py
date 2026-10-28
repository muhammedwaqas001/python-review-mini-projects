words = ["python", "ai", "machine", "learning", "data", "model"]
uppercase_words = [word.upper() for word in words ]
print(uppercase_words)
words_of_four_length = [word for word in words if len(word) > 4]
print(words_of_four_length)
lenght_of_words = [len(word) for word in words]
print(lenght_of_words)
more_than_five_chars = [word for word in words if len(word) >= 5]
print(more_than_five_chars)