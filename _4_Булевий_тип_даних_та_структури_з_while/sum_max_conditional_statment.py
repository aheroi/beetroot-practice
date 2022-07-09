"""
Write a program that asks for two numbers. If the sum of the numbers is greater than 100,
 print That is a big number and terminate the program.
"""
max_sum = 100

while True:
    number_1 = float(input('Enter number 1: '))
    number_2 = float(input('Enter number 2: '))
    if number_1 + number_2 > 100:
        print(number_1 + number_2)
        break
