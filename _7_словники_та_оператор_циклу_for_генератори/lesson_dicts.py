# non-changable types:
# bool (True, False), None, int, float, str, tuple, 'class'
from unicodedata import name


a_bool_dict = {
    True: 'This is True',
    False: 'This is False'
}

a_tuple_dict = {
    (0, 1):'(0, 1)',
    (0, 2): '(0, 2)',
}

a_dict = {
    'name':'sergiy',
    'age': 18,
}

print(a_bool_dict[False])
print(a_tuple_dict[(0, 2)])
print(a_dict['name'])
print(list(a_bool_dict)) # list of keys