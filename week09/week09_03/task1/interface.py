import sqlite3


def add(*, full_name, email, age, phone, additional_info):
    connection = sqlite3.connect('business_card_catalog.db')
    cursor = connection.cursor()
    insert_query = f'''
    INSERT INTO users (full_name, email, age, phone, additional_info)
      VALUES ( ? , ? , ? , ? , ?)
    '''
    cursor.execute(insert_query, (full_name, email, age, phone, additional_info))
    connection.commit()
    connection.close()


def list():
    connection = sqlite3.connect('business_card_catalog.db')
    cursor = connection.cursor()
    select_query = f'''
    SELECT id,full_name,email,phone,age,additional_info
    FROM users;
    '''
    cursor.execute(select_query)
    users_info = cursor.fetchall()
    connection.close()
    i = 0
    for users in users_info:
        print(f'{i}. ID: {users[0]}, Email:{users[2]}, Full Name: {users[1]}')
        i += 1


def delete(*, id):
    connection = sqlite3.connect('business_card_catalog.db')
    cursor = connection.cursor()

    get(id=id)
    tf = input("Delete? y/n")
    if tf == 'y':
        delete_query = f'''
        DELETE FROM users
        WHERE id = ?;
        '''
        cursor.execute(delete_query, (id,))
        connection.commit()
        connection.close()
    else:
        connection.close()


def get(*, id):
    connection = sqlite3.connect('business_card_catalog.db')
    cursor = connection.cursor()
    select_query = f'''
    SELECT id,full_name,email,phone,age,additional_info
    FROM users
    WHERE id = ?;
    '''
    cursor.execute(select_query, (id,))
    users_info = cursor.fetchone()
    connection.close()
    # users_info
    user = f'''
    ID: {users_info[0]}
    Full name: {users_info[1]}
    Email: {users_info[2]}
    Age: {users_info[3]}
    Phone: {users_info[4]}
    Additional info: {users_info[5]}
    '''
    print(user)


def help():
    help = f'''
    1. `a`-`add` - insert new business card
    2. `l`-`list` - list all business cards
    3. `d`-`delete` - delete a certain business card (`ID` is required)
    4. `g`-`get` - display full information for a certain business card (`ID` is required)
    5. `h`-`help` - list all available options
    6. `q`-`quit`
'''
    print(help)
