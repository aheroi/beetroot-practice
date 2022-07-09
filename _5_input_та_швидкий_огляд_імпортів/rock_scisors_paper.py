from random import randint

print('Let\'s play')

user = input('Choose rock, paper or scissors by typing r, p or s:  ')

if user.lower() == 'r' or user.lower() == 'p' or user.lower() == 's':
    computer = randint(1,3)
# 1 - rock
# 2 - paper
# 3 - scissors

    if user.lower() == 'r' and computer == 3 or\
        user.lower() == 'p' and computer == 1 or user.lower() == 's' and computer == 2:
        print('You\'re winner!')
        
    elif user.lower() == 'r' and computer == 1 or\
        user.lower() == 'p' and computer == 2 or user.lower() == 's' and computer == 3:
        print('It\'s draw')
        
    else: 
        print('You loose')
else:
    print('Your input was isn\'t the format, no game for you.')
