# Introduction
# Day 1 - 30DaysOfPython Challenge

# Exercises

# Check the python version you are using
# Open the python interactive shell and do the following operations. The operands are 3 and 4.
from cmath import sqrt


print(4 + 3)
print(4 - 3)
print(4 * 3)
print(4 / 3)
print(4 ** 3)
print(4 % 3)
print(4 // 3)


# Write strings on the python interactive shell. The strings are the following:
name = 'jiwoo'
family_name = 'choi'
country = 'korea'
print(name)
print(family_name)
print(country)


# Check the data types of the following data:
print(type(10))
print(type(9.8))
print(type(3.14))
print(type(4 - 4j))
print(type('Jiwoo'))
print(type([1, 2, 3]))
print(type({'name':'Jiwoo'})) 
print(type({9.8, 3.14, 2.7})) 
print(type((9.8, 3.14, 2.7))) 

print({9.8, 3.14, 2.7, 2.7})
# set는 중복값X


# Exercise: Level 3
# Write an example for different Python data types such as Number(Integer, Float, Complex), String, Boolean, List, Tuple, Set and Dictionary.
# Find an Euclidian distance between (2, 3) and (10, 8)
x = (10 - 2) ** 2 
y = (8 - 3) ** 2
value = sqrt(x+y)
print(value)