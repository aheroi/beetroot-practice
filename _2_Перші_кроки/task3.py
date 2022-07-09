"""
Task 3
Write a program, which has two print statements to print the following text 
(capital letters "O" and "H", made from "#" symbols):
#########
#       #
#       #
#       #
#########

#       #
#       #
#########
#       #
#       #

Pay attention that usage of spaces is forbidden, as well as creating the whole result 
text string using """ """, use '\n' and '\t' symbols instead.
"""
print(
    '', 9 * '#', '\n',
    '#', '\t\t', '#', '\n',
    '#', '\t\t', '#', '\n',
    '#', '\t\t', '#', '\n',
    9 * '#', end='\n\n'
    )
print(
    '', '#', '\t\t', '#', '\n',
    '#', '\t\t', '#', '\n',
    9 * '#', '\n',
    '#', '\t\t', '#', '\n',
    '#', '\t\t', '#', '\n'
    )
