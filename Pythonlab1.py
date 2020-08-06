Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> num_i = 123
>>> num_f = 1.23
>>> num_n = num_i + num_f
>>> print("datatype of num_i:",type(num_i))
datatype of num_i: <class 'int'>
>>> print("data type of num_f:",type(num_f))
data type of num_f: <class 'float'>
>>> print("Value of num_n:",num_n)
Value of num_n: 124.23
>>> print("datatype of num_n:",type(num_n))
datatype of num_n: <class 'float'>
>>> #Addition of string and integer
>>> num_int = 123
>>> num_str = "456"
>>> print("Data type of num_int:",type(num_int))
Data type of num_int: <class 'int'>
>>> print("Data type of num_str:",type(num_str))
Data type of num_str: <class 'str'>
>>> print(num_int+num_str)

Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    print(num_int+num_str)
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> #Addition of string and integer using explicit conversion
>>> 
KeyboardInterrupt
>>> num_int = 123
>>> num_str = "456"
>>> print("Data type of num_int:",type(num_int))
Data type of num_int: <class 'int'>
>>> print("Data type of num_str before Type Casting:",type(num_str))
Data type of num_str before Type Casting: <class 'str'>
>>> num_str = int(num_str)
>>> print("Data type of num_str after Type Casting:",type(num_str))
Data type of num_str after Type Casting: <class 'int'>
>>> num_sum = num_int + num_str
>>> print("Sum of num_int and num_str:",num_sum)
Sum of num_int and num_str: 579
>>> print("Data type of the sum:",type(num_sum))

Data type of the sum: <class 'int'>
>>> # 1
>>> a = 5
>>> print(a, "is of type", type(a)) 

5 is of type <class 'int'>
>>> # 2
>>> a = 2.0
>>> print(a, "is of type", type(a))
2.0 is of type <class 'float'>
>>> # 3
>>> a= 1+2j
>>> print(a, "is complex number?", isinstance(1+2j,complex))

(1+2j) is complex number? True
>>> # 4
>>> s = "This is a string"
>>> print(s)
This is a string
>>> # 5
>>> s = '''A multiline string''' 

>>> print(s)

A multiline string
>>> # 6
>>> a = [1, 2.2, 'python']
>>> print(a)
[1, 2.2, 'python']
>>> # 7
>>> a = [5,10,15,20,25,30,35,40]
>>> # a[2] = 15
>>> print("a[2] = ", a[2])
a[2] =  15
>>> # a[0:3] = [5, 10, 15]
>>> print("a[0:3] = ", a[0:3])
a[0:3] =  [5, 10, 15]
>>> # a[5:] = [30, 35, 40]
>>> print("a[5:] = ", a[5:])
a[5:] =  [30, 35, 40]
>>> # 8
>>> t = (5,'program', 1+3j)
>>> print(t)
(5, 'program', (1+3j))
>>> # t[1] = 'program'
>>> print("t[1] = ", t[1])
t[1] =  program
>>> # t[0:3] = (5, 'program', (1+3j))
>>> print("t[0:3] = ", t[0:3])
t[0:3] =  (5, 'program', (1+3j))
>>> # 9
>>> a = {5,2,3,1,4}
>>> # printing set variable
>>> print("a = ", a)
a =  {1, 2, 3, 4, 5}
>>> # data type of variable a
>>> print(type(a))
<class 'set'>
>>> # 10
>>> a = {1,2,2,3,3,3}
>>> print(a)
{1, 2, 3}
>>> a = {1,2,3}
>>> a[1]
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    a[1]
TypeError: 'set' object is not subscriptable
>>> # 11
>>> d = {1:'value','key':2}
>>>  type(d)
 
SyntaxError: unexpected indent
>>> type(d)
<class 'dict'>
>>> # 12
>>> d = {1:'value','key':2}
>>> print(type(d))
<class 'dict'>
>>> print("d[1] = ", d[1]);
d[1] =  value
>>> print("d['key'] = ", d['key']);
d['key'] =  2
>>> # Generates error
>>> print("d[2] = ", d[2]);
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    print("d[2] = ", d[2]);
KeyError: 2
>>> # 13
>>> float(5)
5.0
>>> int(10.6)
10
>>> int(-10.6)
-10
>>> float('2.5')
2.5
>>> str(25)
'25'
>>> int('1p')
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    int('1p')
ValueError: invalid literal for int() with base 10: '1p'
>>>  set([1,2,3])
 
SyntaxError: unexpected indent
>>> set([1,2,3])
{1, 2, 3}
>>> tuple({5,6,7})
(5, 6, 7)
>>> list('hello')
['h', 'e', 'l', 'l', 'o']
>>> dict([[1,2],[3,4]])
{1: 2, 3: 4}
>>> dict([(3,26),(4,44)])
{3: 26, 4: 44}
>>> # 14
>>> datatype of num_n: <class 'float'>
SyntaxError: invalid syntax
>>> 