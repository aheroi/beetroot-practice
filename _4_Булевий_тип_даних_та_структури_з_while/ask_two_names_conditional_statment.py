"""
Write a program that asks the user their name. If they enter your name, say "That is a nice name."
If they enter "John Cleese" or "Michael Palin", tell them how you feel about them ;),
 otherwise tell them "You have a nice name."
"""

my_name = 'andy'
list_of_favorite_names = ['john cleese', 'michael palin']

print('Enter q to quit')

while True:
    name = input('Enter your name:  ')
    if name.lower() == 'q':
        break
    elif name.lower() == my_name:
        print("That is a nice name.")
    elif name.lower() in list_of_favorite_names:
        print(f'Ooo, {name.title()} my favourite name.')
    else:
        print('You have a nice name.')
