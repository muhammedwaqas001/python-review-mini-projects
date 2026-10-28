class Employee:
    company = "MWM AI Solutions"
    def __init__(self, name, age, salary, password):
        self.name = name
        self.age = age
        self._salary = salary
        self.__password = password
    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Salary: {self._salary}")
    def get_password(self):
        return self.__password
    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company
    @classmethod
    def from_string(cls, data):
        name, age, salary, password = data.split(",")
        return cls(name, int(age), int(salary), password)  
    @staticmethod
    def is_adult(age):
        return age >= 18
employee1 = Employee("Waqas",24, 12399999, "abc123")                      
employee2 = Employee("Khizar",22, 12399999, "abc098")
employee3 = Employee.from_string("Ali,17,290000,bca21")
Employee.change_company("MWM Daires")
print("First Employee details.")
employee1.show_details()  
print("Comany: ", employee1.company)      
print("Second Employee details")              
employee2.show_details()
print("Company: ", employee2.company)
print(employee1.get_password())
print(Employee.is_adult(24))
print(Employee.is_adult(17))
print(employee3.name, employee3.age, employee3._salary, employee3.get_password())