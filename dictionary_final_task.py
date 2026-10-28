student = {
    "name": "Waqas",
    "age": 25,
    "course": "AI Engineering",
    "skills": ["Python", "NumPy", "Pandas"],
    "scores": {
        "Python": 90,
        "Math": 85,
        "ML": 88
    }
}


# 1. Print name, age and course
print(student["name"])
print(student["age"])
print(student["course"])


# 2. Print skills
print(student["skills"])


# 3. Add Git to skills
student["skills"].append("Git")


# 4. Change age
student["age"] = 26


# 5. Add city
student["city"] = "Multan"


# 6. Access city using get()
print(student.get("city"))


# 7. Access a key that doesn't exist using get()
print(student.get("email", "Email not found"))


# 8. Update multiple values
student.update({
    "age": 27,
    "course": "Machine Learning"
})


# 9. Check whether "name" exists
print("name" in student)


# 10. Check whether "Python" exists in skills
print("Python" in student["skills"])


# 11. Print all keys
print(student.keys())


# 12. Print all values
print(student.values())


# 13. Print all key-value pairs
print(student.items())


# 14. Loop through the dictionary
for key, value in student.items():
    print(key, ":", value)


# 15. Access Python score from nested scores dictionary
print(student["scores"]["Python"])


# 16. Find the highest score
highest_score = max(student["scores"].values())
print("Highest Score:", highest_score)


# 17. Find total score
total_score = sum(student["scores"].values())
print("Total Score:", total_score)


# 18. Loop through scores
for subject, score in student["scores"].items():
    print(subject, ":", score)


# 19. Check whether Python exists in scores
print("Python" in student["scores"])


# 20. Dictionary comprehension
squares = {
    number: number ** 2
    for number in range(1, 6)
}

print(squares)


# 21. Remove city using pop()
removed_city = student.pop("city")
print("Removed city:", removed_city)

print(student)