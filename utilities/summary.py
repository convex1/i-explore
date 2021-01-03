import pandas as pd


'''
Function to calculate average value of each column in the dataframe

:param dataframe: dataframe to consider
'''


def get_average(dataframe):

    average_list = []

    for i in dataframe.columns:
        average_list.append(dataframe[i].mean())

    return average_list