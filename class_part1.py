class Student:
    school = "ABC School"
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks
    def display_info(self):
        print(f"Name of student is: {self.name}")
        print(f"Age of student is: {self.age}")
        print(f"Marks of student is: {self.marks}")
    def is_passed(self):    
        return self.marks >= 50   
            
         

student1= Student("Waqas", 24, 98)
student2= Student("Ali", 25, 49)

student1.display_info()
print("Passed:", student1.is_passed())
print(student1.school)
student2.display_info()
print("Passsed:", student2.is_passed())
print(student2.school)
print("Changing School")
Student.school = "MWM Group of Schools"
student1.school = "XYZ School"
print(student1.school)
del student1.school
print("now changing class varibale")
print(student1.school)
print(student2.school)
    