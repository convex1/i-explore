import pandas as pd


'''
Function to get count number of columns of each data type

:param dataframe: dataframe to consider
'''


def count_data_type_columns(dataframe):

    return dataframe.dtypes.value_counts()