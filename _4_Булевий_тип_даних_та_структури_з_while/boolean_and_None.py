from cgi import print_environ
from matplotlib.cbook import pts_to_midstep


print(True, type(True))

print(not True)
print(not False,'\n')

print(True or True)
print(True or False)
print(False or True)
print(False or False,'\n')

print(True and True)
print(True and False)
print(False and True)
print(False and False,'\n')

print(True or False and True)
print(False or True and True,'\n')

print(None, type(None),'\n')

s = 'sdf'
print(s is None, '\n')

print('1 < 2', 1 < 2)
print('2 <= 2', 2 <= 2)
print('1 > 2', 1 > 2)
print('1 <= 2', 1 <= 2)
print('1 == 2', 1 == 2)
print('1 != 2', 1 != 2)
print('True is False', True is False)
print('True is not 1', True is not 1, '\n')

print('1 < 2 and True', 1 < 2 and True)
print('False or 4 == 4', False or 4 == 4, '\n')

print ('2 < 4 < 5 < 10', 2 < 4 < 5 < 10)
print('2 > 4 < 5 < 10', 2 > 4 < 5 < 10, '\n')

print('2 < 4 < 5 ** 2', 2 < 4 < 5 ** 2, '\n')
