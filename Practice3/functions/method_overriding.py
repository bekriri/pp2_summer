# method overriding

class Shape:
    def area(self):
        return 0

    def show(self):
        print("Area:", self.area())


class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        import math
        return math.pi * self.r * self.r


class Rectangle(Shape):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


c = Circle(5)
r = Rectangle(4, 6)
t = Triangle(3, 8)

c.show()
r.show()
t.show()
