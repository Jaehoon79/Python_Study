#TEST 1 : String Test
#str1 = 'He said "I love you"'
#str2 = "It's so beautiful"
#str3 = """My name is \n "Hoon" """
#str4 = '''It's apple'''
"""
print(str1)
print(str2)
print(str3)
print(str4)
"""

# TEST 2 : String Test 2
#str_test1 = """'비구름'이 말했습니다. \n"""
#str_test2 = '''\t"비가 내리면 먼지가 사라질거야."'''
#print(str_test1 + str_test2)

""" TEST 3
print (ord("A"))
print (chr(65))

str = "apple!"
str_sum = str[3] + str[4] + str[5]
print ("str 1st character is ", str[0], "4th character is ", str[3])
print (str_sum)
"""

""" TEST 4 : String Inverse Indexing 
a = "Hello World!"

b = a[-1] + a[-2] + a[-3]
c = a[-0]

print (b)
print (c)
"""

""" TEST 5 : String Slicing
str_val = "Hello World!"
str_slc1 = str_val [0:5]
str_slc2 = str_val [:5]
str_slc3 = str_val [5:]

str_slc4 = str_val[0:-5]
str_slc5 = str_val[6:-11]
print (str_slc1)
print (str_slc2)
print (str_slc3)

print (str_slc4)
print (str_slc5)
"""

""" TEST 6 : String Formating
city = "seoul"
today = 12
day = "화요일"
temperature = 26

#way 1
announcement = city + "의 " + str(today) + "일 " + day + " 기온은 " + str(temperature) + " 도 입니다."
print(announcement)

#way 2
print(city, "의", today, "일", day, "기온은", temperature, "도 입니다.")

#way 3
announcement = "%s의 %d일 %s 기온은 %d도 입니다." %(city, today, day, temperature)
print ("%s의 %d일 %s 기온은 %d도 입니다." %(city, today, day, temperature))
print (announcement)
"""

""" TEST 7:
name_str = "kimc"
age_int = 43
height_float = 184.5
print ("my age is %d" %age_int)
print ("my name is {2}. and my age is {1} and height is {0}cm".format(height_float, age_int, name_str))

print("{length: > 10d}".format(length = 30))
# f-string is supported from python v3.6
print (f"my name is {name_str} and my age is {age_int+10} and height is {height_float}cm.")
"""

""" TEST 8 : useful string function """
str = " Hello World! I study Python.  "

num = str.count(' ') # the number of white_space
print ("The number of white_space is %d." %num)
print ("The number of white_space is {0}".format(num))
print (f"The numver of white_space is {num}.")

f_index = str.find('l')
print ("The index of 1st l character is %d." %f_index)
print ("The index of 1st l character is {0}.".format(f_index))
print (f"The index of 1st l character is {f_index}.")


print (' '.join(str))
print (str.upper())
print (str.lower())
print (str.lstrip())
print (str.rstrip())
print (str.replace('Python', 'c'))
print (str.split())

sentence = "I like studying Python"
print (len(sentence), len(str))