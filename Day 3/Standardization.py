import pandas as pd
from sklearn.preprocessing import StandardScaler

data = {
    'A':[1, 2, 3, 4],
    'B':[2, 3, 4, 5]
}

df= pd.DataFrame(data)

scalar = StandardScaler()
df_standardized = pd.DataFrame(scalar.fit_transform(df), columns=df.columns)
print(df_standardized)
