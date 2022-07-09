"""
Ask the user to enter the password. If the password is correct print "You have successfully logged in" 
and exit the program. If the password is wrong print "Sorry the password is wrong" and ask the user to enter 
the password 3 times. 
If the password is wrong print "You have been denied access" and exit the program.
"""

limit_of_attempts = 3
password = 'QWERTY'
attempt = 0

print('Enter the password')

while True:
    get_rassword = input('password: ')
    attempt += 1
    if get_rassword == password:
        print('You have successfully logged in')
        break
    elif attempt < limit_of_attempts:
        print('Sorry the password is wrong')
        print(f'you have {limit_of_attempts - attempt} attempts')
    else:
        print('You have been denied access')
        break
