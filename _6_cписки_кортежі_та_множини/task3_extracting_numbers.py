"""
Make a list that contains all integers from 1 to 100, then find all integers 
from the list that are divisible by 7 but not a multiple of 5, and store them in a separate list. 
Finally, print the list.

Constraint: use only while loop for iteration
"""

list_1_100 = list(range(1, 101))

list_results = []


i = 0
while i in range(len(list_1_100)):
    if list_1_100[i] % 7 == 0 and list_1_100[i] % 5 != 0:
        list_results.append(list_1_100[i])
        i += 1
    else:
        i += 1


print(list_results)