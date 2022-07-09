"""
Write a program that generates a random number between 1 and 10 and lets the user guess 
what number was generated. The result should be sent back to the user via a print statement.
"""
from random import randint

comp_number = randint(1, 10)


while True:
    user_input = input('print your choose from 1 to 10 or q to quit: ')
    if user_input.lower() == 'q':
        break
    elif int(user_input) == comp_number:
        print(f'{comp_number} is correct.')
        break
    else:
        print('Try again.')
        