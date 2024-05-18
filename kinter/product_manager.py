from db_connection import DatabaseConnector

class Product:
    def __init__(self, id, name, price, quantity):
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity

class ProductManager:
    def __init__(self):
        self.db_connector = DatabaseConnector(host='localhost', user='root', password='password', database='product_db')
        self.db_connector.connect()

    def add_product(self, product):
        query = "INSERT INTO products (name, price, quantity) VALUES (%s, %s, %s)"
        params = (product.name, product.price, product.quantity)
        return self.db_connector.execute_query(query, params)

    # Implement other methods for CRUD operations on products
