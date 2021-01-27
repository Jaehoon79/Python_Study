""" TEST1
test1 = input("Please enter your age:")
print(test1)
"""
""" TEST2
int_num = int(input("Please enter integer num:"))
float_num = float(input("Please enter float num:"))
print("sum is", int_num + float_num)
print(type(int_num))
print(type(int_num + float_num))
"""

""" TEST3
a = 10
b = -2.5
c = 1 + 2j
d = 0xDA

print(a, type(a))
print(b, type(b))
print(c, c.real, c.imag, c.conjugate,  type(c))
print(d, type(d))

print(a+b, type(a+b))
print(c+d, type(c+d))
"""

""" TEST4 
int_num = int(input("enter your int number:"))
int_float = float(input("enter your float number:"))
print(int_num, int_float, type(int_num + int_float))
"""

""" TEST5
a = True

if (a):
    print("True")
else:
    print("False")
"""
""" TEST6
a = "Hello World"
if (a):
    print("True")
else:
    print("False")

b = ""
if (b):
    print("True")
else:
    print("False")
"""

""" TEST7
str_val1 = "Hello"
str_val2 = " World"
print (str_val1 + str_val2)
"""

""" TEST 8
a = 10
b = 3
c = 1.5

print ("A + B = ", a+b)
print ("A - B = ", a-b)
"""

""" TEST 9
a = True
b = False

print ("true and false : ", a and b)
print ("true and true : ", a and a)
print ("true or false : ", a or b)
print ("false or false : ", b or b)
print ("not true : ", not a)
"""
""" TEST 10
print ("100 == 100 :", 100 == 100)
print ("100 == 200 :", 100 == 200)
"""
# Last Test
a = 0b10110
b = 0b10011
print(a,b)
print(a&b)