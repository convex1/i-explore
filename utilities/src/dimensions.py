import pandas as pd
import numpy as np

class dimensions_of_dataframe():

    def __init__(self, input_dataframe):
        self.dataframe = input_dataframe

    '''
    Function to count total number of rows in a dataframe
    
    :param dataframe: dataframe to count
    '''

    def count_rows(self):

        return len(self.dataframe)

    '''
    Function to count total number of columns in a dataframe
    
    :param dataframe: dataframe to count
    '''

    def count_columns(self):

        return len(self.dataframe.columns)

    '''
    Function to count total number of values in a dataframe
    
    :param dataframe: dataframe to count
    '''

    def count_values(self):

        return self.dataframe.size

    def count_non_null_size(self):

        return self.dataframe.dropna()
