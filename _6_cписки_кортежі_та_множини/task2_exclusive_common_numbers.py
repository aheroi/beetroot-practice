"""
Generate 2 lists with the length of 10 with random integers from 1 to 10, 
and make a third list containing the common integers between the 2 initial lists without 
any duplicates.

Constraints: use only while loop and random module to generate numbers
"""

from random import randint




length_list = 6
list_1 = [randint(1, 10) for i in range(length_list)]
list_2 = [randint(1, 10) for i in range(length_list)]


# 1 check x in both lists without while
print([x for x in set(list_1) and set(list_2) if x in list_1 and x in list_2])    # add set to eliminate duplicates


## 2 with while
set_results = set()                     # create set to takes unic numbers
i=0                                     # first index for loop
while i in range(length_list):
    if list_1[i] in list_2:             # check elements from list_1
        set_results.add(list_1[i])      # if True add in set
        i += 1 
    else:
        i += 1

list_results = list(set_results)        # convert set results into list
        
print(list_results)

