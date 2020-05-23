import math
class Apple:
    def __init__(self,w,c):
        """weight はグラム"""
        self.weight = w
        self.color = c
        self.mold = 0
        print("created!")


class Circle:
    def __init__(self,r):
        """r は半径[mm]"""
        self.r = r
        print("created circle")
    
    def area(self):
        return self.r * self.r * math.pi

class Triangle:
    def __init__(self,t,h):
        """t,h は単位[mm]のこと"""
        self.teihen = t
        self.height = h
        print("created Triangle")
    
    def area(self):
        return self.teihen * self.height / 2.0

circle = Circle(10)
print(circle.area())

triangle = Triangle(10,5)
print(triangle.area())