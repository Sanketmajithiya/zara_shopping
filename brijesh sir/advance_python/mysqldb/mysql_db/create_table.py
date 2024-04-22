from . import dbConnection

def create_table():
    table_name = input("Enter a table-name: ")
    table_config = input("Enter table config: ")
    sql = f"create table {table_name} {table_config}"
    print(sql)
    dbConnection.mycursor.execute(sql)