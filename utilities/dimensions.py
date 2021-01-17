import pandas as pd
import numpy as np


'''
Function to count total number of rows in a dataframe

:param dataframe: dataframe to count
'''

def count_rows(dataframe):

    return len(dataframe)

'''
Function to count total number of columns in a dataframe

:param dataframe: dataframe to count
'''

def count_columns(dataframe):

    return len(dataframe.columns)

'''
Function to count total number of values in a dataframe

:param dataframe: dataframe to count
'''

def count_values(dataframe):

    return dataframe.shape