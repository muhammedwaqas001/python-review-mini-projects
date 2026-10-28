from itertools import chain, count, cycle, repeat, product, permutations, combinations, combinations_with_replacement, zip_longest, filterfalse, compress, groupby, accumulate, pairwise, starmap

# model_scores = [70, 85, 78, 92, 88]

# result = accumulate(model_scores, max)
# print(list(result))

model_scores = [60, 75, 70, 90]

result = accumulate(model_scores, max)
print(list(result))

# models = ["Model A", "Model B", "Model C"]
# datasets = ["Text", "Images", "Audio"]

# experiments = product(models, datasets)

# for experiment in experiments:
#     print(experiment)
# numbers_of_models_dataset = len(models) * len(datasets)
# print(numbers_of_models_dataset)
# experiment_results = [
#     ("Model A", 90),
#     ("Model B", 85),
#     ("Model C", 95)
# ]
# result = starmap(print, experiment_results)
# list(result)

# numbers = [(10, 2), (20, 3), (30, 4)]
# result = starmap(pow, numbers)
# print(list(result))

# accuracies = [60, 68, 75, 82, 85]

# for previous, current in pairwise(accuracies):
#     change = current - previous
#     print(change)


# daily_costs = [500, 300, 700, 200]

# result = accumulate(daily_costs)
# print(list(result))


# students = [
#     ("Ali", "Python"),
#     ("Sara", "AI"),
#     ("Waqas", "Python"),
#     ("Ahmed", "AI"),
#     ("Zoya", "Python")
# ]

# sorted_students = sorted(students, key = lambda student:student[1])




# for category, group in groupby(sorted_students, key= lambda student: student[1]):
#     print(category, list(group))



# models = ["GPT", "Llama", "Gemini", "Claude", "DeepSeek"]
# selectors = [True, False, True, True, False]

# result = compress(models, selectors)
# print(list(result))

# model_scores = [92, 45, 78, 30, 88, 50, 25]

# result = filterfalse(lambda score:score >= 50, model_scores )
# print(list(result))
# skill_groups = [
#     ["Python", "OOP"],
#     ["NumPy", "Pandas"],
#     ["Machine Learning", "Deep Learning"]
# ]
# result = chain.from_iterable(skill_groups)
# print(list(result))

# models = ["GPT", "Llama", "Gemini", "Claude"]
# accuracy = [95, 88, 92]

# result = zip_longest(models, accuracy, fillvalue="Not Found.")

# print(list(result))

# models = ["A", "B", "C"]

# permuted_models = permutations(models, 2)
# combined_models = combinations(models, 2)
# combined_models_with_repeat = combinations_with_replacement(models, 2)
# print(list(permuted_models))
# print(list(combined_models))
# print(list(combined_models_with_repeat))

# result = combinations_with_replacement(models, 2)
# print(list(result))

# skills = ["Python", "SQL", "Git"]

# result = combinations(skills, 2)
# print(list(result))

# models = ["A", "B", "C"]
# result = permutations(models, 2)

# print(list(result))

# models = ["Model A", "Model B"]
# datasets = ["Dataset 1", "Dataset 2", "Dataset 3"]

# model_set_combo = product(models, datasets)
# print(list(model_set_combo))

# repeated_skill = repeat("AI Engineer", 4)
# print(list(repeated_skill))

# ai_skills = ["Python", "Machine Learning", "Deep Learning"]
# cycle_skills = cycle(ai_skills)

# print(next(cycle_skills))
# print(next(cycle_skills))
# print(next(cycle_skills))
# print(next(cycle_skills))


# counter = count(10, 5)
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))

# python_skills = ["Python", "OOP", "Functions"]
# ai_skills = ["Machine Learning", "Deep Learning"]

# combined_items = chain(python_skills, ai_skills)
# print(next(combined_items))
# print(next(combined_items))
# print(next(combined_items))
# print(next(combined_items))

# python_skills = ["Python", "OOP", "Functions"]
# ai_skills = ["Machine Learning", "Deep Learning"]
# combined_list = chain(python_skills, ai_skills)

# print(list(combined_list))