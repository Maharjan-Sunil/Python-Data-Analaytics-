import pandas as pd
data =pd.read_csv("Data.csv") 
#print(data)

#to display the csv file size
# print(data.shape)

#to print the number of row
#print(data.head(0))

#print(len(data))
#print(data.columns)

print(data['Name'][:2])