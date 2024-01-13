# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 19:51:48 2024

@author: yasli
"""

class DataScientist():
    employees = []
    def __init__(self):
        self.major = ""
        self.languages_known = []
    def add_languages(self, new_language):
        self.languages_known.append(new_language)


#instantiation
person1 = DataScientist()
person1.languages_known.append("Python")
person2 = DataScientist()
person2.languages_known.append("C++")
print(person1.languages_known)
print(person2.languages_known)

person1.add_languages("Java")
person2.add_languages("Javascript")
print(person1.languages_known)
print(person2.languages_known)



#inheritance
class Employees():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


class DataScience(Employees):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        #self.programming = ""


class Marketing(Employees):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        #self.email_marketing = ""

employee1 = DataScience("Corrina Shonda", "Moors")
employee2 = Marketing("Cyril Davin", "Taft")




#Anonymous Functions
unsorted_list = [("b", 3), ("a",2),("c",10),("e",7)]
print(sorted(unsorted_list, key = lambda x : x[0]))
print(sorted(unsorted_list, key = lambda x : x[1]))


#Vector Operations

# OOP
list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
list1xlist2 = []

for i in range(0, len(list1)):
    list1xlist2.append(list1[i] * list2[i])
print(list1xlist2)


#Functional Programming
import numpy as np
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])
print(arr1 * arr2)



#map
list1 = [1, 2, 3, 4, 5]
print(list(map(lambda x : x**2, list1)))

#filter
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(filter(lambda x : x % 2 == 0, list1)))

#reduce
from functools import reduce
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(reduce(lambda a,b : a + b, list1))
