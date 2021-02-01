"""TEST 1
# dictionary : "index":"value"
dic1 = {"apple":"사과", "bird":"새", "bug":"벌레"}
print(dic1)
# dictionary function : dict(index = "value")
dic2 = dict(apple = "사과", bird = "새", bug = "벌레")
print(dic2)
"""

""" TEST 2
#initialize dic
dic = {}
dic["apple"] = "사과"
dic["grape"] = "포도"
dic["fruits"] = ["바나나", "딸기", "오렌지"]
print(dic)

#initialize dic1
dic1 = {"apple":"사과", "bird":"새", "bug":"벌레"}
print(dic1)

#delete dic1
del dic1["bug"]
print(dic1)
"""

""" TEST3 
dic = {"num":3}
dic["num"] = 4
print(dic)

dic[False] = 0
print(dic)

dic[True] = [1, 10, 100]
dic["nums"] = {"one":1, "two":2}
print(dic)

dic[True]  = 10
print(dic[True])
"""

""" Exercise1
phone = {}
phone["model"] = "iphoneXS"
phone["manufacturer"] = "apple"
phone["year"] = 2018

print(phone)

del phone["year"]

print(phone)
"""

""" TEST4 : useful functions
mem = {"김구름":25, "박에듀":23, "온라인":24}
print(mem.keys())

names = list(mem.keys())
print(names[0], names[1], names[2])

names.append("윤레벨")
print("새로운 리스트", names)
print(mem.values())
print(list(mem.values()))
print("key와 value를 튜플로", mem.items())
print(mem.get("온라인"))

exist = "온라인" in mem
print(exist)

print(mem)
mem.clear()
print(mem)
"""

""" EXERCISE2 """
D = {'A':1, 'B':2}
D['C'] = 3
print(D)

del D['C']
print(D)