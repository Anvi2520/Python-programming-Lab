try:
    file=open('File1.txt')
    str=file.readline()
    print(str)
except IOError:
    print("Error occured during Input")
else:
    print("Program terminating successfully")
