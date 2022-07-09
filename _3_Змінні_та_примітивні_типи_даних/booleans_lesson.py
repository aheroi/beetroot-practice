# boolean values:
a_true = True
a_false = False

# NOT
# not True = False
# not False = True

# AND
# True and True => True
# True and False => False
# False and True => False
# False and False => False


a = 12
b = 13
if a > b:
    sum = 2 + 2
    print('This is a True')
    print('2 + 2 = ', sum)
else:
    print('Not good at all ...')

age = 60
if age < 21 or age > 30:
    print('You\'re not allowed here')
else:
    print('You\'re lucky')

if age > 21 and age < 30:
    print('You\'re not allowed here')
else:
    print('You\'re lucky')

if 21 < (age < 30):                     # first check age < 30
    print('You\'re not allowed here')
else:
    print('You\'re lucky')

if (age > 21 and age < 30) or age == 60:        # check first part (age > 21 and age < 30) or second part age == 60
    print('You\'re not allowed here')
else:
    print('You\'re lucky')

# assignation variables
age_between_21_and_30 = age > 21 and age < 30
age_is_60 = age == 60

if age_between_21_and_30 or age_is_60:        
    print('You\'re not allowed here')
else:
    print('You\'re lucky')

# NOT    

if not (age_between_21_and_30 or age_is_60):        
    print('You\'re lucky')
else:
    print('You\'re not allowed here')    