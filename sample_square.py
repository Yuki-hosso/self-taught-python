class Square:
    square_list = []

    def __init__(self,w):
        self.width = w
        self.square_list.append(self.width)
        print("created square")

    def __repr__(self):
        return "{} by {} by {} by {}".format(self.width,self.width,self.width,self.width)

def compare(com1,com2):
    return com1 is com2

square = Square(10)
square2 = Square(20)
print(square.square_list)
print(Square(29))

print(compare(square,square2))

same_square = square
print(compare(square,same_square))