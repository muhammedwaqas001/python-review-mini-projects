from itertools import chain, product
from itertools import combinations
from itertools import permutations
from itertools import cycle
from itertools import repeat
from itertools import accumulate
from itertools import islice
from itertools import count
from itertools import zip_longest
from itertools import groupby

tasks = [
    ("Data Cleaning", "AI"),
    ("Model Training", "ML"),
    ("Model Testing", "ML"),
    ("Data Visualization", "AI"),
]

for a, b in groupby(tasks, key=lambda item: item[1]):
    print(a, list(b))

# skills = ["Python", "NumPy", "Pandas"]
# levels = ["Beginner", "Intermediate"]

# for skill, level in zip_longest(skills, levels, fillvalue= "Not assigned"):
#     print(skill, level)

# for number in count(3):
#     print(number)

#     if number == 7:
#         break

# number =  range(1,10)

# selected_numbers = list(islice(number, 0,4))
# print(selected_numbers)

# numbers = [5, 10, 15, 20]

# print(list(accumulate(numbers)))

# for value in repeat("Python", 5):
#     print(value)
# status = ["Python", "ai"]

# stat_cycle = cycle(status)

# for _ in range(5):
#     print(next(stat_cycle))

# models = ["GPT", "BERT", "Llama"]

# for model_pair in permutations(models, 2):
#     print(model_pair)

# skills = ["Python", "SQL", "NumPy", "Pandas"]

# for pair in combinations(skills, 2):
#     print(pair)

# models = ["GPT", "BERT"]
# environments = ["Development", "Production"]

# for model, environment in product(models, environments):
#     print(model, environment)

# backend_skills = ["Python", "SQL"]
# ai_skills = ["Numpy", "Pandas"]

# for skill in chain(backend_skills, ai_skills):
#     print(skill)


    