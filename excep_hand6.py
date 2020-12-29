#2. Write a program that prompts the user to enter the number. If the number is positive or zero print it. Otherwise raise an error.
try:
    num=int(input("Enter the number: "))
    if(num>=0):
        print(num)
    else:
        raise Exception
except:
    print("Error! Negative number!")
