import pandas as pd

df_data = pd.read_csv('../IO/Data.csv')
df_data1 = pd.read_csv('../IO/Data1.csv')

#4 types of join (inner,outer,left & right)
merge_data = df_data.merge(df_data1, on = ['Name'])

#left 
merge_data_left = df_data.merge(df_data1, on =['Name'], how = 'left')
print(merge_data_left)