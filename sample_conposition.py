class Horse:
    def __init__(self,name,owner):
        self.name = name
        self.owner = owner
        print("created horse")

class Rider:
    def __init__(self,name):
        self.name = name
        print("created rider")


yuki = Rider("yuki")
hon = Horse("hon",yuki)

print(hon.owner.name)