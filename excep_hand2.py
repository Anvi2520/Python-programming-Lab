try:
    file=open('File1.txt')
    str=file.readline()
    print(str)
except IOError:
    print("Error occured during Input")
except ValueError:
    print("Could not convert to integer")
except:
    print("Unexpected error")
