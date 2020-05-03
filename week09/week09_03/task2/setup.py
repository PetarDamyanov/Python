import sqlite3


def setup_db():
    connection = sqlite3.connect('vehicle_repair_management.db')
    cursor = connection.cursor()
    query = f'''
    CREATE TABLE IF NOT EXISTS BaseUser (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_name VARCHAR(50),
        email VARCHAR(100),
        phone INTEGER,
        addres VARCHAR(255)
    );
    CREATE TABLE IF NOT EXISTS Client (
        base_id INTEGER NOT NULL,
        FOREIGN KEY(base_id) REFERENCES BaseUser(id)
    );
    CREATE TABLE IF NOT EXISTS Mechanic (
        base_id INTEGER NOT NULL,
        title VARCHAR(50),
        FOREIGN KEY(base_id) REFERENCES BaseUser(id)
    );
    CREATE TABLE IF NOT EXISTS Vehicle (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        category VARCHAR(50) ,
        make VARCHAR(100),
        model VARCHAR(50),
        register_number VARCHAR(50),
        gear_box VARCHAR(50),
        owner INTEGER ,
        FOREIGN KEY(owner) REFERENCES Client(base_id)
    );
    CREATE TABLE IF NOT EXISTS Service (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(50)
    );
    CREATE TABLE IF NOT EXISTS Mechanic_services (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        mechanic_id INTEGER,
        service_id INTEGER,
        FOREIGN KEY(mechanic_id) REFERENCES Mechanic(id),
        FOREIGN KEY(service_id) REFERENCES Service(id)
    );
    CREATE TABLE IF NOT EXISTS Vehicle_repair (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date VARCHAR(50),
        start_hour VARCHAR(100),
        vechile INTEGER,
        bill REAL,
        mechanic_service INTEGER,
        FOREIGN KEY(vechile) REFERENCES Vehicle(id),
        FOREIGN KEY(mechanic_service) REFERENCES Mechanic_services(id)
    );
    '''
    cursor.executescript(query)
    connection.commit()
    connection.close()


def main():
    setup_db()


if __name__ == '__main__':
    main()
