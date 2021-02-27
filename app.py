from utils import database

USER_CHOICE = """
Enter :
 - 'a' to add a new contact
 - 'l' to list all the contact
 - 'd' to delete a book
 - 'q' to quit 
Your choice ? : """

def menu():
    database.create_contact_table()
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input == 'a':
            prompt_add_contact()
        elif user_input == 'l':
            list_contacts()
        elif user_input == 'd':
            prompt_delete_contact()
        else:
            print("Unknown input given, please try again. ")
        
        user_input = input(USER_CHOICE)


def prompt_add_contact():
    name = input("Enter the contact name : ")
    number = input("Enter the contact number: ")
    database.add_contact(name,number)


def list_contacts():
    contacts = database.get_all_contacts()
    for contact in contacts:
        print(f"{contact['name']}'s number is {contact['number']}")


def prompt_delete_contact():
    name = input("Enter the name of the contact that u want to delete : ")
    database.delete_contact(name)

menu()