message="Hello!"
index=0
for i in message:
    print("message[",index,"]=",i)
    index+=1

str="Hello, welcome to the world of python"
i=2
print(str[i])
print(str[i*3])

print(str.upper())
print(str.lower())
print(str.split())
print("join-",'-'.join(str.split()))
print(str.replace("python","java"))
print(str.find("of"))

