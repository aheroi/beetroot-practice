# via while operator options for mistakes
a_list = [1, 2, 3, 4, 5]
i = 0
print(a_list)
print(i)

print('# via while ')
while i < len(a_list):
    print(a_list[i])
    i += 1

# via for
print('\n# via for')
for item in a_list:
    print(item)

# enumerate
print('\n# enumerate')
for ind, item in enumerate(a_list):
    print('ind ', ind, 'item ', item)

# for and range
print('\n# for and range')
for i in range(len(a_list)):
    print(a_list[i])

# add break
print('\n# add break')
for item in a_list:
    if item == 2:
        break

    print(item)

# add continue
print('\n# add continue')
for item in a_list:
    if item == 2:
        continue

    print(item)

# for else
print('\n# for else')
for item in a_list:
    if item == 20:
        break
    print(item)
else:
    print('ok')
