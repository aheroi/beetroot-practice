# before running: pip install rich
import uuid
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt

print("Welcome to the Contacts v1.0!")

# Contact should contain name, email, phone, address (optional) and notes (optional)
contacts = [
    {
        'id':'5dc94f41-2be2-4139-a832-c3fb3b542958',
        'name':'Janice Thomas',
        'email': 'janice.thomas@example.com',
        'phone': '(272) 569-4415',
        'address': '2745 Thornridge Cir',
        'notes': None
    },
    {
        'id': 'bba4e536-03d6-4738-ab59-7fab218cf9a1',
        'name':'Cassandra Burton',
        'email':'cassandra.burton@example.com',
        'phone':'(629) 326-8652', 
        'address': None, 
        'notes': None
     },
]

while True:
    print("""
a - add a contact
r - remove contact
p - print list of contacts
q - quit from app
    """)

    action = Prompt.ask("Choise your action")

    if action == "q":
        print("Thank you! See you soon!")
        break
    elif action == "a":
        id = str(uuid.uuid4())
        name = input("Enter a name: ")
        email = input("Enter an email: ")
        phone = input("Enter a phone: ")
        address = input("Enter an address (optional): ")
        notes = input("Enter the notes (optional): ")

        address = address if len(address) > 0 else None
        notes = notes if len(notes) > 0 else None

        contact = {'name':name, 'email':email, 'phone':phone, 'address': address, 'notes':notes}

        contacts.append(contact)
        print("Contact added successfully!")

        
    elif action == 'r':
        email = Prompt.ask('Enter email of the contact to remove')

        for contact in contacts:
            if email.lower() == contact['email'].lower():
                contacts.remove(contact)
                print(f"Contact {contact['name']} removed successfully!")
                break
        else:
            print('Contact is not exist')
        
    elif action == "p":
        table = Table(title="Contacts")

        table.add_column("Name", style="cyan")
        table.add_column("Email", style="cyan")
        table.add_column("Phone", style="bright_blue")
        table.add_column("Address", style="bright_blue")
        table.add_column("Notes", style="bright_blue")


        for contact in contacts:
            table.add_row(
                contact['name'],
                contact['email'],
                contact['phone'],
                contact['address'] or "-",
                contact.get('notes', '-'),
                # contact['notes'] or "-",
                )


        # i = 0
        # while i < len(contacts):
        #     contact = contacts[i]

        #     table.add_row(
        #         contact['name'],
        #         contact['email'],
        #         contact['phone'],
        #         contact['address'] or "-",
        #         contact['notes'] or "-",
        #     )
        #     i += 1

        #     print("Name: {} / Email: {} / Phone: {} / Address: {} / Notes: {}".format(
        #         contact[0],
        #         contact[1],
        #         contact[2],
        #         contact[3] or "-",
        #         contact[4] or "-",
        #     ))

        console = Console()
        console.print(table)
    else:
        print("Unknown action!")
