file=open("File1.txt","wb")
print("Name of the file: ",file.name)
print("File is closed",file.closed)
print("File has been opened in ",file.mode," mode")
print("File is now being closed.. you cannot access the file.")
file.close()
print("file is closed")
print(file.read())
