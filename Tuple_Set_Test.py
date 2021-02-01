"""TEST 1 : Tuple (immutable List) """
t1 = ('a', 'b', 'c', 1, 2, 3)
print(t1, t1[2])

t2 = ("hello",)
print(t2)

t3 = "jaehoon", 'b', "hello", 1, 2, 3
print(t3, t3[2])

s1 = list(set([1,2,3]))
t4 = ([1,2,3], {"사과":"apple", "포도":"grape"}, s1)
print(t4, t4[2])

t4[1]["사과"] = "edit"
t4[0][2] = "edit"
print(t4)