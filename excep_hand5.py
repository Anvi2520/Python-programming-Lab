#1. Write a program that prompts the user to enter a number and prints its square. If no number is entered(ctrl+c is pressed), the keyboard interrupt is generated.
try:
    num=int(input("Enter the number: "))
    print(num**2)
except KeyboardInterrupt:
    print("Keyboard Interrupt Error Generated.")
