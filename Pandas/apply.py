import pandas as pd

def display_count(count):
    if(count > 2):
        return True
    else:
        return False

df_data = pd.read_csv('../IO/Data.csv')

#apply passsed the value as per df if group then send row but if series then element
Standard_data = df_data['Count'].apply(display_count)
df_data['Assert'] = Standard_data
print(df_data)


#fillna replace none to false
