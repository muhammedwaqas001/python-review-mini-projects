python_skills = {
    "Python",
    "OOP",
    "Functions",
    "Git",
    "SQL"
}

ai_skills = {
    "Python",
    "Machine Learning",
    "Deep Learning",
    "Git",
    "NumPy"
}
new_set = {
    "Python",
    "Git"
}
personal_info = {
    "Muhammad",
    "Waqas"
}
even_numbers ={x for x in range(1,11) if x % 2 == 0}
numbers = [1, 2, 2, 3, 3, 4, 4, 5]
print(python_skills)
print(ai_skills)
python_skills.add("Pandas")
ai_skills.update(["PyTorch", "TensorFlow"])
print("Python" in ai_skills)
print(python_skills | ai_skills)
print(python_skills & ai_skills)
print(python_skills - ai_skills)
print(ai_skills - python_skills)
print(python_skills ^ ai_skills)
print(new_set <= python_skills)
print(python_skills >= new_set)
print(python_skills.isdisjoint(personal_info))
print(len(python_skills))
python_skills_list = list(python_skills)
numbers_set = set(numbers)
print(numbers_set)
print(even_numbers)
python_skills.remove("Git")
print(python_skills)
ai_skills.discard("Deep Learning")
print(ai_skills)
odd_number = frozenset({1, 3, 5, 7})
print(type(odd_number))