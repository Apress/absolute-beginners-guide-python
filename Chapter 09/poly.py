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


square = Square(3,3)

print (square.getArea())


triangle = Triangle(3,4)

print (triangle.getArea())

