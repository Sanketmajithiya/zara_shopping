from db_connection import DatabaseConnector

class User:
    def __init__(self, id, username, password, email):
        self.id = id
        self.username = username
        self.password = password
        self.email = email

class UserManager:
    def __init__(self):
        self.db_connector = DatabaseConnector(host='localhost', user='root', password='password', database='product_db')
        self.db_connector.connect()

    def register_user(self, user):
        query = "INSERT INTO users (username, password, email) VALUES (%s, %s, %s)"
        params = (user.username, user.password, user.email)
        return self.db_connector.execute_query(query, params)

    # Implement other methods for user management
