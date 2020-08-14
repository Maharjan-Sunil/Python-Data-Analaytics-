import pandas as pd

#to set the header for the data
df_data = pd.read_csv('../IO/Data.csv', names=['Name','Address','Star'], header=None)
print(df_data)

#set index from cols & also can set multiple index 
#inplace override the data frame
# df_data.set_index('Name', inplace=True)
# print(df_data)

#sort value and indexing in data frame
# def sort_by_address(data_fram):
#     sorted_address = data_fram.sort_values('Address')
#     return [((sorted_address.loc[index,'Name'],sorted_address.loc[index,'Star'])) for index in sorted_address.index][:2]

#to find the highest value in data frame according to column name
# def get_name_with_highest_star(data_frame):
#     print(data_frame.nlargest(2,'Star'))

# get_name_with_highest_star(df_data)
# data = sort_by_address(df_data)
# print(data)

#to get high value in index 
group_by_df = df_data.groupby('Address')['Star'].sum()
print(group_by_df.loc[group_by_df.idxmax()])


#drop duplicates row
# unique_df = df_data.drop_duplicates(subset='Name', keep='first')
# print(unique_df)