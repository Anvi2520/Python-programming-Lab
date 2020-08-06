#7. Write a program to print the table of a given number using functions.
num = int(input("Enter the number: "))
def table(num):
    print("Multiplication Table of", num)
    for i in range(1, 11):
       print(num,"X",i,"=",num * i)
table(num)
