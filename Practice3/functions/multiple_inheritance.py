# multiple inheritance

class Flyable:
    def fly(self):
        print(self.name, "is flying")


class Swimmable:
    def swim(self):
        print(self.name, "is swimming")


class Walkable:
    def walk(self):
        print(self.name, "is walking")


class Duck(Flyable, Swimmable, Walkable):
    def __init__(self, name):
        self.name = name

    def quack(self):
        print(self.name, "- quack!")


class FlyingFish(Flyable, Swimmable):
    def __init__(self, name):
        self.name = name


d = Duck("Donald")
d.fly()
d.swim()
d.walk()
d.quack()

f = FlyingFish("Nemo")
f.fly()
f.swim()
