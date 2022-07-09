# for
sevens = []

for i in range(71):
    if i % 7 == 0:
        sevens.append(i)
print(sevens)

# 
sevens_2 = []

for i in range(0, 71, 7):
    sevens_2.append(i)
print(sevens_2)

# while
sevens_3 = []
i = 0
while i <=70:
    sevens_3.append(i)
    i += 7
print(sevens_3)
