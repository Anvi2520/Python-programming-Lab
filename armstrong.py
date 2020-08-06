# 5. Write a program to find whether a given number is armstrong number or not.
num = int(input("Enter a number: "))  
sum = 0  
x = num  
while x > 0:  
   digit = x % 10  
   sum += digit ** 3  
   x //= 10  
if num == sum:  
   print(num,"is an Armstrong number")  
else:  
   print(num,"is not an Armstrong number") 
