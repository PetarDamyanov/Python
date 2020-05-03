import sqlite3


def mechanic_menu(user):
    menu = f'''
    Hello, {user}!
    You can choose from the following commands:
    list_all_free_hours (lafh)
    list_free_hours <date> (lfh)
    list_all_busy_hours (labh)
    list_busy_hours <date> (lbh)
    add_new_repair_hour (anr)
    add_new_service(ans)
    update_repair_hour <hour_id>(urh)
    exit
    '''
    print(menu)
    return input('Choise:')


def mechanic_choise(user, user_id):
    choise = mechanic_menu(user)
    c1 = None
    if choise.count(' ') > 0:
        c1 = choise.split(" ")[0]
        c2 = choise.split(" ")[1]
    if c1:
        if c1 == 'lfh':
            list_free_hours(date=c2, user_id=user_id)
        elif c1 == 'lbh':
            list_busy_hours(date=c2, user_id=user_id)
        elif c1 == 'urh':
            update_repair_hour(hour_id=c2)
    if choise == 'lafh':
        list_all_free_hours(user_id=user_id)
    elif choise == 'labh':
        list_all_busy_hours(user_id=user_id)
    elif choise == 'anr':
        add_new_repair_hour()
    elif choise == 'ans':
        add_new_service(user_id=user_id)
    elif choise == 'e':
        return False


def add_new_service(user_id):
    name = input('service name')
    connection = sqlite3.connect('vehicle_repair_management.db')
    cursor = connection.cursor()
    insert_query = f'''
    INSERT INTO Service (name)
      VALUES ( ? )
    '''
    insert_query_2 = f'''
    INSERT INTO `Mechanic_services` (service_id,mechanic_id)
    VALUES((SELECT id FROM `Service` WHERE name = ?) , ?);
    '''
    cursor.execute(insert_query, (name,))
    cursor.execute(insert_query_2, (name, user_id))
    connection.commit()
    connection.close()


def list_free_hours(*, date, user_id):
    connection = sqlite3.connect('vehicle_repair_management.db')
    cursor = connection.cursor()
    select_query = f'''
    SELECT id,date,start_hour FROM `Vehicle_repair`
    WHERE date = ? AND vechile is null AND mechanic_service = (SELECT id FROM Mechanic_services WHERE mechanic_id = ?);
    '''
    free_hours = cursor.execute(select_query, (date, user_id))
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


def list_all_free_hours(user_id):
    connection = sqlite3.connect('vehicle_repair_management.db')
    cursor = connection.cursor()
    select_query = f'''
    SELECT id,date,start_hour FROM `Vehicle_repair`
    WHERE vechile is null AND mechanic_service = (SELECT id FROM Mechanic_services WHERE mechanic_id = ?);
    '''
    print(user_id)
    free_hours = cursor.execute(select_query, (user_id,))
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


def list_busy_hours(*, date, user_id):
    connection = sqlite3.connect('vehicle_repair_management.db')
    cursor = connection.cursor()
    select_query = f'''
    SELECT * FROM `Vehicle_repair`
    WHERE date = ? AND vechile is not null AND mechanic_service = (SELECT id FROM Mechanic_services WHERE mechanic_id = ?);
    '''
    free_hours = cursor.execute(select_query, (date, user_id))
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


def list_all_busy_hours(user_id):
    connection = sqlite3.connect('vehicle_repair_management.db')
    cursor = connection.cursor()
    select_query = f'''
    SELECT * FROM `Vehicle_repair`
    WHERE vechile is not null AND mechanic_service = (SELECT id FROM Mechanic_services WHERE mechanic_id = ?);
    '''
    free_hours = cursor.execute(select_query, (user_id,))
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


def add_new_repair_hour():
    date = input('date')
    start_hour = input('start_hour')
    print_service()
    service = input('start_hour id')
    connection = sqlite3.connect('vehicle_repair_management.db')
    cursor = connection.cursor()
    insert_query = f'''
    INSERT INTO `Vehicle_repair` (`date`,start_hour, mechanic_service)
    VALUES (?,?, ?);
    '''
    cursor.execute(insert_query, (date, start_hour, service))
    connection.commit()
    connection.close()


def print_small_menu():
    menu = f'''
    Choose one of the following:
    1 - change start hour
    2 - change bill
    3 - return to main menu
    '''
    print(menu)
    return input('choise:')


def update_repair_hour(*, hour_id):
    connection = sqlite3.connect('vehicle_repair_management.db')
    cursor = connection.cursor()
    select_query = f'''
    SELECT date,start_hour,user_name,model,category,bill
    FROM `Vehicle_repair`
    JOIN `Vehicle`
    ON `Vehicle_repair`.vechile = `Vehicle`.id
    JOIN `BaseUser`
    ON `Vehicle`.owner = BaseUser.id;
    '''
    repair_info = cursor.execute(select_query)
    connection.commit()
    for info in repair_info:
        print(f' {info[0]} at {info[1]} \n Client: {info[2]} \n Car:{info[3]} {info[4]}\n bill:{info[5]}')
    connection.close()
    exit = True
    while exit:
        choise = print_small_menu()

        if choise == '1':
            date = input('Date:')
            start_hour = input('hour:')
            connection = sqlite3.connect('vehicle_repair_management.db')
            cursor = connection.cursor()
            update_query = f'''
            UPDATE `Vehicle_repair` SET date = ?, start_hour = ?
            WHERE id = ? ;
            '''
            cursor.execute(update_query, (date, start_hour, hour_id))
            connection.commit()
            connection.close()

        elif choise == '2':
            bill = input("bill")
            connection = sqlite3.connect('vehicle_repair_management.db')
            cursor = connection.cursor()
            update_query = f'''
            UPDATE `Vehicle_repair` SET bill = ?
            WHERE id = ? ;
            '''
            cursor.execute(update_query, (bill, hour_id))
            connection.commit()
            connection.close()
        elif choise == '3':
            exit = False
