# class variables vs instance variables

class Employee:
    company = "TechCorp"
    count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.count += 1

    def show(self):
        print(self.name, "|", Employee.company, "|", self.salary)


e1 = Employee("Bekri", 150000)
e2 = Employee("Dana", 180000)

e1.show()
e2.show()
print("Total employees:", Employee.count)

# changing class variable
Employee.company = "NewTech"
e1.show()
e2.show()

# changing instance variable only changes that one
e1.salary = 200000
e1.show()
e2.show()
