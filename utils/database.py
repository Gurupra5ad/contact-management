from .database_connection import DatabaseConnection
""" 
        Concerned with storing and retreiving books from the list
"""


def create_contact_table():
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('CREATE TABLE IF NOT EXISTS contact(name text primary key, number integer)')

def add_contact(name, number):
    with DatabaseConnection('data.db') as connection:

        cursor = connection.cursor()

        cursor.execute('INSERT INTO contact VALUES(?,?)', (name,number))


def get_all_contacts():
    with DatabaseConnection('data.db') as connection:

        cursor = connection.cursor()

        cursor.execute('SELECT * FROM contact')
        contacts = [{'name':row[0], 'number':row[1]} for row in cursor.fetchall()]

        return contacts


def delete_contact(name):
    with DatabaseConnection('data.db') as connection:

        cursor = connection.cursor()

        cursor.execute('DELETE FROM contact WHERE name = ?', (name,))
