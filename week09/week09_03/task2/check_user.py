import sqlite3


def get(*, user_name):
    connection = sqlite3.connect('vehicle_repair_management.db')
    cursor = connection.cursor()
    select_query = f'''
    SELECT id
    FROM BaseUser
    WHERE user_name = ? ;
    '''
    cursor.execute(select_query, (user_name,))
    users_info = cursor.fetchone()
    connection.close()
    # print(users_info[0])
    if not users_info:
        return None
    return users_info[0]


def add_user():
    user_name = input('user_name:')
    email = input('email:')
    phone = int(input('phone:'))
    addres = input('addres')
    client_mechanic = input('Are you a client or mechanic: c/m:')
    while client_mechanic != 'c' and client_mechanic != 'm':
        print('wrong input please try again')
        client_mechanic = input('Are you a client or mechanic:c/m:')
    if client_mechanic == 'm':
        title = input('title')
    connection = sqlite3.connect('vehicle_repair_management.db')
    cursor = connection.cursor()
    insert_query_client = f'''
    INSERT INTO BaseUser (user_name, email, phone, addres)
      VALUES ( ? , ? , ? , ? )
    '''
    insert_query_client_2 = f'''
    INSERT INTO Client (base_id)
      VALUES ( (SELECT id FROM BaseUser WHERE user_name = ?) )
    '''
    insert_query_mechanic = f'''
    INSERT INTO BaseUser (user_name, email, phone, addres)
     VALUES ( ? , ? , ? , ? )
     '''
    insert_query_mechanic_2 = f'''
    INSERT INTO Mechanic (base_id,title)
      VALUES ( (SELECT id FROM BaseUser WHERE user_name = ?), ? )
    '''
    if client_mechanic == 'c':
        cursor.execute(insert_query_client, (user_name, email, phone, addres,))
        cursor.execute(insert_query_client_2, (user_name,))
    if client_mechanic == 'm':
        cursor.execute(insert_query_mechanic, (user_name, email, phone, addres,))
        cursor.execute(insert_query_mechanic_2, (user_name, title,))
    connection.commit()
    connection.close()

    welcome = f'''
    Thank you, {user_name}!
    Welcome to Vehicle Services!
    Next time you try to login, provide your user_name!
    '''
    print(welcome)


def user_is_client(*, id):
    connection = sqlite3.connect('vehicle_repair_management.db')
    cursor = connection.cursor()
    select_query = f'''
    SELECT *
    FROM Client
    WHERE base_id = ?;
    '''
    cursor.execute(select_query, (id,))
    users_info = cursor.fetchall()
    connection.close()
    return users_info


def user_is_mechanic(*, id):
    connection = sqlite3.connect('vehicle_repair_management.db')
    cursor = connection.cursor()
    select_query = f'''
    SELECT *
    FROM Mechanic
    WHERE base_id = ?;
    '''
    cursor.execute(select_query, (id,))
    users_info = cursor.fetchall()
    connection.close()
    return users_info


def check(user):
    user_id = get(user_name=user)
    # print(user_id)
    if not user_id:
        add_user()
    else:
        if len(user_is_client(id=user_id)) > 0:
            return 'c', user_id
        if len(user_is_mechanic(id=user_id)) > 0:
            return 'm', user_id
