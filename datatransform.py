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
        self.DataFrame[self.column_name] = self.DataFrame[self.column_name].str.extract('(\d+)').astype(int)
        return self.DataFrame



  
