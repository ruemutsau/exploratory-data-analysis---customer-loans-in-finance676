import pandas as pd

class DataFrameInfo:
   def describe_dtypes(self, DataFrame: pd.DataFrame, column_name: str = None)
       if column_name is not None: # In the case that a column name IS provided.
            if column_name not in DataFrame.columns: # In the case the provided column_name is NOT in the DataFrame.
                raise ValueError(f"Column '{column_name}' not found in the dataframe.")
            return DataFrame[column_name].dtypes
        else: 
            return DataFrame.dtypes
           
   def median(self, DataFrame: pd.DataFrame, column_name: str = None)
    if column_name is not None:
            if column_name not in DataFrame.columns:
                raise ValueError(f"Column '{column_name}' not found in the dataframe.") 
            return DataFrame[column_name].median(numeric_only=True) 
        else:
            return DataFrame.median(numeric_only=True)
           
    def standard_deviation(self, DataFrame: pd.DataFrame, column_name: str = None):
        if column_name is not None:
            if column_name not in DataFrame.columns:
                raise ValueError(f"Column '{column_name}' not found in the dataframe.") 
            return DataFrame[column_name].std(skipna=True, numeric_only=True)
        else: 
            return DataFrame.std(skipna=True, numeric_only=True)

def mean(self, DataFrame: pd.DataFrame, column_name: str = None): 
        if column_name is not None: 
            if column_name not in DataFrame.columns:
                raise ValueError(f"Column '{column_name}' not found in the dataframe.")
            return DataFrame[column_name].mean(skipna=True, numeric_only=True)
        else: 
            return DataFrame.mean(skipna=True, numeric_only=True)
 def count_distinct(self, DataFrame: pd.DataFrame, column_name: str):
        return len(DataFrame[column_name].unique())

def shape(self, DataFrame: pd.DataFrame):
        print(f'The DataFrame has {DataFrame.shape[1]} columns and {DataFrame.shape[0]} rows.')
        return DataFrame.shape
   
def null_count(self, DataFrame: pd.DataFrame, column_name: str = None):
        if column_name is not None: 
            if column_name not in DataFrame.columns:
                raise ValueError(f"Column '{column_name}' not found in the dataframe.")
            return DataFrame[column_name].isna().sum() 
        else: # In the case a column name IS NOT provided.
            return DataFrame.isna().sum() 

 def null_percentage(self, DataFrame: pd.DataFrame, column_name: str = None):
        if column_name is not None: 
            if column_name not in DataFrame.columns:
                raise ValueError(f"Column '{column_name}' not found in the dataframe.")
            percentage = (DataFrame[column_name].isna().sum())/(len(DataFrame[column_name]))*100 
        else: # just in case there is no column provided
            percentage = (DataFrame.isna().sum())/(len(DataFrame))*100  
            return percentage
           
 def get_null_columns(self, DataFrame: pd.DataFrame, print: bool = False):
        columns_with_null = list(DataFrame.columns[list(DataFrameInfo.null_count(self, DataFrame=DataFrame)>0)]) # Creating a list of columns that contain null values.
        if print == True:
            for col in columns_with_null:
                print(f'{col}: {round(DataFrameInfo.null_percentage(self, DataFrame=DataFrame, column_name=col),1)} %')
        return columns_with_null
    
