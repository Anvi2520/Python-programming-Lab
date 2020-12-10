#5. Write a class Rectangle that has attributes length and breadth and a method area which returns the area of the rectangle.
class Rectangle():
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        return self.length*self.breadth
l=int(input("Enter length of the rectangle: "))
b=int(input("Enter the breadth of the rectangle: "))
obj=Rectangle(l,b)
print("Area of rectangle: ",obj.area())
