from . import dbConnection

def show_all_table_name():
    dbConnection.mycursor.execute("show tables")
    return dbConnection.mycursor.fetchall()