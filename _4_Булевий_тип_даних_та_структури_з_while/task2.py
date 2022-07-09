"""
The valid phone number program.
Make a program that checks if a string is in the right format for a phone number. 
The program should check that the string contains only numerical characters and is only 10 characters long.
 Print a suitable message depending on the outcome of the string evaluation.
"""


from operator import le
from queue import PriorityQueue

list_of_phone_numbers = [
                        '0675706091',
                        '80675706092',
                        '06757O6093',
                        '0675706094',
                        '306757O6095',
                        '0675706096',
                        '0675706097',
                        '0675706098',
                        '0675706099',
                        '0675706100',
                        '0675706101',
                        '+06757O6102',                         
                        ]
len_of_number = 10

msg_numeric_format = 'type_mistake: not all characters in a string are integers (0 to 9)'
msg_len_of_number = 'len_mistake: phone number long is not 10 charackters'
msg_of_correct = 'phone number is correct'

for number in list_of_phone_numbers:
    if len(number) == len_of_number and number.isnumeric():
        print(number, ':', msg_of_correct)
    else:
        if len(number) != len_of_number:            
            print(number, ':', msg_len_of_number)
# use if instead elif because one phone number can contain two type of mistake 
        if not number.isnumeric():
            print(number, ':', msg_numeric_format)
