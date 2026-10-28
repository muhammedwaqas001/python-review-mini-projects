company = "AI Solutions"

def outer():
    department = "AI Engineering"

    def employee():
        name = "Waqas"

        print("Name: ", name)
        # nonlocal department
        print("Department: ", department)
        # global company
        print("Company: ", company)

    employee()

outer()