import json
import re
import pandas as pd


def extract_from_json(json_data):
    column_name = json_data['columnName']  # Stores name of the column to split
    split_size = int(json_data['Split_size'])  # Gives us the split size
    over_flow_strategy = json_data['overFlowStrategy']  # Stores the overFlowStrategy
    return [column_name, split_size, over_flow_strategy]

def delimiter(data):
    # Replacing the different Delimiters with an empty space
    data = data.str.replace('\t', ' ').str.replace('|', ' ')
    data = data.str.replace(',', ' ').str.replace('-', ' ')
    return data

def splitter(data_frame, json_data):
    # Storing the extracted values from json into variables
    column_name, split_size, over_flow_strategy = extract_from_json(json_data)
    # Saving original dataframe containing 'columnName' values
    column_before_split = data_frame[column_name]
    # Saving the dataframe with removed delimiter
    column_with_removed_delimiters = delimiter(data_frame[column_name])
    # Assigning the no. of rows and columns
    row, column = data_frame.shape
    # Separating the different elements using a comma using regular expression
    for i in range(row):
        column_with_removed_delimiters[i] = re.split(' ', column_with_removed_delimiters[i])

    # Removing the empty strings within a list
    for i in range(row):
        while "" in column_with_removed_delimiters[i]:
            column_with_removed_delimiters[i].remove("")

    # Removing the extra strings if overflowstrategy == 'ignore'
    if over_flow_strategy == 'ignore':
        for i in range(row):
            while len(column_with_removed_delimiters[i]) > split_size:
                column_with_removed_delimiters[i].pop()

    # Converting the list into a string with spaces
    for i in range(row):
        column_with_removed_delimiters[i] = " ".join(column_with_removed_delimiters[i])

    # Separating the lists into columns and storing it in dataframe 'column_after_split'
    for i in range(row):
        column_after_split = column_with_removed_delimiters.str.split(" ", n=split_size-1, expand=True)

    # Concatenating two dataframes and storing it in result
    result = pd.concat([column_before_split, column_after_split], axis=1)
    return result


if __name__ == '__main__':
    try:
        with open("input1.json", "r") as read_file:
            JSON_DATA = json.load(read_file)
    except:
        print("Json File is missing")
    try:
        DATAFRAME = pd.read_excel("df.xlsx")
        print(splitter(DATAFRAME, JSON_DATA))
    except:
        print("Panda Dataframe File is missing")
    