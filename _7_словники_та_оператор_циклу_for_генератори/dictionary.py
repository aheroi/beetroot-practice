from numpy import empty


country = {
    'name': 'Sweden',
    'capital': 'Stokholm',
    'largest_cities': ['Stokholm', 'Gothenberg', 'Malmo']
    }
# empty_dict = {}
# empty_set = set()

print(country['name'])

country.update({'population': 10_000_000, 'language': 'Swedish'})


# print(country['population'])

for key, value in country.items():
    print(key, ':', value)