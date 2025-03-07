# Parent Class
class Shape:
    def area(self):
        pass

# Child Class-1
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
        
    def area(self):
        return 3.14*self.radius**2

# Child class-2 
class Square(Shape):
    def __init__(self,side):
        self.side=side
        
    def area(self):
        return self.side**2

Area1=Circle(int(input("Enter the radius of circle:")))
print("The area of circle is:")
print(Area1.area())
Area2=Square(int(input("Enter the side of square:")))
print("The area of square is:")
print(Area2.area())
