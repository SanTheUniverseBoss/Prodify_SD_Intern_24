import os

# Function to load contacts from a file
def load_contacts():
    contacts = []
    if os.path.exists('contacts.txt'):
        with open('contacts.txt', 'r') as file:
            for line in file:
                name, phone, email = line.strip().split(',')
                contacts.append({'name': name, 'phone': phone, 'email': email})
    return contacts

# Function to save contacts to a file
def save_contacts(contacts):
    with open('contacts.txt', 'w') as file:
        for contact in contacts:
            file.write(f"{contact['name']},{contact['phone']},{contact['email']}\n")

# Function to display the contact list
def view_contacts(contacts):
    if not contacts:
        print("Contact list is empty.")
    else:
        print("\nContacts:")
        for idx, contact in enumerate(contacts, 1):
            print(f"{idx}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
    print()

# Function to add a new contact
def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    contacts.append({'name': name, 'phone': phone, 'email': email})
    save_contacts(contacts)
    print(f"Contact {name} added successfully.\n")

# Function to edit an existing contact
def edit_contact(contacts):
    view_contacts(contacts)
    try:
        idx = int(input("Enter the number of the contact you want to edit: ")) - 1
        if 0 <= idx < len(contacts):
            print(f"Editing contact {contacts[idx]['name']}")
            contacts[idx]['name'] = input("Enter new name (leave blank to keep current): ") or contacts[idx]['name']
            contacts[idx]['phone'] = input("Enter new phone (leave blank to keep current): ") or contacts[idx]['phone']
            contacts[idx]['email'] = input("Enter new email (leave blank to keep current): ") or contacts[idx]['email']
            save_contacts(contacts)
            print("Contact updated successfully.\n")
        else:
            print("Invalid contact number.\n")
    except ValueError:
        print("Invalid input. Please enter a valid contact number.\n")

# Function to delete a contact
def delete_contact(contacts):
    view_contacts(contacts)
    try:
        idx = int(input("Enter the number of the contact you want to delete: ")) - 1
        if 0 <= idx < len(contacts):
            deleted_contact = contacts.pop(idx)
            save_contacts(contacts)
            print(f"Contact {deleted_contact['name']} deleted successfully.\n")
        else:
            print("Invalid contact number.\n")
    except ValueError:
        print("Invalid input. Please enter a valid contact number.\n")

# Main menu
def main_menu():
    contacts = load_contacts()
    while True:
        print("Contact Management System")
        print("1. View Contacts")
        print("2. Add New Contact")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Exit")
        choice = input("Choose an option (1-5): ")

        if choice == '1':
            view_contacts(contacts)
        elif choice == '2':
            add_contact(contacts)
        elif choice == '3':
            edit_contact(contacts)
        elif choice == '4':
            delete_contact(contacts)
        elif choice == '5':
            print("Exiting Contact Management System.")
            break
        else:
            print("Invalid option. Please choose a valid number.\n")

if __name__ == "__main__":
    main_menu()
