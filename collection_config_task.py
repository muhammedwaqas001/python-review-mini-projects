# from collections import ChainMap

# default_config = {
#     "model": "GPT",
#     "temperature": 0.7,
#     "max_tokens": 1000
# }

# custom_config = {
#     "temperature": 0.3
# }

# # Yahan ChainMap banayein
# config = ChainMap(default_config, custom_config)

# # Model print karein
# print(config["model"])
# # Temperature print karein
# print(config["temperature"])
# # Max tokens print karein
# print(config["max_tokens"])

# numbers = [10, 20, 30]

# values = numbers

# values.append(40)

# numbers = [1, 2, 3]

# print(numbers)
# print(values)

# import copy

# original = [[10, 20], [30, 40]]

# shallow = copy.copy(original)
# deep = copy.deepcopy(original)

# original[0].append(99)

# print(original)
# print(shallow)
# print(deep)

# import copy

# original = {"skills": ["Python", "SQL"]}
# shallow = copy.copy(original)

# shallow["skills"].append("NumPy")
# shallow["level"] = "Beginner"

# print(original)
# print(shallow)

# import gc

# numbers = [10, 20, 30]
# backup = numbers

# del numbers

# print(backup)

a = [1, 2, 3]
b = a
c = a.copy()

a.append(4)

print(b)
print(c)