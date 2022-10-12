import math
 
 
# Parent class
class Polygon:
    def getSides(self):
        return 0
 
    def getgetArea(self):
        return 0
 

# Child class inherited from Polygon
class Triangle(Polygon):
    def getSides(self):
        return 3
 
    def getArea(self, base, height):
        area =  base * height / 2
        return area
 

# Child class inherited from Polygon
class Square(Polygon):
    def getSides(self):
        return 4
 
    def getArea(self, length, width):
        area = length * width
        return area
 

# Child class inherited from Polygon
class Pentagon(Polygon):
    def getSides(self):
        return 5
 
    def getArea(self, a):
        area = 1 / 4 * math.sqrt(5 * (5 + 2 * math.sqrt(5))) * a ** 2
        return area

 
# Create triangle object
tri = Triangle()

# Call getArea method for triangle
print (tri.getArea(22, 22))

# Create pentagon object
pent = Pentagon()

# Call getArea method for pentagon
print (pent.getArea(22))


