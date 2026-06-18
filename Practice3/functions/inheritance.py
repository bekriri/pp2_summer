# inheritance basics

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name, "makes a sound")


class Dog(Animal):
    def speak(self):
        print(self.name, "says woof")

    def fetch(self):
        print(self.name, "fetches the ball")


class Cat(Animal):
    def speak(self):
        print(self.name, "says meow")


class Bird(Animal):
    def __init__(self, name, can_fly):
        super().__init__(name)
        self.can_fly = can_fly

    def fly(self):
        if self.can_fly:
            print(self.name, "is flying")
        else:
            print(self.name, "cannot fly")


d = Dog("Buddy")
c = Cat("Whiskers")
b = Bird("Eagle", True)

d.speak()
d.fetch()
c.speak()
b.speak()
b.fly()
