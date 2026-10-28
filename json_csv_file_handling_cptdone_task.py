import json
import csv

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

# ---------------- JSON WRITE ----------------

with open("data/student.json", "w", encoding="utf-8") as file:
    json.dump(student, file, indent=4)


# ---------------- JSON READ ----------------

with open("data/student.json", "r", encoding="utf-8") as file:
    student_data = json.load(file)

print("JSON Data")
print("Name:", student_data["name"])
print("Course:", student_data["course"])


# ---------------- CSV WRITE ----------------

csv_student = {
    "name": student["name"],
    "age": student["age"],
    "course": student["course"]
}

with open("data/student.csv", "w", newline="", encoding="utf-8") as file:
    fieldnames = ["name", "age", "course"]

    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow(csv_student)


# ---------------- CSV READ ----------------

with open("data/student.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for student_data in reader:
        print("\nCSV Data")
        print("Name:", student_data["name"])
        print("Course:", student_data["course"])