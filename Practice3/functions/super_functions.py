# super() function

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print("Name:", self.name, "| Age:", self.age)


class Student(Person):
    def __init__(self, name, age, major):
        super().__init__(name, age)
        self.major = major

    def show(self):
        super().show()
        print("Major:", self.major)


class GradStudent(Student):
    def __init__(self, name, age, major, thesis):
        super().__init__(name, age, major)
        self.thesis = thesis

    def show(self):
        super().show()
        print("Thesis:", self.thesis)


p = Person("Mr Smith", 45)
s = Student("Bekri", 19, "Computer Science")
g = GradStudent("Dana", 23, "AI", "Machine Learning")

p.show()
print()
s.show()
print()
g.show()
