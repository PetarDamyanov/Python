import sqlite3
from secret_keeper import make_it_secret


def read_file(file):
    f = open(file, "r")
    content = f.read().split(' ')
    f.close()
    return content


def insert_query(msg):
    connection = sqlite3.connect('hacker.db')
    cursor = connection.cursor()
    query = f'''
    SELECT id FROM CipherBreaker WHERE messege = ?;
    '''
    cursor.execute(query, (msg,))
    msg_check = cursor.fetchone()
    connection.close()
    if not msg_check:
        connection = sqlite3.connect('hacker.db')
        cursor = connection.cursor()
        query = f'''
        INSERT INTO CipherBreaker (messege, encypted_message) VALUES(?,?);
        '''
        encypted_message = make_it_secret(msg)
        cursor.execute(query, (msg, encypted_message))
        connection.commit()
        connection.close()


def main():
    for messege in read_file('dict.txt'):
        if len(messege) <= 5:
            insert_query(messege)
            insert_query(f'{messege}.')
            insert_query(f'{messege}!')
            insert_query(f'{messege}<')
            insert_query(f'{messege}s')
            insert_query(f'{messege}'.capitalize())
            insert_query(f'{messege}s'.capitalize())
    for messege in read_file('refactor_verb.txt'):
        if len(messege) <= 5:
            insert_query(messege)
            insert_query(f'{messege}.')
            insert_query(f'{messege}!')
            insert_query(f'{messege}<')
            insert_query(f'{messege}s')
            insert_query(f'{messege}'.capitalize())
            insert_query(f'{messege}s'.capitalize())


if __name__ == '__main__':
    main()
