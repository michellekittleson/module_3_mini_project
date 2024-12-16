'''
Mini-Project: Contact Management System

Your task is to develop a Contact Management System with the following features:

1. User Interface
    - Create a user-friendly command-line interface (CLI) for the Contact Managament System.
    - Display a welcoming message and provide a menu with the following options:

'''

# contacts = {'123': {'name': 'michelle', 'email_address': 'm@m.com', 'notes': 'notes'}}
contacts = {}

def add_contact():
    name = input("Enter name: ")
    phone_number = input("Enter phone number: ")
    email_address = input("Enter email address")
    notes = input("Enter additional notes: ")
    dict1={'name': name, 'email_address': email_address, 'notes': notes}
    contacts[phone_number]=dict1
    print(contacts)

def edit_contact():
    phone_number = input("Enter phone number of contact to edit: ")
    name = input("Enter name: ")
    email_address = input("Enter email address")
    notes = input("Enter additional notes: ")
    contacts[phone_number]['name'] = name
    contacts[phone_number]['email_address'] = email_address
    contacts[phone_number]['notes'] = notes
    print(contacts)

def delete_contact():
    phone_number = input("Enter phone number of contact to delete: ")
    if phone_number in contacts:
        del contacts[phone_number]
        print("Contact deleted.")
    else:
        print("Contact not found")
    

def search_for_contact(contacts, name):
    name = input("Enter name of contact to search: ")
    for contact in contacts: 
        if ['name'].lower() == name.lower():
            return contact
        else:
            print("Contact not found.")
            return None

def display_contacts():
    for contact in contacts:
        print(f"Name: {contact['name']}, Phone Number: {contact['id']}, Email Address: {contact['email_address']}, Notes: {contact['notes']}")

def export_contacts():
    with open('contacts.txt', 'w') as file:
        file.write(contacts)



def main(): 
    while True:
        print("\nWelcome to the Contact Management System!\nMenu:\n1. Add a new contact\n2. Edit an Existing Contact\n3. Delete a Contact\n4. Search for a Contact\n5. Display All Contacts\n6. Export Contacts to a Text File\n8. Quit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            edit_contact()
        elif choice == '3':
            delete_contact()
        elif choice == '4':
            search_for_contact()
        elif choice == '5':
            display_contacts()
        elif choice == '6':
            export_contacts()
        elif choice == '8':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number corresponding to a choice.")

if __name__ == "__main__":
    main()