from math import sqrt

class Point:
    def __init__(self, x , y, z):
        self.x = x
        self.y = y
        self.z = z
    def __str__(self):
        return("(" + self.x+",", self.y+",", self.z+")")
    def distance(self, point2):
        return sqrt((self.x - point2.x)**2+(self.y - point2.y)**2+(self.z - point2.z)**2)