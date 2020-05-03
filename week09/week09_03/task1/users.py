import sqlite3


def create_users_table():
    connection = sqlite3.connect('business_card_catalog.db')
    cursor = connection.cursor()
    query = f'''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        full_name VARCHAR(50) NOT NULL,
        email VARCHAR(100) NOT NULL,
        age INTEGER NOT NULL,
        phone VARCHAR(50) NOT NULL,
        additional_info TEXT
    )
    '''
    cursor.execute(query)
    connection.commit()
    connection.close()


def main():
    create_users_table()


if __name__ == '__main__':
    main()
