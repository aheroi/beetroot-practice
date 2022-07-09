"""
The greeting program.

Make a program that has your name and the current day of the week stored as separate variables and then prints a message like this:

     "Good day <name>! <day> is a perfect day to learn some python."
Note that  <name> and <day> are predefined variables in source code.

An additional bonus will be to use different string formatting methods for constructing result string.
"""
import datetime


my_name = 'andriy'
current_data = datetime.datetime.now().strftime("%A %d %B")

print(f'Good day {my_name.title()}! {current_data} is a perfect day to learn some python.')
print('Hi, {}! Today is {} and it\'s a great day to learn something new)))'.format(my_name.title(), current_data))
print('Today is {1}. Hi, {0}! It\'s a great day to learn something new)))'.format(my_name.title(), current_data))
