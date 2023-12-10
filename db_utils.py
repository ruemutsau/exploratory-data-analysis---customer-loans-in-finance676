import  RDSDatabase

def connect_to_db():
    connection =  RDSDatabase.connect(
        database="database_name",
        user="username",
        password="password",
        host="localhost"
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
