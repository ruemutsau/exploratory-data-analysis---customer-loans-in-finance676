import pandas as pd
from sqlalchemy import create_engine
import yaml

def extract_credentials():


    with open('credentials.yaml', 'r') as file:
        return yaml.safe_load(file)

credentials: dict = extract_credentials()

# creates a class object to retrieve data from an RDS database connection.
class RDSDatabaseConnector():



    def __init__(self, credentials_dict: dict):

       
        
        self.credentials_dict = credentials_dict # when class is initiated it requires the credentials argument.

    def create_engine(self):
        
       
        self.engine = create_engine(f"postgresql+psycopg2://{self.credentials_dict['RDS_USER']}:{self.credentials_dict['RDS_PASSWORD']}@{self.credentials_dict['RDS_HOST']}:{self.credentials_dict['RDS_PORT']}/{self.credentials_dict['RDS_DATABASE']}")

    # connects to the database and uses the 'loan payments' table to construct a pandas dataframe.
    def extract_loans_data(self):


        with self.engine.connect() as connection:
            self.loan_payments_df = pd.read_sql_table('loan_payments', self.engine)
            return self.loan_payments_df
  
def save_data_to_csv(loans_df: pd.DataFrame):


    with open('loan_payments.csv', 'w') as file:
        loans_df.to_csv(file, encoding= 'utf-8', index= False)

if __name__ == '__main__':
    connector = RDSDatabaseConnector(credentials) 
    connector.create_engine()
    extracted_data_frame: pd.DataFrame = connector.extract_loans_data()
    save_data_to_csv(extracted_data_frame) 
