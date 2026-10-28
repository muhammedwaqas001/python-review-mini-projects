import json
import csv

employee = {
    "name": "Waqas",
    "age": 25,
    "department": "AI Engineering",
    "skills": ["Python", "Machine Learning", "Deep Learning"],
    "salary": 100000
}

with open("data/employee.json", "w", encoding="utf-8") as file:
    json.dump(employee, file, indent= 4)

with open("data/employee.json", "r", encoding="utf-8") as file:
    employee_data = json.load(file)

print("JSON Data")
print("Name: ", employee_data["name"])
print("Department: ", employee_data["department"])
print("Salary: ", employee_data["salary"])
print("Skills: ", employee_data["skills"])

for skill in employee_data["skills"]:
    print(skill)

csv_employee = {
    "name": employee["name"],
    "age": employee["age"],
    "department": employee["department"],
    "salary": employee["salary"]
}
    
with open("data/employee.csv", "w", newline="", encoding="utf-8") as file:
    fieldnames = ["name", "age", "department", "salary"]

    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow(csv_employee)

with open("data/employee.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for employee_data in reader:
        print("CSV Data")
        print("Name: ", employee_data["name"])
        print("Age: ", employee_data["age"])
        print("Department: ", employee_data["department"])
        print("Salary", employee_data["salary"])
