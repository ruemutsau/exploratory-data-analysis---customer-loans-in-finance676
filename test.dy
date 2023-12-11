import pymysql
import yaml
from sqlalchemy import create_engine
import pandas as pd

class RDSDatabaseConnector:

    def __init__(self, credentials_dict):
        self.db_host = credentials_dict['RDS_HOST']
        self.db_name = credentials_dict['RDS_DATABASE']
        self.db_user = credentials_dict['RDS_USER']
        self.db_password = credentials_dict['RDS_PASSWORD']

    def connect_to_database(self):
        connection = pymysql.connect(host=self.db_host, db=self.db_name, user=self.db_user, password=self.db_password)
        return connection

    def load_credentials(self):
        with open('credentials.yaml', 'r') as f:
            credentials_dict = yaml.load(f)
        return credentials_dict

    def query_database(self, query):
        connection = self.connect_to_database()
        cursor = connection.cursor()

        try:
            cursor.execute(query)
            results = cursor.fetchall()
            return results
        except Exception as e:
            print("Error querying database:", e)
            connection.close()
            return None

    def close_connection(self, connection):
        if connection is not None:
            connection.close()

    def query_and_return_pandas_dataframe(self, query):
        connection = self.connect_to_database()
        df = pd.read_sql(query, connection)
        self.close_connection(connection)
        return df

    def save_data_to_csv(self, data, filename):
        data.to_csv(filename, index=False)

    def extract_and_save_data(self, filename):
        data = self.query_and_return_pandas_dataframe("SELECT * FROM loan_payments")
        self.save_data_to_csv(data, filename)
