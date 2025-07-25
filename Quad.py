from Point import Point
from Shape import Shape

class Quad(Shape):
    def __init__(self, point1, point2, point3, point4):
        self.point1 = point1
        self.point2 = point2
        self.point3 = point3
        self.point4 = point4
    def __str__(self):
        return str(self.point1) +", "+ str(self.point2) +", "+ str(self.point3) +", "+ str(self.point4)
    def area(self):
        return((self.point4.distance(self.point3) + self.point1.distance(self.point2)) / 2) * ((self.point1.distance(self.point4) + self.point2.distance(self.point3)) / 2)
    def perimeter(self):
        return (self.point1.distance(self.point2) + self.point2.distance(self.point3) + self.point3.distance(self.point4) + self.point4.distance(self.point1))
cheese = Quad(Point(0,0,0), Point(0,1,0), Point(1,1,0), Point(1,0,0))
print(cheese.area())
print(cheese.perimeter())