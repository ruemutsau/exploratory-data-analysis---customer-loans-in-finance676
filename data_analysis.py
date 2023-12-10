import pandas as pd

class DataTransform:
    def __init__(self, data):
        self.data = data
        
    def transform_column(self, column_name, transformation):
        self.data[column_name] = transformation(self.data[column_name])

  def convert_to_category(column):
    return pd.Categorical(column)

transformer = DataTransform(data)
transformer.transform_column('column_name', convert_to_category)
