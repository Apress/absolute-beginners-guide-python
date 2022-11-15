from math import pi


class Polygon:
    def __init__(self, name):
        self.name = name
    def getArea(self):
        pass
    def getName(self):
        return "Polygon"
    def __str__(self):
        return self.name


class Square(Polygon):
    def __init__(self, length):
        super().__init__("Square")
        self.length = length
    def getArea(self):
        return self.length**2
    def getName(self):
        return "Square"


class Circle(Polygon):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius
    def getArea(self):
        return pi*self.radius**2



squareObj = Square(7)
circleObj = Circle(7)


print(circleObj.name)

print(squareObj.getArea())

print(circleObj.getName())



