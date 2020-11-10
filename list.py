num_list=[1,2,3,4,5,6,7,8,9]
print("List of elements in num_list is: ",num_list)
print(num_list[0])
print(num_list[5])
print(num_list[2:5])
print(num_list[::2])
print(num_list[::1])
print(num_list[1::3])
num_list.append(10)
print(num_list)
del num_list[3]
print(num_list)
num_list[3]=4
print(num_list)
del num_list[2:4]
print(num_list)
