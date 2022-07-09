from matplotlib.pyplot import table
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt


print('Welcome to the Contacts V1.0')

# contact should contain name, email, phone, address (optional) and notes (optional)
# contacts = [
#     ('Cassandra Burton', 'cassandra.burton@example.com', '(629) 326-8652', None, None),
#     ('Janice Thoas', 'janice.thomas@example.com', '(272) 569-4415', '2745 Thornridge Cir', None),
#     ('Cassandra Burton', 'cassandra.burton@example.com', '(629) 326-8652', None, None),
#     ('Janic Thomas', 'janice.thomas@example.com', '(272) 569-4415', '2745 Thornridge Cir', None),
#     ('Jance Thomass', 'janice.thomas@example.com', '(272) 569-4415', '2745 Thornridge Cir', None),
#     ]

contacts = [
    ('Cassandra Burton', 'cassandra.burton@example.com', '(629) 326-8652', None, None),
    ('Janice Thoas', 'janice.thomas@example.com', '(272) 569-4415', '2745 Thornridge Cir', None),   
    ]

while True:
    print("""
a - add contact
d - delete contact
p - print list of contacts
q - quit from app    
    """)
    
    # action = Prompt.ask("Choise your action")
    action = input('Choosenyour action: ')

    if action == 'q':
        print('Thank you. See you soon')
        break
    elif action == 'a':
        name = input('Enter a name: ')
        email = input('Enter a email: ')
        phone = input('Enter a phone: ')
        address = input('Enter a address (optional): ')
        notes= input('Enter a notes (optional): ')

        # for optional parts
        address = address if len(address) > 0 else None
        notes = notes if len(notes) > 0 else None

        contact = [name, email, phone, address, notes]

        contacts.append(contact)
        print('Contact added succesfully')

    elif action == 'd':         
        email = input('Enter a email: ')
        i = 0
        try:
            while i < len(contacts):
                contact = contacts[i]
                if email in contact:
                    contacts.remove(contact)
                    i += 1
                else:
                    i += 1
        except TypeError:       # to avoide typeerror (None is not iterable)
            continue

    elif action == 'p':
        table = Table(title="Contacts")

        table.add_column("Name", style="cyan")
        table.add_column("phone", style="magenta")
        table.add_column("email", style="green")
        table.add_column("address", style="cyan")
        table.add_column("Notes", style="magenta")

        i = 0
        while i < len(contacts):
            contact = contacts[i]
            table.add_row(
                contact[0],
                contact[2],
                contact[1],
                contact[3] or '-',
                contact[4] or '-',
            )
            i += 1
        console = Console()
        console.print(table)    
## block without add imports
    # elif action == 'p':
    #     i = 0
    #     while i < len(contacts):            # to print in row
    #         contact = contacts[i]
    #         print('Name: {} / email: {} / phone: {} / Adress: {} / notes: {}'. format(
    #             contact[0],
    #             contact[1],
    #             contact[2],
    #             contact[3] or '-',
    #             contact[4] or '-',
    #         ))            
    #         i += 1
    else:
        print('unknown action')
