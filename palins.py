# 4. Write a python program to check whether a string is palindrome or not.
s=input("Enter a string")  
for i in range(0, int(len(s)/2)):  
    if s[i] != s[len(s)-i-1]: 
         print("This is not a palindrome")
print("This is a palindrome.")
