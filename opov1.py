#1. Write a program that overloads the + operator on a class student that has attributes name and marks.
class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def display(self):
        print(self.name,self.marks)
    def __add__(self,S):
        temp=Student(S.name,[])
        for i in range(len(self.marks)):
            temp.marks.append(self.marks[i] + S.marks[i])
        return temp
S1=Student("Anvitha", [87,90,98])
S2=Student("Anvitha", [78,90,89])
S1.display()
S2.display()
S3=Student("",[])
S3=S1+S2
S3.display()
