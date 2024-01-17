import pandas as pd

class DataFrameInfo:
   def describe_dtypes(self, DataFrame: pd.DataFrame, column_name: str = None)
       if column_name is not None: # In the case that a column name IS provided.
            if column_name not in DataFrame.columns: # In the case the provided column_name is NOT in the DataFrame.
                raise ValueError(f"Column '{column_name}' not found in the dataframe.")
            return DataFrame[column_name].dtypes
        else: 
            return DataFrame.dtypes
