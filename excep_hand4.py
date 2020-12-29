try:
    file=open('File1.txt')
    str=file.readline()
    print(str)
except:
    print("Error occured")
else:
    print("Program terminating successfully")
