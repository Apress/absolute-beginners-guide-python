class Polygon:
    def __init__(self, width, height):
        self.width = width
        self.height = height

class Triangle(Polygon):
    def getArea(self):
        return self.width * self.height / 2

class Square(Polygon):
    def getArea(self):
        return self.width * self.height

class Circle:
    def __init__(self, radius):
        self.radius = radius
        
    def getArea(self):
        return 3.14 * self.radius ** 2

  

square = Square(3,3)
triangle = Triangle(3,4)
circ = Circle(3)


print(square.getArea())

print(triangle.getArea())

print(circ.getArea())
