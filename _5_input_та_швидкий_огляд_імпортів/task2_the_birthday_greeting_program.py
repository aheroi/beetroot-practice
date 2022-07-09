"""
Write a program that takes your name as input, and then your age as input and 
greets you with the following:

“Hello <name>, on your next birthday you will be <age+1> years”  
"""

input_name = input('Enter your name:  ')
input_age = int(input('\nEnter your age:  '))

print(f'Hell {input_name.title()}, on your next birthday you will be {input_age + 1}.')
