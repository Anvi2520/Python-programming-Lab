#2. Write a python program to find the factorial of  given no. using functions.
num=int(input("Enter a number:"))
def factorial(num):
    fact=1
    if num<0:
        print("factorial does not exist")
    elif num==0:
        print("the factorial for 0 is 1")
    else:
        for i in range(1,num+1):
            fact=fact*i
        print("The factorial of the given no. is",fact)
factorial(num);
