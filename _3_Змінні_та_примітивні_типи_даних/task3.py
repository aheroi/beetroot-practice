"""
Task 3
Using python as a calculator.
Make a program with 2 numbers saved in separate variables a and b, then print the result for each of the following: 
Addition
Subtraction
Division
Multiplication
Exponent (Power)
Modulus
Floor division
"""
import math

a = 9
b = 2
print('a = ', a)
print('b = ', b, end='\n\n')
print('a + b = ', a + b)
print('a - b = ', a - b)
print('a / b = ', round((a / b), 2))
print('a * b = ', a * b)
print('a ** b = ', a ** b)
print('pow a / b = ', math.pow(a, b))
print('ceil division a / b = ', math.ceil(a / b))
print('floor division a / b = ', math.floor(a / b))
print('floor division a // b = ', a // b)
print('remainder a / b = ', a % b)
print('|b - 2| = ', abs(b - 2))
