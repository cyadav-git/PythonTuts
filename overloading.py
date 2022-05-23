class Baseclass:
    def __init__(self, name):
        self.name = name
    def area1(self):
        pass
    def __str__(self):
        return self.name
class Rectangle(Baseclass):
    def __init__(self, length, breadth):
        super().__init__("Rectangle")
        self.length = length
        self.breadth = breadth
    def area1(self):
        return self.length * self.breadth
class Triangle(Baseclass):
    def __init__(self, height, base):
        super().__init__("Triangle")
        self.height = height
        self.base = base
    def area1(self):
        return (self.base*self.height)/2
a = Rectangle(90, 80)
b = Triangle(77, 64)
print("the shape is: ", b)
print("the area of shape is", b.area1())
print("the shape is ", a)
print("the area of shape is", a.area1())
