# 1.Converting integer to float
num_int = 123
num_flo = 1.23
num_new = num_int + num_flo 
print("datatype of num_int:",type(num_int)) 
print("datatype of num_flo:",type(num_flo)) 
print("Value of num_new:",num_new) 
print("datatype of num_new:",type(num_new))



# 2.Addition of string and integer using explicit conversion
num_int = 123 
num_str = "456"
print("Data type of num_int:",type(num_int)) 
print("Data type of num_str before Type Casting:",type(num_str)) 
num_str = int(num_str) 
print("Data type of num_str after Type Casting:",type(num_str)) 
num_sum = num_int + num_str 
print("Sum of num_int and num_str:",num_sum) 
print("Data type of the sum:",type(num_sum))



# 3
a = 5 
print(a, "is of type", type(a))



# 4
a = 2.0 
print(a, "is of type", type(a))



# 5
a= 1+2j
print(a, "is complex number?", isinstance(1+2j,complex))



# 6
s = "This is a string" 
print(s) 
s = '''A multiline string''' 
print(s)



# 7
a = [1, 2.2, 'python']
print(a)



# 8
a = [5,10,15,20,25,30,35,40] 
# a[2] = 15 
print("a[2] = ", a[2]) 
# a[0:3] = [5, 10, 15] 
print("a[0:3] = ", a[0:3]) 
# a[5:] = [30, 35, 40] 
print("a[5:] = ", a[5:])



# 9
t = (5,'program', 1+3j)
print(t)



# 10
t = (5,'program', 1+3j) 
# t[1] = 'program' 
print("t[1] = ", t[1]) 
# t[0:3] = (5, 'program', (1+3j)) 
print("t[0:3] = ", t[0:3])



# 11
a = {5,2,3,1,4} 
# printing set variable 
print("a = ", a) 
# data type of variable a 
print(type(a))



# 12
a = {1,2,2,3,3,3} 
print(a)



# 13
a = {1,2,3} 
a[1]



# 14
d = {1:'value','key':2} 
type(d)



# 15
d = {1:'value','key':2} 
print(type(d)) 
print("d[1] = ", d[1]); 
print("d['key'] = ", d['key']); 
# Generates error 
print("d[2] = ", d[2]);



# 16.Addition of string data type and integer datatype
num_int = 123 
num_str = "456" 
print("Data type of num_int:",type(num_int)) 
print("Data type of num_str:",type(num_str)) 
print(num_int+num_str)
