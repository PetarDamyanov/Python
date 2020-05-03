import sqlite3


def client_menu(user):
    menu = f'''
    Hello, {user}!
    You can choose from the following commands:
    list_all_free_hours (lah)
    list_free_hours <date> (lfh)
    save_repair_hour <hour_id> (srh)
    update_repair_hour <hour_id> (urh)
    delete_repair_hour <hour_id> (drh)
    list_personal_vehicles (lpv)
    add_vehicle (av)
    update_vehicle <vehicle_id> (uv)
    delete_vehicle <vehicle_id> (dv)
    exit (e)
    '''
    print(menu)
    return input('Choise:')


def cleint_choise(user, user_id):
    choise = client_menu(user)
    c1 = None
    if choise.count(' ') > 0:
        c1 = choise.split(" ")[0]
        c2 = choise.split(" ")[1]
    if c1:
        if c1 == 'lfh':
            list_free_hours(date=c2)
        elif c1 == 'srh':
            save_repair_hour(hour_id=c2, owner=user_id)
        elif c1 == 'urh':
            update_repair_hour(hour_id=c2)
        elif c1 == 'drh':
            delete_repair_hour(hour_id=c2)
        elif c1 == 'uv':
            update_vehicle(id=c2)
        elif c1 == 'dv':
            delete_vehicle(id=c2)
    if choise == 'lah':
        list_all_free_hours()
    elif choise == 'av':
        add_vehicle(owner=user_id)
    elif choise == 'lpv':
        list_personal_vehicles(owner=user_id)
    elif choise == 'e':
        return False


def add_vehicle(*, owner):
    category = input('Category')
    make = input('Make')
    model = input('Model')
    register_number = input('Register Number')
    gear_box = input('Gear box')
    connection = sqlite3.connect('vehicle_repair_management.db')
    cursor = connection.cursor()
    insert_query = f'''
    INSERT INTO Vehicle (category, make, model, register_number, gear_box, owner)
      VALUES ( ? , ? , ? , ? , ? , ?)
    '''
    cursor.execute(insert_query, (category, make, model, register_number, gear_box, owner))
    connection.commit()
    connection.close()


def update_vehicle(*, id):
    category = input('Category')
    make = input('Make')
    model = input('Model')
    register_number = input('Register Number')
    gear_box = input('Gear box')
    connection = sqlite3.connect('vehicle_repair_management.db')
    cursor = connection.cursor()
    update_query = f'''
    UPDATE Vehicle SET category = ? , make = ? , model = ? , register_number = ? , gear_box = ?  WHERE id = ?
    '''
    cursor.execute(update_query, (category, make, model, register_number, gear_box, id))
    connection.commit()
    connection.close()


def delete_vehicle(*, id):
    connection = sqlite3.connect('vehicle_repair_management.db')
    cursor = connection.cursor()
    delete_query = f'''
    DELETE FROM  Vehicle  WHERE id = ?
    '''
    cursor.execute(delete_query, (id,))
    connection.commit()
    connection.close()


def list_personal_vehicles(*, owner):
    connection = sqlite3.connect('vehicle_repair_management.db')
    cursor = connection.cursor()
    select_query = f'''
    SELECT * FROM `Vehicle`
    WHERE owner = ?;
    '''
    vehicle = cursor.execute(select_query, (owner,))
    connection.commit()
    title = f'''
    +-------+---------------+--------+--------+-----------------+---------+
    |  id   |   category    | model  |  make | register_number | gear box|
    +-------+---------------+--------+--------+-----------------+---------+
    '''
    print(title)
    for v in vehicle:
        print(f'| {v[0]} | {v[1]} |  {v[3]} | {v[2]} | {v[4]} | {v[5]} |')
        print('  +-------+---------------+--------+--------+-----------------+---------+')
    connection.close()


def list_free_hours(*, date):
    connection = sqlite3.connect('vehicle_repair_management.db')
    cursor = connection.cursor()
    select_query = f'''
    SELECT * FROM `Vehicle_repair`
    WHERE date = ? AND vechile is null;
    '''
    free_hours = cursor.execute(select_query, (date,))
    connection.commit()
    title = f'''
    +-------+-----------+-------+
    |  id   |   Date    | hour  |
    +-------+-----------+-------+
    '''
    print(title)
    for hours in free_hours:
        print(f'| {hours[0]} | {hours[1]} |  {hours[2]} |')
        print('+-------+-----------+-------+')
    connection.close()


def list_all_free_hours():
    connection = sqlite3.connect('vehicle_repair_management.db')
    cursor = connection.cursor()
    select_query = f'''
    SELECT * FROM `Vehicle_repair` WHERE vechile is null;
    '''
    free_hours = cursor.execute(select_query)
    connection.commit()
    title = f'''
    +-------+-----------+-------+
    |  id   |   Date    | hour  |
    +-------+-----------+-------+
    '''
    print(title)
    for hours in free_hours:
        print(f'| {hours[0]} | {hours[1]} |  {hours[2]} |')
        print('+-------+-----------+-------+')
    connection.close()


def print_service():
    connection = sqlite3.connect('vehicle_repair_management.db')
    cursor = connection.cursor()
    select_query = f'''
    SELECT * FROM `Service`;
    '''
    service = cursor.execute(select_query)
    connection.commit()
    title = f'''
    +-------+-----------+
    |  id   |  service  |
    +-------+-----------+
    '''
    print(title)
    for s in service:
        print(f'| {s[0]} | {s[1]} |')
        print('+-------+-----------+')
    connection.close()


def save_repair_hour(*, hour_id, owner):
    list_personal_vehicles(owner=owner)
    vehicle = input('vehicle id:')
    print_service()
    service = input('service id:')
    connection = sqlite3.connect('vehicle_repair_management.db')
    cursor = connection.cursor()
    update_query = f'''
    UPDATE `Vehicle_repair` SET vechile = ?, mechanic_service = ?
    WHERE id = ? ;
    '''
    cursor.execute(update_query, (vehicle, hour_id, service))
    connection.commit()
    connection.close()


def update_repair_hour(*, hour_id):
    # hour_id = input('hour_id')
    date = input('Date')
    start_hour = input('Start hour')
    vehicle = input('vehicle id:')
    connection = sqlite3.connect('vehicle_repair_management.db')
    cursor = connection.cursor()
    update_query = f'''
    UPDATE `Vehicle_repair` SET date = ?, start_hour = ?, vechile = ?
    WHERE id = ?
    '''
    cursor.execute(update_query, (date, start_hour, vehicle, hour_id))
    connection.commit()
    connection.close()


def delete_repair_hour(*, hour_id):
    # hour_id = input('hour_id')
    connection = sqlite3.connect('vehicle_repair_management.db')
    cursor = connection.cursor()
    delete_query = f'''
    UPDATE `Vehicle_repair` SET vechile = NULL
    WHERE id = ?
    '''
    cursor.execute(delete_query, (hour_id,))
    connection.commit()
    connection.close()
