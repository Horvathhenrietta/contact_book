from contact_view import ContactView

INPUT_TEXT = """Enter one of the following commands:
- 'a' to add a contact
- 'l' to list all contacts
- 's' to search for a contact by name
- 'd' to delete a contact
- 'q' to quit
"""


def menu():
    user_input = input(INPUT_TEXT).lower()
    while user_input != 'q':
        if user_input == 'a':
            ContactView.add_contact()
        elif user_input == 'l':
            ContactView.print_all_contacts()
        elif user_input == 's':
            ContactView.search()
        elif user_input == 'd':
            ContactView.delete()
        elif user_input == 'q':
            print('Unknown command, please try again.')
        user_input = input(INPUT_TEXT).lower()


menu()
