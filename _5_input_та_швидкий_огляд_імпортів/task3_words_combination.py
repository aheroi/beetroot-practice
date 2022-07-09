"""
Create a program that reads an input string and then creates and prints 5 random strings
 from characters of the input string.

For example, the program obtained the word 'hello', so it should print 5 random strings(words)
that combine characters 

'h', 'e', 'l', 'l', 'o' -> 'hlelo', 'olelh', 'loleh' …
"""

import random

input_word = input('Print your choise:  ')
number_of_repetitions = 5

for i in range(number_of_repetitions):
    print(''.join(random.sample(input_word, k=len(input_word))))
