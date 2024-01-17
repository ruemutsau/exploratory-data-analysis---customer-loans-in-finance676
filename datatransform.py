import pandas as pd
...
The data's columns can be transformed using this class.
...
  class DataTransform:
    def __init__(self, DataFrame, column_name):
        self.DataFrame = DataFrame
        self.column_name = column_name
      def extract_integer_from_string(self):
        # Extract integers from the column
        self.DataFrame[self.column_name] = self.DataFrame[self.column_name].str.extract('(\d+)').astype('Int32')
        return self.DataFrame
def replace_string_text(self, DataFrame: pd.DataFrame, column_name: str, original_string: str, new_string: str)
DataFrame[column_name] = DataFrame[column_name].str.replace(original_string, new_string)
        return DataFrame

    def convert_string_to_date(self, DataFrame: pd.DataFrame, column_name: str)
 DataFrame[column_name] = pd.to_datetime(DataFrame[column_name], errors='coerce').dt.to_period('M')
        return DataFrame


  
