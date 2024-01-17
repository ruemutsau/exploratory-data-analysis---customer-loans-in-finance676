import numpy as np
import pandas as pd
from scipy import stats
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import RobustScaler
from sklearn.svm import SVC
from dataframeinfo import DataFrameInfo as info
from plotter import Plotter as plotter

np.random.seed(123) # To ensure reproducibility, the random seed is set to '123'.Here, 123 is the seed value that is used to initialize the random number generator.
Setting the seed value ensures that the same sequence of random numbers is generated every time the code is run, which is useful for debugging and testing purposes.

class DataFrameTransform:
  def remove_null_columns(self, DataFrame: pd.DataFrame, column_name):
       DataFrame.drop(column_name, axis=1, inplace=True)
        return DataFrame
  def remove_null_rows(self, DataFrame: pd.DataFrame, column_name):
        DataFrame.dropna(subset=column_name, inplace=True)
        return DataFrame
 def fill_median(self, DataFrame: pd.DataFrame, column_name):
        DataFrame[column_name].fillna(DataFrame[column_name].median(numeric_only=True), inplace=True)
        return DataFrame
 def fill_mean(self, DataFrame: pd.DataFrame, column_name):
            DataFrame[column_name].fillna(DataFrame[column_name].mean(numeric_only=True, skipna=True), inplace=True)
        return DataFrame
 def linear_regression_fill(self, DataFrame: pd.DataFrame, column_to_fill: str, training_features: list = None, score: bool = False, check_distribution: bool = False):
  if check_distribution == True:
            print(f'\n({column_to_fill}) Initial Distribution:\n')
            plotter.histogram(self, DataFrame, column_to_fill) # Plots histogram to display distribution before method is applied.

        if training_features == None: # no training features are provided.
            x = DataFrame.drop(info.get_null_columns(self, DataFrame), axis=1) # Only uses columns with no nulls for training.
        else:  # training features are provided.
            x = DataFrame[training_features] # Using provided list for training.
        y = DataFrame[column_to_fill] # Identify target column.
if check_distribution == True:
            print(f'\n({column_to_fill}) Final Distribution:\n')
            plotter.histogram(self, DataFrame, column_to_fill) # Plots histogram to display distribution after method is applied.

        if score == True:
            print(f'\nScore: {round(model.score(x_train, y_train),2)}') # Provides an accuracy score for the model (based on the training data) which is rounded to 2 d.p.

        return DataFrame


        # Encode string columns to numeric type to be compatible with model.
        object_columns = x.select_dtypes(include=['object']).columns.tolist() # creates a list by adding all columns with the data type "object."
        x[object_columns] = x[object_columns].astype('category') # sets the 'category' data type for each column in this list.
        x[object_columns] = x[object_columns].apply(lambda x: x.cat.codes) #creates numerical codes from these categories.

        # Encode date columns to numeric type to be compatible with model.
        date_columns = x.select_dtypes(include=['period[M]']).columns.tolist() # Adds all columns with 'period [M]' as their data type into a list.
        x[date_columns] = x[date_columns].astype('category') # Changes the data type of the columns in this list to 'category'.
        x[date_columns] = x[date_columns].apply(lambda x: x.cat.codes) # Converts these categories into numerical codes.

        # Data Split
        x_train = x[~y.isna()] # Training input data: all columns except target column where target column values are known (not null).
        y_train = y[~y.isna()] # Training output data: all non null (known) values in target column.

        x_test = x[y.isna()] # Testing input data: all columns except target column where target column values are not known (null).
        # This will be input into the model to impute null values.

        # Train Linear Regression Model:
        model = LinearRegression()
        model.fit(x_train, y_train)

        # Run model and impute null values with predicted values:
        prediction = model.predict(x_test)
        DataFrame[column_to_fill].loc[y.isna()] = prediction # Where values in target column are null, impute the model's predicted value.
        
 def support_vector_machine_fill(self, DataFrame: pd.DataFrame, column_to_fill: str, training_features: list = None, score: bool = False, check_distribution: bool = False):
         if check_distribution == True:
            initial_distribution = DataFrame[column_to_fill].value_counts(normalize=True) # Stores the normalized value count (distribution of data) into a variable.

        if training_features == None: # In the case no training features are provided.
            x = DataFrame.drop(info.get_null_columns(self, DataFrame), axis=1) # Only uses columns with no nulls for training.
        else: # In the case training features are provided.
            x = DataFrame[training_features] # Using provided list for training.
        y = DataFrame[column_to_fill]  # Identify target column.
if check_distribution == True:
            final_distribution = DataFrame[column_to_fill].value_counts(normalize=True) # Stores the normalized value count (distribution of data) after method into a variable.
            distribution_df = pd.DataFrame({'Before': round(initial_distribution, 3),'After': round(final_distribution, 3)}) # combines both the before and after normalised value counts into a dataframe, rounded to 3 d.p.
            print('Distribution: Normalised Value Count')
            print(distribution_df)
        
        if score == True:
            print(f'\nScore: {round(model.score(x_train, y_train),2)}') # Provides an accuracy score for the model (based on the training data) which is rounded to 2 d.p.
        
        return DataFrame
 def box_cox_transform(self, DataFrame: pd.DataFrame, column_name: str):
        boxcox_column = stats.boxcox(DataFrame[column_name])
        boxcox_column = pd.Series(boxcox_column[0])
        return boxcox_column

    def yeo_johnson_transform(self, DataFrame: pd.DataFrame, column_name: str):
        yeojohnson_column = stats.yeojohnson(DataFrame[column_name])
        yeojohnson_column = pd.Series(yeojohnson_column[0])
        return yeojohnson_column

    def drop_outlier_rows(self, DataFrame: pd.DataFrame, column_name: str, z_score_threshold: int):

        mean = np.mean(DataFrame[column_name]) # Identify the mean of the column.
        std = np.std(DataFrame[column_name]) # Identify the standard deviation of the column.
        z_scores = (DataFrame[column_name] - mean) / std # Identofy the 'z score' for each value in the column.
        abs_z_scores = pd.Series(abs(z_scores)) # Create a series with the absolute values of the 'z_score' stored.
        mask = abs_z_scores < z_score_threshold
        DataFrame = DataFrame[mask] # Only keep rows where the 'z score' is below the threshold.        
        return DataFrame
