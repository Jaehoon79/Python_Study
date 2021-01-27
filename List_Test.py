""" TEST 1: List
oddnumber = [1, 3, 5, 7, 9]
cafes = ['star', 'bene', 'yoger', 'friends']
A = [1, 5, 'A', 'CC', 'B']
listInList = [[1, 3, 5, 6, 7], cafes, oddnumber, 1, 3, 'Abc']

print(oddnumber)
print(cafes)
print(A)
print(listInList)

a = oddnumber[3]
b = cafes[1]
c = A[2]
d = listInList[0][1]

print(a)
print(b)
print(c)
print(d)
print(a + d, oddnumber[4], listInList[4])
print(b + c)

a = oddnumber[1:5]
print(a)
"""

""" TEST 2
evennumber = [2, 4, 6, 8, 10]
oddnumber = [1, 3, 5, 7, 9]

numbers = evennumber + oddnumber
print (numbers)
print (numbers * 4) # 4-iterations

# python can add different variable type to list
evennumber[2] = ['a', 'b', 'c']
print (evennumber)

# slicing range make just-one array
evennumber[2:3] = ['a', 'b', 'c']
print (evennumber)
"""

""" TEST 3
#remove value in array
numbers = [2, 4, 6, 8, 10, 1, 3, 5, 7, 9]
a = "kimc"
numbers[3] = ""
print (numbers)
"""

""" TEST 4 : del function
numbers = [2, 4, 6, 8, 10, 1, 3, 5, 7, 9]
del numbers[2]
print(numbers)

del numbers [:5]
print(numbers)
"""

""" TEST 5: List Function (adding function)
#appedn(x) add new argument(x) to the end of list
#insert(x, y) add y value to Xth in list (can be added just one per one)
#extend(x) merge x with existing list (x should be list variable)
numbers = [2, 4, 6, 8, 10, 1, 3, 5, 7, 9]
print(numbers)

numbers.insert(3, [11,12,13])
print(numbers)

# differenciation BTW append and extend
numbers.extend(['a', 'b','c'])
print(numbers)
numbers.append(['a','b','c'])
print(numbers)
"""

""" TEST 6: List Function (del function)
#remove(x) : delete x at the fist x value in list
#pop() : return the end of list and delete it

numbers = [2, 4, 6, 8, 1, 3, 5, 7]
print(numbers)

numbers.insert(3, [11,12,13])
print(numbers)

numbers.remove(3)
print(numbers)
print(numbers.pop())
print(numbers)
"""

""" TEST 7: List sorting Function 
# sort(): sort function (arg is not needed)
# reverse(): revert order in list (arg is not needed)
evennumber = [2, 4, 6, 8]
oddnumber = [1, 3, 5, 7]
print(evennumber, oddnumber)

numbers = evennumber + oddnumber
print (numbers)

numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)
"""

""" TEST 8 : List information Function
# index(x): return the index of x value in list
# count(x): return the number of x value in list
# len(x): return the number of argument in x list
numbers = [1, 6, 7, 3, 5, 6, 8, 3, 3]
numbers.index(6)
print(numbers)
print(numbers.index(1))
print(numbers.count(3))
print(len(numbers))
"""

""" TEST 9 : Practice
num_list = [1, 3, 5, 8, 2, 4, 6, 7, 9, 10]
#reverse_list = [1, 3, 5, 8, 2, 4, 6, 7, 9, 10]
reverse_list = num_list # give address of num_list to reverse_list

num_list.sort() #sorting List
print(num_list)

num_list.remove(9) # del #9
print(num_list)

num_list.append(8) # add #8 at the end of list
print(num_list)

reverse_list.sort()
reverse_list.reverse()
print(reverse_list)
"""

drawer = []
drawer.append("socks")
print(drawer, drawer[0])

drawer.extend(["under-ware", "cap", "t-shirt", "pants"])
print(drawer)

drawer[3] = ""
print(drawer)

drawer[3] = "jacket"
print(drawer)