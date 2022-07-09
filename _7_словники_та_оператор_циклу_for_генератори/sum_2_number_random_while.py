from ast import While
from random import randint

points = 0
while True:
    x = randint(0, 10)
    y = randint(0, 10)
    # print('points: ' + str(points))
    print(f'points: {points}')
    answer = input(f'{x} + {y} = ? (type q to quit):  ')
    if answer == 'q':
        break
    elif int(answer) != x + y:
        print('You have 0 points')
        continue
    points += 10
    print(f'You are right')
        