def identify_conditional_null_columns(self, DataFrame: pd.DataFrame, comparison_operator: str, null_percentage_condition: int):
        columns = []
        for col in DataFrame.columns
            if '>' in comparison_operator and '<' not in comparison_operator
                if DataFrameInfo.null_percentage(self, DataFrame=DataFrame, column_name=col) > null_percentage_condition: # if the given integer is greater than the percentage of nulls in the column.
                    columns.append(col) # Add column to list.
            elif '<' in comparison_operator and '>' not in comparison_operator:
                if DataFrameInfo.null_percentage(self, DataFrame=DataFrame, column_name=col) < null_percentage_condition and DataFrameInfo.null_percentage(self, DataFrame=DataFrame, column_name=col) > 0: # If percentage of nulls in column is less than specified integer but greater than 0.
                        columns.append(col) 
            else:
                raise ValueError(f"'{comparison_operator}' is not a comparison operator please input either '>' or '<'.")
        return columns
   
    def get_numeric_columns(self, DataFrame: pd.DataFrame):
        numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64'] # List of numeric datatypes in string format.
        numeric_columns = []
        for column in DataFrame.columns: # For each column in the dataframe.
            if DataFrame[column].dtypes in numerics: # If the columns datatype is numeric.
                numeric_columns.append(column) # Add column to list.
        return numeric_columns

    def get_skewed_columns(self, DataFrame: pd.DataFrame, threshold: int):
        numerics_columns = DataFrameInfo.get_numeric_columns(self, DataFrame) # Call 'DataFrameInfo.get_numeric_columns()' method to get list of numeric columns.
        skewed_columns = [] # Empty list.
        for column in numerics_columns: # For each numeric column in the dataframe.
            if abs(DataFrame[column].skew()) >= threshold: # If the absolute value of the skewness of column is greater than or equal to the threshold.
                skewed_columns.append(column) # Add column to list.
        return skewed_columns
       
   def get_skewness(self, DataFrame: pd.DataFrame, column_names: list):
        for column in column_names:
            print(f'{column}: {round(DataFrame[column].skew(),2)}') # Print column name and skewness rounded to 2 d.p.
            skewness[column] = DataFrame[column].skew() # Add column and its skewness to dictionary.
        return skewness
    
    def calculate_column_percentage(self, DataFrame: pd.DataFrame, target_column_name: str, total_column_name: str):
        target_column_sum = DataFrame[target_column_name].sum() # Sum of values in target column.
        total_column_sum = DataFrame[total_column_name].sum() # Sum of values in total column.
        percentage = (target_column_sum / total_column_sum) * 100 # Calculate of target value over total value.
        return percentage

    def calculate_percentage(self, target, total):
        percentage = (target/total)*100
        return percentage
    
    def calculate_total_collections_over_period(self, DataFrame: pd.DataFrame, period: int):
        collections_df = DataFrame.copy()
        final_payment_date = collections_df['last_payment_date'].max()
       
    def calculate_term_end(row): # Function used to calculate term end according to term length and issue date.
            if row['term'] == '36 months': # In 36 month terms
                return row['issue_date'] + 36 # Term end will be 36 months after issue date.
            elif row['term'] == '60 months': # In 60 month terms
                return row['issue_date'] + 60 # Term end will be 60 months after issue date.

 def calculate_collections(row): # Define function to sum collections over projection period.
            if row['mths_left'] >= period: # If months left in term are equal to or greater than projection period.
                return row['instalment'] * period #  projection period * Installments.
            elif row['mths_left'] < period: # If less than projection period months left in term.
                return row['instalment'] * row['mths_left'] # number of months left * installments.

        collections_df['collections_over_period'] = collections_df.apply(calculate_collections, axis=1)
        total_loan = collections_df['loan_amount'].sum()
        total_loan_left = total_loan - collections_df['total_payment'].sum()

        return {'total_collections': collection_sum, 'total_loan': total_loan, 'total_loan_outstanding': total_loan_left}

 def monthly_collection_percentage_projections(self, DataFrame: pd.DataFrame, period: int):
        # Generate empty lists that will contain percentages of collection out of total and outstanding loan.
        percentage_of_loan = []
        percentage_of_outstanding = []

        for month in range(1, (period+1)): # For each month in 1-6.
            projections = DataFrameInfo.calculate_total_collections_over_period(self, DataFrame, period=month) 
            total_collections = projections['total_collections'] # Extract total collection amount from dictionary.
            total_loan = projections['total_loan'] # Extract total loan amount from dictionary.
            total_loan_outstanding = projections['total_loan_outstanding'] # Extract total loan amount outstanding from dictionary.
            
            percent_total_loan = DataFrameInfo.calculate_percentage(self, total_collections, total_loan) # Calculate percentage of collections out of total loan.
            percent_outstanding_loan = DataFrameInfo.calculate_percentage(self, total_collections, total_loan_outstanding) # Calculate percentage of collections out of outstanding loan.

            # Add percentages to lists.
            percentage_of_loan.append(percent_total_loan)
            percentage_of_outstanding.append(percent_outstanding_loan)
        
        return {'total_loan_percent': percentage_of_loan, 'outstanding_loan_percent': percentage_of_outstanding}
    
    def count_value_in_column(self, DataFrame: pd.DataFrame, column_name: str, value):
        return len(DataFrame[DataFrame[column_name]==value]) 
       
    def revenue_lost_by_month(self, DataFrame: pd.DataFrame):
        df = DataFrame.copy() 
        df['term_completed'] = (df['last_payment_date'] - df['issue_date'])
        df['term_completed'] = df['term_completed'].apply(lambda x: x.n) # Converting the row into an integer.

    def calculate_term_remaining(row): # Function used to calculate months remaining in term for each row.
            if row['term'] == '36 months': # In 36 month terms
                return 36 - row['term_completed'] # Term remaining is term length - how much of term was completed.
            elif row['term'] == '60 months': # In 60 month terms
                return 60 - row['term_completed'] # Term remaining is term length - how much of term was completed.

        df['term_left'] = df.apply(calculate_term_remaining, axis=1) # Applying function to calculate term left for each loan.
        
        revenue_lost = [] # Empty list
        cumulative_revenue_lost = 0
        for month in range(1, (df['term_left'].max()+1)): # For each month in the maximum number of months left in any term.
            df = df[df['term_left']>0] # Filter out any terms which have no months left.
            cumulative_revenue_lost += df['instalment'].sum() # Cumulatively sum the total number of monthly instalments.
            revenue_lost.append(cumulative_revenue_lost) # Add this cumulative sum to list of revenue projected to be lost.
            df['term_left'] = df['term_left'] - 1 # Take away one from the number of terms left.
        
        return revenue_lost
 def calculate_total_expected_revenue(self, DataFrame: pd.DataFrame):
       def calculate_total_revenue(row): # Function used to calculate total expected revenue for each loan.
            if row['term'] == '36 months': # In 36 month terms
                return 36 * row['instalment'] # Number of instalments * value of instalments = Total expected revenue.
            elif row['term'] == '60 months': # In 60 month terms
                return 60 * row['instalment'] # Number of instalments * value of instalments = Total expected revenue.

        DataFrame['total_revenue'] = DataFrame.apply(calculate_total_revenue, axis=1)
        total_expected_revenue = DataFrame['total_revenue'].sum()

        return total_expected_revenue

    

    
