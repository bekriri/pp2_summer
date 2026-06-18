# class definition and objects

class Dog:
    species = "dog"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(self.name + " says woof!")

    def info(self):
        print(self.name, "is", self.age, "years old")


dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)

dog1.bark()
dog2.bark()
dog1.info()

print(dog1.species)

dog1.age = 4
print(dog1.age)
