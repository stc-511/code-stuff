from Shape import Shape
import math

class Circ(Shape):
    def __init__(self, radius, center):
        self.radius = radius
        self.center = center
    def __str__(self):
        return ("Radius is", str(self.radius) + ".", "Area is", str(self.area()) + ".", "Circumfrence is", str(self.perimeter()) + ".", "Center point is at", str(self.center) + ".")
    def area(self):
        return math.pi*self.radius**2
    def perimeter(self):
        return 2*math.pi*self.radius
cheese = Circ(4, [0,0,0])
print(cheese.area())
print(cheese.perimeter())