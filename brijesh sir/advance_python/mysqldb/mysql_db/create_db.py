from . import dbConnection

def create_database():
    database_name = input("Enter a database name : ")
    sql = f"create database {database_name}"
    dbConnection.mycursor.execute(sql)