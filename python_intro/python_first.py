# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 13:25:30 2024

@author: yasli
"""

# Types 
print(type(3))
print(type(3.3))
print(type("Hello"))
print(type(False))
print(type('a'))
print(type(1 + 2j))


# Strings 
print("a" + "b")
print("a" "b")
print("a " * 3)

# String Methods 
msg = "ReveRse"
print(len(msg))
print(msg.isupper())
print(msg.lower().islower())


print(msg)
msg = msg.replace("R", "r")
print(msg)
del msg

msg = " reverse       "
print(msg.strip() + "24")

msg = "*reverse**"
print(msg.strip("*"))
del msg

# see methods
print("\nString:")
print(dir(str)) 
print("\nFloat:")
print(dir(float))
print("\nFloatingPointError:")
print(dir(FloatingPointError))
print("\nInteger:")
print(dir(int))

# # casting
# num1 = int(input())
# num2 = input()
# print(num1 + num1)
# print(num2 + num2)
# del num1, num2


# print()
print("print", "function")
print("print", "function", sep = "**")
print("print", "function", "examples", sep = "_")
#?print
print("print", "function", end = "...")