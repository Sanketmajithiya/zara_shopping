from . import dbConnection

def show_all_db_name():
    dbConnection.mycursor.execute("show databases")
    return dbConnection.mycursor.fetchall()