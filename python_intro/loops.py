# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 15:10:30 2024

@author: yasli
"""

def find_max(x, y):
    if x > y:
        print("Maximum of these two numbers is : " + str(x))
        
    else:
        print("Maximum of these two numbers is : " + str(y))

find_max(10, 20)


def factorial(x):
    result = 1
    for i in range(1, x + 1):
        result *= i
    print(f"Factorial of {x} : " + str(result))

factorial(5)
factorial(6)
factorial(7)


# find numbers less than 100
def lessThanHundred(x):
    for i in x:
        if(i < 100):
            print(str(i), end = " ")
        else:
            continue


def lessThanHundred_(x):
    x.sort()
    
    for i in x:
        if(i < 100):
            print(str(i), end = " ")
        else:
            break

list1 = [290, 34, 21, 345, 1000, 2, 10, 99, 100]
lessThanHundred_(list1)
print()
lessThanHundred(list1)


def powersLessThan(num, limit):
    power = 0
    temp = 1
    while temp < limit:
        print(f"{power}. power of {num} = " + str(temp))
        temp = temp * num
        power += 1
    print(f"((({power}. power of {num} is not less than {limit} => " + str(temp) + ")))")

powersLessThan(2, 100)
powersLessThan(3, 1000)
powersLessThan(4, 10000)
powersLessThan(5, 100000)
