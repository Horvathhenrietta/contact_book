from database_connection import DatabaseConnection


class ContactBook:
    database_file = 'contactbook.db'
    table = 'contacts'

    @classmethod
    def create_table(cls):
        with DatabaseConnection(cls.database_file) as connection:
            cursor = connection.cursor()

            cursor.execute(
                f'CREATE TABLE IF NOT EXISTS {cls.table}(Contact_Name primary key, Phone_Num text, Email text)')

    @classmethod
    def add_contact(cls, name: str, phone_num: str, email: str) -> None:
        with DatabaseConnection(cls.database_file) as connection:
            cursor = connection.cursor()

            cursor.execute(F'INSERT INTO {cls.table} VALUES("{name}", "{phone_num}", "{email}")')

    @classmethod
    def get_all_contacts(cls):
        with DatabaseConnection(cls.database_file) as connection:
            cursor = connection.cursor()

            cursor.execute(f'SELECT * FROM {cls.table}')
            contacts = [{'name': row[0], 'phone_num': row[1], 'email': row[2]} for row in cursor.fetchall()]

        return contacts

    @classmethod
    def search_by_name(cls, name):
        with DatabaseConnection(cls.database_file) as connection:
            cursor = connection.cursor()
            cursor.execute(f'SELECT * FROM {cls.table} WHERE Contact_Name=?', (name,))

            contacts = [{'name': row[0], 'phone_num': row[1], 'email': row[2]} for row in cursor.fetchall()]

            return contacts

    @classmethod
    def delete_contact(cls, name):
        with DatabaseConnection(cls.database_file) as connection:
            cursor = connection.cursor()

            cursor.execute(f'DELETE FROM {cls.table} WHERE Contact_Name=?', (name,))



