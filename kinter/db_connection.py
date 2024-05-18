import mysql.connector

class DatabaseConnector:
    def __init__(self, host, user, password, database,cursor):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None
        self.cursor = cursor

    def connect(self):
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        self.cursor = self.connection.cursor()

    def execute_query(self, query, params=None):
        try:
            self.cursor.execute(query, params)
            self.connection.commit()
            return True
        except mysql.connector.Error as err:
            print("Error executing query:", err)
            self.connection.rollback()
            return False

    def fetch_data(self, query, params=None):
        self.cursor.execute(query, params)
        return self.cursor.fetchall()

    def close_connection(self):
        self.cursor.close()
        self.connection.close()
