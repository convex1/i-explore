import pandas as pd


'''
Function to calculate average value of each column in the dataframe and return as a dictionary

:param dataframe: dataframe to consider
:param columns_list: list of columns to calculate mean for
'''

class summary_of_dataframe():

    def __init__(self, input_dataframe):
        self.dataframe = input_dataframe

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

    '''
    Function to calculate variance of each column in the dataframe and return as a dictionary
    
    :param dataframe: dataframe to consider
    :param columns_list: list of columns to calculate range for
    '''

    def get_variance(dataframe, columns_list):

        range_dict = {}
        columns = []

        if len(columns) == 0:
            columns = columns_list
        else:
            columns = dataframe.columns

        for i in columns:
            range_dict[i] = dataframe[i].var()

        return range_dict

    '''
    Function to calculate range value of each column in the dataframe and return as a dictionary
    
    :param dataframe: dataframe to consider
    :param columns_list: list of columns to calculate range for
    '''

    def get_range(dataframe, columns_list):

        range_dict = {}
        columns = []

        if len(columns) == 0:
            columns = columns_list
        else:
            columns = dataframe.columns

        for i in columns:
            range_dict[i] = dataframe[i].max() - dataframe[i].min()

        return range_dict