import  customerloans

def connect_to_db():
    connection =  customerloans.connect(
        database="database_name",
        user="username",
        password="password",
        host="localhost")
    return connection

def extract_data():
    connection = connect_to_db()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM table_name")
    data = cursor.fetchall()

    connection.close()
    return data

if __name__ == "__main__":
    data = extract_data()
    for row in data:
        print(row)
class RDSDatabaseConnector:
    def __init__(self, database_name, user, password, host):
        self.connection = customerloans.connect(
            database=database_name,
            user=user,
            password=password,
            host=host)
        
    def extract_data(self, query):
        cursor = self.connection.cursor()
        cursor.execute(query)
        data = cursor.fetchall()
        return data

    def close_connection(self):
        self.connection.close()

if __name__ == "__main__":
    connector = RDSDatabaseConnector("database_name", "username", "password", "localhost")
    data = connector.extract_data("SELECT * FROM table_name")
    for row in data:
        print(row)

    connector.close_connection()
