class Stack:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return self.items == []
    def push(self,new_one):
        self.items.append(new_one)
    def pop(self):
        return self.items.pop()
    def peek(self):
        size = len(self.items) - 1
        return self.items[size]
    def size(self):
        return len(self.items)

print("input yesterday")
str_m = Stack()
for i in "yesterday":
    str_m.push(i)

show = ""
for i in range(str_m.size()):
    show += str_m.pop()

print(show)

print("input [1,2,3,4,5]")
num = Stack()
for i in [1,2,3,4,5]:
    num.push(i)

show = []
for i in range(num.size()):
    show.append(num.pop())
print(show)

