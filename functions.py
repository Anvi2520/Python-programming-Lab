#1.Write a program that finds a given character is present in a string or not. In case it is present it prints the index at which it is present. Do not use builtin find function to search the character.
#2.Write a program that counts the occurences of a character in a string. Do not use built in count function.
#3.Modify the above program so that it starts counting from the specified location.
#4.Write a program to reverse a string.
#5.Write a program using filter function to a list of squares of no.s from 1-10. Then use for..in construct to sum the elements in the list generated.

#1.
def search(str,x):
    for i in range(0,len(str)):
        if(x==str[i]):
            print("character ", x," is present at index",i)
        
print("Enter the string")
str=input()
print("Enter the character to be searched:")
x=input()
search(str,x)


#2.
def search(str,x):
    count=0
    for i in range(0,len(str)):
        if(x==str[i]):
            count+=1
    print("This character occured ",count," times")
print("\nEnter the string")
str=input()
print("Enter the character to be counted:")
x=input()
search(str,x)


#3.
def countchar(str,a,b):
    count = 0
    for i in str[b:]:
        if i == a:
            count = count+1
    print("The character '",a,"' occurred '",count,"' times")

str = input("\nEnter a string: ")
a = input("Enter which character to count ouccurence: ")
b = int(input("Enter a number from which the occurred character should be counted: "))
countchar(str,a,b)


#4.
def reverse(str): 
  s = "" 
  for i in str: 
    s = i + s
  return s
print("\nEnter the string")
str=input()
print("The original string  is : ",end="") 
print(str) 
print("The reversed string is : ",end="") 
print(reverse(str)) 

#5.
def sqr(x):
    return (x**2)
square=[]
square=list(filter(sqr,range(1,11)))
print("Squares of no.s 1-10 ", square)
sum=0
for i in square:
    sum+=i
print("Sum of squares ",sum)
