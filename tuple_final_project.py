student = (
    "Waqas",
    25,
    "AI Engineering",
    (85, 90, 78, 92, 88),
    ["Python", "NumPy", "Pandas"]
)
extra_skills = ("Machine Learning", "Deep Learning")
print(student[0])
print(student[1])
print(student[2])
scores = student[3]
print(max(scores))
print(min(scores))
print(sum(scores))
print(len(scores))
skills = student[4]
print("Python" in skills)
skills.append("Machine Learning")
first, *middle, last = scores
print(first)
print(middle)
print(last)
name, age, *end = student
print(name)
print(age)
all_skills = tuple(skills) + extra_skills
print(all_skills)
print(type(student))
print(len(student))