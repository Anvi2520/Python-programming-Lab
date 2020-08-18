def fibo(n):
    if n<=1:
        return n
    else:
        return(fibo(n-1)+fibo(n-2))
n=int(input("Enter the number of terms-"))
if n<=0:
    print("You have entered a negative number")
else:
    print("The sequence is:")
    for i in range(n):
        print(fibo(i))