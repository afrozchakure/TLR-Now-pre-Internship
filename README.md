# TLR-Now-pre-Internship


# Libraries Used :

1. json - Used to load json file. 
2. re - Used for separating different elements in the  DataFrame using a comma. 
3. pandas - Used to load .xlxs file as well as perform operations on dataframe

# Functions defined :

1. extract_from_json(json_data) : This functions has been used to extract the variable names from the json_data.

2. delimiter(data) : The delimiter() function replaces the different delimiters with empty spaces in the string. It returns a dataframe with delimiters removed.

3. splitter(data_frame, json_data) : It takes the dataframe and json_data as input. It makes call to the extract_from_json() and delimiter() functions. 
Here the dataframe returned by the delimiter() is further processed to remove the empty strings within it. 
The over_flow_strategy is checked to remove any extra elements when over_flow_strategy == 'ignore'. 
Further the list within the DataFrame is converted into a string with spaces, which is then splitted into a number of columns specified by the split_size. After this, the Column before the split and the columns generated from the original column are concatenated to give the required DataFrame. 

The splitter() function is called from '__main__' with proper try-except block to check whether the files are 'present' or 'missing'

# Files for sample output:
df.xlxs | input1.json | input2.json
