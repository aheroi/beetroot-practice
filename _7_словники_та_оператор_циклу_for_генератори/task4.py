"""
1 Створити лист із днями тижня.
2 В один рядок (ну або як завжди) створити словник виду: {1: “Monday”, 2:...
3 Також в один рядок або як вдасться створити зворотний словник {“Monday”: 1,
"""

# 1
list_of_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# 2
dict_of_days = {key+1: day for key, day in enumerate(list_of_days)}
print(dict_of_days)

# 3 
reverse_dict_of_days = {day:key+1 for key, day in enumerate(list_of_days)}
print(reverse_dict_of_days)