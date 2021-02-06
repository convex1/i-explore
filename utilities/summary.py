import pandas as pd


'''
Function to calculate average value of each column in the dataframe and return as a dictionary

:param dataframe: dataframe to consider
:param columns_list: list of columns to calculate mean for
'''


def get_average(dataframe, columns_list):

    average_dict = {}
    columns = []

    if len(columns) == 0:
        columns = columns_list
    else:
        columns = dataframe.columns

    for i in columns:
        average_dict[i] = dataframe[i].mean()

    return average_dict


'''
Function to calculate median value of each column in the dataframe and return as a dictionary

:param dataframe: dataframe to consider
:param columns_list: list of columns to calculate median for
'''


def get_median(dataframe, columns_list = []):

    median_dict = {}
    columns = []

    if len(columns) == 0:
        columns = columns_list
    else:
        columns = dataframe.columns

    for i in columns:
        median_dict[i] = dataframe[i].median()

    return median_dict

'''
Function to calculate mode value of each column in the dataframe and return as a dictionary

:param dataframe: dataframe to consider
:param columns_list: list of columns to calculate mode for
'''

def get_mode(dataframe, columns_list):

    mode_dict = {}
    columns = []

    if len(columns) == 0:
        columns = columns_list
    else:
        columns = dataframe.columns

    for i in columns:
        mode_dict[i] = dataframe[i].mode()

    return mode_dict