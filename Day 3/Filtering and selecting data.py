import pandas as pd

data = {
    'Name':['Alice','Bob', None, 'David'],
    'Age':[25, None, 35, 40],
    'City':['New York', 'Los angeles', 'San Francisco', None],
}

df = pd.DataFrame(data)
print(df)

adults = df[df['Age']>=35]
print(adults)

selected_columns = df[['Name', 'City']]
print(selected_columns)

selected_data = df.loc[df['Age'] > 30, ['Name', 'City']]
print(selected_data)

selected_data = df.iloc[1:3, [0,2]]
print(selected_data)
