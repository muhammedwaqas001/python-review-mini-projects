employee = ("Waqas", 25, "AI Engineer", 120000)
name, age, job, salary = employee
print(name)
print(age)
print(job)
print(salary)

scores = (85, 90, 78, 92, 88, 95)
first, *middle, last = scores
print(first)
print(middle)
print(last)

#concatenation of tuples

python_topics = ("Python", "OOP", "Functions")
ai_topics = ("Machine Learning", "Deep Learning")

all_topics = python_topics + ai_topics
print(all_topics)
print(python_topics)
print(ai_topics)


#tuple repitation

days = ("Monday", "Tuesday")

weekdays = days * 3
print(weekdays)
print(days)


# in and not in 

skills = ("Python", "NumPy", "Pandas", "Machine Learning")
print("Python" in skills)
print("Pandas" in skills)
print("Java" not in skills)
print("Machine Learning" not in skills) 