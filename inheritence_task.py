class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def show_details(self):
         print(f"Employee {self.name} is taking {self.salary} as salary.")
class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)              
        self.programming_language = programming_language
    def show_details(self):
        print("Name: ", self.name)
        print("Salary: ", self.salary)
        print("Programming language: ", self.programming_language) 

developer = Developer("Waqas", 100000, "Python")
developer.show_details()