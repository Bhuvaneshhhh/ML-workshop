mport pandas as pd
from sklearn.preprocessing import MinMaxScaler

data = {
    'A':[1, 2, 3, 4],
    'B':[2, 3, 4, 5]
}

df= pd.DataFrame(data)
scaler = MinMaxScaler()
df_normalized = pd.DataFrame(scaler.fit_transform(df), columns=df.columns)
print(df_normalized)

