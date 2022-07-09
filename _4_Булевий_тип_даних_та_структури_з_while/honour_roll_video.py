
gpa = float(input('What was your Grade Point Average? '))
lowest_grade = float(input('Wha was your lowest grade? '))
 
# first options via AND
print('\n# first options via AND')
if gpa >= .85 and lowest_grade >= .70:
    print('You made honour roll')



# option via TRUE
print('\n# option via TRUE')

honour_roll = gpa >= .85 and lowest_grade >= .70

if honour_roll:
    print('You made honour roll')



# option via TRUE_2
print('\n# option via TRUE_2')

if gpa >= .85 and lowest_grade >= .70:
    honour_roll = True
else:
    honour_roll = False

if honour_roll:
    print('You made honour roll')

