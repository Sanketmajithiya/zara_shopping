import mysql.connector

myconn = mysql.connector.connect(user='root', password='root',
                              host='127.0.0.1', database="school")

mycursor = myconn.cursor()