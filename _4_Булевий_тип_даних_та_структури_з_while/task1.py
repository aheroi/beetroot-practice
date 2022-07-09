"""
String manipulation
Write a Python program to get a string made of the first 2 and the last 2 chars from a given string. 
If the string length is less than 2, return instead of the empty string.
Sample String: 'helloworld'
Expected Result : 'held'
Sample String: 'my'
Expected Result : 'mymy'
Sample String: 'x'
Expected Result: Empty String
"""



print('press \'q\' to quit')

while True:
    get_str = str(input('\nEnter string:  '))
    len_get_str = len(get_str)
    
    if get_str.lower() == 'q':
        break
    elif len_get_str < 2:
        print('Empty String')
    elif len_get_str == 2:
        print(get_str * 2)
    else:
        print(get_str[:2] + get_str[-2:])
