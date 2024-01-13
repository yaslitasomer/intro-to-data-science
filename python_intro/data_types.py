# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 21:16:13 2024

@author: yasli
"""

# LISTS 
list1 = [10, 10.5, "pie"]
list2 = [20, 20.5, "apple pie"]
list3 = [list1, list2]
print(list3)
print(list3[0][2])
print(list3[1][2])
print(list3[0])
del list1, list2, list3


list1 = [0, 2, 3, 4, 5]
list1[0] = 1
list1[1:] = [3, 5, 7, 9]
print(list1)
list1 = list1 + [11]
print(list1)
del list1[0]
print(list1)
del list1


list1 = []
list1.append(1)
print(list1)
list1.remove(1)
print(list1)
del list1

list1 = [0, 1, 2, 4, 5, 6]
list1.insert(3, 3)
list1.insert(len(list1), 7)
list1.pop(0)
print(list1)
del list1


list1 = [1, 2, 3, 4, 5, 2, 3, 2]
print(list1.count(2))
list2 = list1.copy()
list2[0] = 0
print(list1)
print(list2)
list2.extend([0])
print(list2)
print(list2.index(4))
del list1, list2

list1 = [1, 2, 3]
list1.reverse()
print(list1)
list1.sort()
print(list1)
list1.clear()
print(list1)
del list1



# TUPLES
t1 = (1, 2, "reverse", [1, 2, 3])
t2 = 1, 2, "reverse", [1, 2, 3]
print(t1, t2, sep="\n")
del t1, t2

t1 = ("reverse")
print(type(t1))

t1 = ("reverse", )
print(type(t1))
del t1
dir(tuple)

# tuple object does not support item assignment
# t1[0] = 0



# DICTIONARY
dict1 = {"REG" : {"RMSE" : 10},
         "LOG" : "Logistic Regression",
         "CART": "Classification and Regression"}

print(dict1)
print(dict1["REG"]["RMSE"])

dict1["GBM"] = "Gradient Boosting Mac"

dict1[1] = "Integers can be key values"
dict1[1.1] = "Floats can be key values"
t = (1, 2, "reverse")
dict1[t] = "Tuples can be key values"
del t

# Lists cannot be key values
l = [1, 2]
# dict1[l] = "unhashable type: 'list'"
del dict1
del l



# SETS 
set1 = set()
print(set1)

list1 = [1, 2]
set1 = set(list1)
print(set1)
del list1

tuple1 = ("a", 1)
set1 = set(tuple1)
print(set1)
del tuple1

msg = "set_assignment"
set1 = set(msg)
print(set1)
del msg

set1 = set()
set1.add(1)
set1.add(1) # no error
set1.add(2)
set1.add(3)
set1.remove(3)

# error
#set1.remove(3) 

set1.discard(3) # no error
print(set1)


set1 = set([1, 2, 3])
set2 = set([3, 4, 5])

print(set1.difference(set2))
print(set1 - set2)

print(set1.intersection(set2))
print( set1 & set2)

print(set1.union(set2))
print(set1.symmetric_difference(set2))


set2 = set([1, 2, 3, 4, 5])
print(set1.isdisjoint(set2))
print(set1.issubset(set2))
del set1, set2

# FUNCTIONS

def square(x):
    print(f"Square of {x} : " + str(x**2))

def multiply(x = 1, y = 1):
    return x * y

square(55)
print(multiply(2, 3))