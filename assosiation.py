class Student:
    def __init__(self, name):
        self.name = name       

class Teacher:
    def __init__(self, name):
        self.name = name
    def teach(self, student):
        return f"Teahcer {self.name} is teaching Student {student.name}"    

student = Student("Waqas")
teacher = Teacher("Ali")
print(teacher.teach(student))       