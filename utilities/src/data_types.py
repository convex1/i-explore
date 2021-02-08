import pandas as pd


'''
Function to get count number of columns of each data type

:param dataframe: dataframe to consider
'''

class dimensions_of_dataframe():

    def __init__(self, input_dataframe):
        self.dataframe = input_dataframe

    def count_data_type_columns(dataframe):

        return dataframe.dtypes.value_counts()