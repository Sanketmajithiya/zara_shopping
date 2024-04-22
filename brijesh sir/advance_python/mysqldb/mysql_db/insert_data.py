from . import dbConnection

def insert_data():
    insert_query = "INSERT INTO students (fullname, age) VALUES (%s, %s)"

    data = [
    ('John Smith', 20),
    ('Alice Johnson', 22),
    ('Michael Brown', 21),
    ('Emily Davis', 19),
    ('David Wilson', 23),
    ('Sarah Martinez', 20),
    ('James Taylor', 22),
    ('Emma Anderson', 21),
    ('Daniel Thomas', 20),
    ('Olivia Clark', 19),
    ('Matthew Hall', 21),
    ('Sophia Lewis', 22),
    ('Benjamin Lee', 20),
    ('Chloe Harris', 21),
    ('William Wright', 23),
    ('Ava King', 20),
    ('Ethan Evans', 21),
    ('Mia Moore', 19),
    ('Alexander Scott', 22),
    ('Isabella Green', 20)
    ]

    dbConnection.mycursor.executemany(insert_query, data)
    dbConnection.myconn.commit()