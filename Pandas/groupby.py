import pandas as pd

df_data = pd.read_csv('../IO/Data.csv')
# group_by_name = df_data.groupby('Name')['Count'].sum()

#using agg
group_by_name = df_data.groupby('Name').agg({
    'Count': ['mean', 'count']
})
print(group_by_name)

#further filter in data
print(df_data['Address'].str.match('Dallu'))