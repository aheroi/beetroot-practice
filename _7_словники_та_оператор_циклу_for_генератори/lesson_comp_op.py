import numbers
import random

# Plain list creation and filling

random_numbers = []

for _ in range(10):
    random_numbers.append(random.randint(1, 100))

print(random_numbers)

# List comprehechensions
numbers = [x**x for x in [2, 4, 3, 5]]
random_numbers = [random.randint(1, 100) for _ in range(10)]
random_even_numbers = [random.randint(1, 100) for i in range(10) if i % 2 == 0]
print(random_numbers)
print(random_even_numbers)
print(numbers)

# Plain dict creation
data = [('name', 'sergiy'), ('age', 18)]
user = {}

for col_name, col_value in data:
    user[col_name] = col_value
print(user)
# Dict comprehencions
user = {col_name: col_value for col_name, col_value in data}

print(user)
