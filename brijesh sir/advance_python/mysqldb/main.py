# from mysql_db.dbConnection import *
from mysql_db.create_db import create_database
from mysql_db.create_table import create_table
from mysql_db.insert_data import insert_data
from mysql_db.show_databases import  show_all_db_name
from mysql_db.show_tables import  show_all_table_name
from mysql_db.show_data import show_table_data


# create_database()

# create_table()

# insert_data()

# for db in show_all_db_name():
#     print(db[0])

# for db in show_all_table_name():
#     print(db[0])

for row in show_table_data():
    print(row[1])
