## CREATE DB ##

import sqlite3

connection = sqlite3.connect('CoolebraSPA.db')
cursor = connection.cursor()

## CREACION TABLAS ##
cursor.execute('''
    CREATE TABLE Product (
        id INTEGER PRIMARY KEY,
        Name TEXT,
        SKU TEXT,
        EAN TEXT,
        Market_id INTEGER,
        FOREIGN KEY (Market_id) REFERENCES Market(id)
    )
''')


cursor.execute('''
    CREATE TABLE Market (
        id INTEGER PRIMARY KEY,
        Name TEXT
    )
''')

cursor.execute('''
    CREATE TABLE Price (
        id INTEGER PRIMARY KEY,
        product_id INTEGER,
        normal_price REAL,
        discount_price REAL,
        active INTEGER,
        create_date DATE,
        FOREIGN KEY (product_id) REFERENCES Product(id)
    )
''')


## INSERTAR DATOS A LAS TABLAS ##
cursor.execute("INSERT INTO Market (Name) VALUES ('Market1')")
cursor.execute("INSERT INTO Market (Name) VALUES ('Market2')")

cursor.execute("INSERT INTO Product (Name, SKU, EAN, Market_id) VALUES ('Product1', 'SKU1', 'EAN1', 1)")
cursor.execute("INSERT INTO Product (Name, SKU, EAN, Market_id) VALUES ('Product2', 'SKU2', 'EAN2', 2)")

cursor.execute("INSERT INTO Price (product_id, normal_price, discount_price, active, create_date) VALUES (1, 100, 90, 1, '2023-01-01')")
cursor.execute("INSERT INTO Price (product_id, normal_price, discount_price, active, create_date) VALUES (1, 120, 110, 0, '2023-01-02')")
cursor.execute("INSERT INTO Price (product_id, normal_price, discount_price, active, create_date) VALUES (2, 150, 140, 1, '2023-01-03')")


connection.commit()
connection.close()
