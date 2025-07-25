from Point import Point
from Shape import Shape
from Quad import Quad
from Tri import Tri
from Circ import Circ


quad = Quad(Point(0,0,0), Point(0,1,0), Point(1,1,0), Point(1,0,0))
tri = Tri(Point(0,0,0), Point(1,1,0), Point(2,0,0))
circ = Circ(4, [0,0,0])

shapes = [quad, tri, circ]
for i in shapes:
    print(i.area())
    print(i.perimeter())
    print("")