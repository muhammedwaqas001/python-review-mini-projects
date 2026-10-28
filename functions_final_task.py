def student_report(name, age, course="AI Engineering", *skills, **details):
    print("Name:", name)
    print("Age:", age)
    print("Course:", course)
    print("Skills:", skills)
    print("Details:", details)

    scores = details["scores"]

    average_score = sum(scores.values()) / len(scores)

    return name, average_score


student_name, average_score = student_report(
    "Waqas",
    25,
    "AI Engineering",
    "Python",
    "NumPy",
    "Pandas",
    scores={
        "Python": 90,
        "Math": 85,
        "ML": 88,
        "Deep Learning": 92
    }
)

print("Student:", student_name)
print("Average Score:", average_score)