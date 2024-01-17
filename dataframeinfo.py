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
    
