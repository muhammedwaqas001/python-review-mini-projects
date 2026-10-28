class Student:
    school = "XYZ School"
    def __init__(self, name, age):
        
        self.name = name
        self.age = age
    @classmethod
    def change_school(cls, new_school):
        cls.school = new_school

    @classmethod
    def from_string(cls, student_data):
        name, age = student_data.split(",")
        return cls(name, int(age))

    @staticmethod
    def is_adult(age):
        return age >= 18
        
student1 = Student.from_string("Waqas,24")
student2 = Student("Imtiaz", 28)

Student.change_school("MWM School")

print(student1.name, student1.age)
print(student2.name, student2.age)
print(student1.school)
print(student2.school)

print(Student.is_adult(24))
print(Student.is_adult(16))