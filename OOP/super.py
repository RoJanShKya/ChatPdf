class Shape:
    def __init__ (self, color, filled):
        self.color=color
        self.filled= filled
class circle(Shape):
    def __init__ (self,color, filled, radius):
        super().__init__(color,filled)
        self.radius=radius 
    def area(self):
        return 3.14*self.radius*self.radius
class square(Shape):
    def __init__ (self,color, filled,length):
        super().__init__(color,filled)
        self.length=length       
class rectangle(Shape):
    def __init__ (self,color, filled,length, breadth):
        super().__init__(color,filled)
        self.length=length   
        self.breadth=breadth
    def area(self):
        area=self.length*self.breadth
        return area          

Circle=circle("red",True,7)
print(Circle.color)
print(Circle.filled)
print(Circle.radius)
print(Circle.area())

Rectangle=rectangle("blue",False,4,5)
print(Rectangle.color)
print(Rectangle.filled)
print(Rectangle.length)
print(Rectangle.breadth)
print(f"{Rectangle.area()} is the area of the given rectangle")
