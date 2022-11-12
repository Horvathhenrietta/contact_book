from contact_book import ContactBook

ContactBook.create_table()


class ContactView:
    @classmethod
    def add_contact(cls):
        name = input("Name: ")
        phone_num = input("Phone number: ")
        email = input("Email address: ")
        ContactBook.add_contact(name, phone_num, email)

    @classmethod
    def _print_contacts(cls, contacts):
        for contact in contacts:
            print(f"{contact['name']}\t{contact['phone_num']}\t{contact['email']}")

    @classmethod
    def print_all_contacts(cls):
        all_contacts = ContactBook.get_all_contacts()
        cls._print_contacts(all_contacts)

    @classmethod
    def search(cls):
        name = input('Name to search for: ')
        contact = ContactBook.search_by_name(name)
        cls._print_contacts(contact)

    @classmethod
    def delete(cls):
        name = input('Name to delete: ')
        ContactBook.delete_contact(name)
