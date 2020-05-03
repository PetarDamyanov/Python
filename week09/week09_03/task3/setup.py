import sqlite3


def setup_db():
    connection = sqlite3.connect('hacker.db')
    cursor = connection.cursor()
    query = f'''
    CREATE TABLE IF NOT EXISTS CipherBreaker (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        messege VARCHAR(50),
        encypted_message TEXT
    );
    '''
    cursor.executescript(query)
    connection.commit()
    connection.close()


def main():
    setup_db()


if __name__ == '__main__':
    main()
