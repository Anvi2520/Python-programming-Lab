#Write a python program to check if a no. is even or odd with functions.
num=int(input("Enter a number:"))
def find(num):
    if num%2==0:
        print("This is an even number")
    else:
        print("This is an odd number")
find(num);
