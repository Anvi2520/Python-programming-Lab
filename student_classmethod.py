#1.Write a python program that uses class to store the name and marks of students. Use list to store the marks in three subjects.
class students:
    def __init__(self, name):
        self.name = name
        self.marks = []
    def EMarks(self):
        for i in range(3):
            m = int(input("Enter the marks of %s in subject %d: "%(self.name,i+1)))
            self.marks.append(m)
    def display(self):
        print (self.name, "list of marks are ", self.marks)
             
name = input("Enter the name of Student:")
s1 = students(name)
s1.EMarks()
name = input("Enter the name of Student:")
s2 = students(name)
s2.EMarks()
name = input("Enter the name of Student:")
s3 = students(name)
s3.EMarks()
s1.display()
print ("")
s2.display()
print ("")
s3.display()
print ("")
