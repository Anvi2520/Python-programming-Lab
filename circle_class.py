#4. Write a program that has a class Circle. Use a class variable to define the value of constant Pi. Use this class variable to calculate area and circumference of a circle with specified radius.
class Circle():
    pi=3.14
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return Circle.pi*(self.radius**2)
    def circumference(self):
        return 2*(Circle.pi)*(self.radius)
r=int(input("Enter radius of circle: "))
obj=Circle(r)
print("Area of circle:",obj.area())
print("Circumference of circle:",obj.circumference())
