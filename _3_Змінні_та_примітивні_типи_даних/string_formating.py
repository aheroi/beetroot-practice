from operator import le
from pyparsing import matchOnlyAtCol
import math


a = 3
b = 5
print(f'{a * b} not equales {3 ** 5}')

name = 'ManCat'
super_power = 'brain'
enemy = 'DogMan'
print(f'Superhero is {name}. His superpower is {super_power.title()}. And he has an enemy {enemy[:(len(enemy) -1)]}.')

s = 'Superhero is {}. His superpower is {}.'
print(s.format(name, super_power))


print('Superhero is {1}. His superpower is {0}. {1}\'s enemy is {2}.'.format(super_power.upper(), name.upper(), enemy.capitalize()))
print('Superhero is %s. His superpower is %s. His enemy is %s.' % (name.upper(), super_power.upper(), 
            enemy[:(len(enemy) -1)].capitalize()))

print('this number is %d' % 3.134567890)
print('this nuber is %f' % 3.12345678)
print('this number is %.2f' % 3.12234567)


address_book = [{'name':'N.X.', 'addr':'15 Jones St', 'bonus': 70},
    {'name':'J.P.', 'addr':'1005 5th St', 'bonus': 400},
    {'name':'A.A.', 'addr':'200001 Bdwy', 'bonus': 5},]

for person in address_book:
    print(f'{person["name"]:8} || {person["addr"]:20} || {person["bonus"]:>5}')
# N.X.     || 15 Jones St          ||    70
# J.P.     || 1005 5th St          ||   400
# A.A.     || 200001 Bdwy          ||     5

text = (
    '%d litle pigs come out, '
    'or I\'ll %s, and I\'ll %s, '
    'and I\'ll blow your %s down.'
    % (3, 'huff', 'puff', 'house')
)
print(text)

# Strings (Unicode vs bytes)
ustring = 'A unicode \u018e string \xf1'
b = ustring.encode('utf-8')
print(b)
# b'A unicode \xc6\x8e string \xc3\xb1'         ## bytes of utf-8 encoding. Note the b-prefix.
t = b.decode('utf-8')                           ## Convert bytes back to a unicode string
print(t == ustring)                             ## It's the same as the original, yay!


print(math.exp(2))

a = ['q', 'W', 4, 'Tr']
for count, value in enumerate(a):
    print(count, value)

