"""
Example #1: Suppose we want to create an output list which contains only the even numbers
 which are present in the input list. Let s
see how to do this using for loops and list comprehension and decide which method suits better.
"""

# Constructing output list WITHOUT
# Using List comprehensions
input_list = [1, 2, 3, 4, 4, 5, 6, 7, 7]

output_list = []

# Using loop for constructing output list
for var in input_list:
	if var % 2 == 0:
		output_list.append(var)

print("Output List using for loop:", output_list)


# Using List comprehensions
# for constructing output list

input_list = [1, 2, 3, 4, 4, 5, 6, 7, 7]


list_using_comp = [var for var in input_list if var % 2 == 0]

print("Output List using list comprehensions:",
							list_using_comp)
