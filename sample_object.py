class Shape:
    def __init__(self,w,l):
        self.width = w
        self.len = l
        print("created shape")

    def what_am_i(self):
        print("I am a shape")

class Rectangle:
    def __init__(self,w,l):
        self.width = w
        self.len = l
        print("created rectangle")

    def calculate_perimeter(self):
        return self.width * 2 + self.len * 2

class Square:
    def __init__(self,w):
        self.width = w
        print("created square")
    
    def calculate_perimeter(self):
        return self.width * 4

    def change_size(self,w):
        self.width += w

rectangle = Rectangle(10,10)
print(rectangle.calculate_perimeter())

square = Square(10)
print(square.calculate_perimeter())
square.change_size(5)
print(square.calculate_perimeter())