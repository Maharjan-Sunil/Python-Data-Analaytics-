# import pandas as pd
# data =pd.read_csv("Data.csv", na_values=['.']) 
# print(data)

#to_csv for converting in to csv file via pandas

#to display the csv file size
# print(data.shape)

#to print the number of row
#print(data.head(0))

#print(len(data))
#print(data.columns)

# print(data['Name'][:2])
# import os
# print(os.listdir('.'))

#mode r+ w+ for both read and write
#mode wb means binary file

with open('./Data.csv', 'r') as f:
    for line in f.readlines():
        print(line)

