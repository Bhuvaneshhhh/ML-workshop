import pandas as pd
data = {
    'Name':['Alice','Bob', None, 'David'],
    'Age':[25, None, 35, 40],
    'City':['New York', 'Los angeles', 'San Francisco', None],
}

df = pd.DataFrame(data)
print(df)

df_renamed = df.rename(columns={'Name': 'Full Name', 'Age': 'Years'})
print(df_renamed)

df.columns = ['Full Name', 'Years', 'Location']
print(df)