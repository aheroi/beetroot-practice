"""
Write a password guessing program to keep track of how many times the user has entered the password wrong. If it is more than 3 times, print You have been denied access. and terminate the program. If the password is correct,
 print You have successfully logged in. and terminate the program.
"""
from re import T


attempt = 0
attempts = 3
password = 'qwerty'

## 1
# while attempts:
#     get_password = input('Enter password: ')
#     if get_password == password:
#         print('the password is correct')
#         break
#     else:
#         for attempt in range(attempts):
#             get_password = input('Enter password: ')
#             attempt += 1
#             continue
#         else:
#             print('access denied')
#             break

## 2
while attempt < attempts:
    get_password = input('Enter password: ')
    attempt += 1
    if get_password == password:
        print('You have successfully logged in')
        break
else:
    print('You have been denied access')


## 3
# while True:
#     get_password = input('Enter passord:  ')
#     attempt += 1
#     if get_password == password:
#         print('You have successfully logged in.')
#         break
#     else:
#         if attempt > attempts:
#             print('You have been denied access')
#             break
 