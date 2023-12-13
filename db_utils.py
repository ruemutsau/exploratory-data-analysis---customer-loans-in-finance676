import pandas as pd
from sqlalchemy import create_engine
import yaml


# Extract the credentials from the yaml file into a dictionary.
def extract_credentials():


    with open('credentials.yaml', 'r') as file:
        return yaml.safe_load(file)

# Store the dictionary into a variable.
credentials: dict = extract_credentials()

# Creates class object to connect to RDS database and extract data.
class RDSDatabaseConnector():



    def __init__(self, credentials_dict: dict):

       
        
        self.credentials_dict = credentials_dict # when class is initiated it requires the credentials argument.

    # Initialises SQLAlchemy engine.
    def create_engine(self):
        
       
        self.engine = create_engine(f"postgresql+psycopg2://{self.credentials_dict['RDS_USER']}:{self.credentials_dict['RDS_PASSWORD']}@{self.credentials_dict['RDS_HOST']}:{self.credentials_dict['RDS_PORT']}/{self.credentials_dict['RDS_DATABASE']}")

    # Establishes a connection to the database and creates a pandas dataframe from the 'loan payments' table.
    def extract_loans_data(self):


        with self.engine.connect() as connection:
            self.loan_payments_df = pd.read_sql_table('loan_payments', self.engine)
            return self.loan_payments_df
    
# Writes the pandas dataframe into a csv file.
def save_data_to_csv(loans_df: pd.DataFrame):


    with open('loan_payments.csv', 'w') as file:
        loans_df.to_csv(file, encoding= 'utf-8', index= False)

if __name__ == '__main__':
    connector = RDSDatabaseConnector(credentials) # Instantiates the 'RDSDatabaseConnector' class using the .
    # Calling all defined methods:
    connector.create_engine() # Creates the sqlalchemy engine to establish connection.
    extracted_data_frame: pd.DataFrame = connector.extract_loans_data() # Extracts sql data to a pandas dataframe.
    save_data_to_csv(extracted_data_frame) # Writes the dataframe into a csv file.
