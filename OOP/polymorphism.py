from abc import ABC, abstractmethod
class Shape():
    @abstractmethod
    def area(self):
        pass
class circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14*self.radius*self.radius
class square(Shape):
    def __init__(self,length):
        self.length=length
    def area (self):
        return self.length*self.length
class triangle(Shape):
    def __init__(self,base,height):
        self.base=base
        self.height=height
    def area(self):
        return 0.5*self.base*self.height
class pizza(circle):
    def __init__(self,topping,radius):
        super().__init__(radius)
        self.topping=topping
shapes=[circle(7),square(4),triangle(4,5),pizza("pineapple",7)]

for shape in shapes:
    print(shape.area())