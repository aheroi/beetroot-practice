"""
Write a Python program to get the largest number from a list of random numbers with the length of 10

Constraints: use only while loop and random module to generate numbers
"""
from random import randint

length_list_random = 10
list_random = [randint(-100, 100) for i in range(length_list_random)]
i = 0
max_number = list_random[0]

while i in range(length_list_random):    
    if max_number < list_random[i]:
        max_number = list_random[i]
        i += 1
    else:
        i += 1
print(max_number)

# print(max(list_random)) 