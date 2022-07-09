from re import L


a_list = [1, 2, 3, 4, 5]

i = 0
while i < len(a_list):
    print(a_list[i])
    i += 1


for item in a_list:
    print(item)


for ind, item in enumerate(a_list):
    print(ind, item)

for i in range(len(a_list)):
    print(a_list[i])

for item in a_list:
    if item == 2:
        continue
    print(item)

for item in a_list:
    if item == 10:
        break
    print(item)
else:
    print('ok')