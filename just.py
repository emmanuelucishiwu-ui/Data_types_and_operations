# the fromkeys when u pass a string like abc your result would be none

# dict3 = dict([("name", "EM"), ("age", 20), ("course", "Python")])
# print(dict3)
# dictionary = dict3.fromkeys("name")
# print(dict3)

# print(dictionary)



# the set default automatically set EM as set default even you change it it rteturns to EM

dict3 = dict([("name", "EM"), ("age", 20), ("course", "Python")])
print(dict3)
dictionary = dict3.setdefault("name","emmanue")
print(dict3)

print(dictionary)