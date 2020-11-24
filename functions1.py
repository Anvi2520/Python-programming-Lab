def check(x):
    if(x%2==0 or x%4==0):
        return 1
evens=list(filter(check,range(2,22)))
print(evens)

def add_2(x):
    x+=2
    return x
num_list=[1,2,3,4,5,6,7]
print("Original :",num_list)
new_list=list(map(add_2,num_list))
print("Modified :",new_list)

def add(x,y):
    return x+y
list1=[1,2,3,4,5]
list2=[6,7,8,9,10]
list3=list(map(add,list1,list2))
print("Sum of",list1,"and",list2,"=",list3)

import functools
def addition(x,y):
    return x+y
num_list1=[1,2,3,4,5]
print("Sum of values in list=")
print(functools.reduce(addition,num_list1))

