
a_dict = {'key': 'hello', 'key1': 'Hello'}

for key in a_dict:
    print(a_dict[key])


for value in a_dict.values():
    print(value)

for key, value in a_dict.items():
    print(key, value)

# {x: x**2 for x in (2, 4, 6)} -> # {2: 4, 4: 16, 6: 36}


# dict(sape=4139, guido=4127, jack=4098) -> {'sape': 4139, 'guido': 4127, 'jack': 4098}