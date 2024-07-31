import pandas as pd
df=pd.read_csv('data.csv')
print(df)
df=pd.read_excel('data.xlsx',sheet_name='Sheet1')
print(df)
df=pd.read_json('data.json')
print(df)

import sqlite3
conn = sqlite3.connect('database.db')
df=pd.read_sql_query('SELECT * FROM table_name', conn)
print(df)
#Exporting the data to csv
df.to_csv('output.csv',index=False)
df.to_excel('output.xlsx',sheet_name='Sheet1',index=False)
df.to_json('output.json')
#exporting data to a sql databases
conn=sqlite3.connect('database.db')
df.to_sql('table_name',conn,if_exists='replace',index=False)