from . import dbConnection

def show_table_data():
    dbConnection.mycursor.execute("select * from students order by fullname desc limit 5")
    return dbConnection.mycursor.fetchall()