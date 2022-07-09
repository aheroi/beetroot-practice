our_threshold = 5
i = 1

while i < our_threshold:
    print('Do important logic here')
    i += 1


our_threshold = 5
i = 10
while i < our_threshold:
    print('Do important logic here')
    i += 1

# break
our_threshold = 100
i = 0
print('\n# break:')
while i < our_threshold:
    print(f'Variable i: {i}.', end=' ')
    print('Do important logic here')
    i += 1
    if i % 7 == 0:
        print('good reason to stop')
        break 

# continue
our_threshold = 13
i = 0
print('\n# continue:')
while i < our_threshold:
    print(f'Variable i: {i}.', end=' ')
    if i % 7 == 0:
        print('Do very very important task and that\'s it')
        i += 1
        continue

    print('Do important logic here')
    i += 1

# while_else. Some times it's important to know that your  while loop had break took place or vice versa 
our_threshold = 7
i = 0
print('\n# while_else:')
while i <= our_threshold:
    print(f'Variable i: {i}.', end=' ')
    print('Do important logic here')
    i += 1
    if i % 7 == 0:
        print('Something went wrong')
        break
else:
    print('The important logic will take place only if nothing broken')
    