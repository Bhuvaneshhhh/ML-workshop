import pandas as pd
from sklearn.impute import SimpleImputer

data = {
    'A':[1, 2, None, 4],
    'B':[None, 2, 3, 4],
    'C':[1, None, 3, 4],
}

df = pd.DataFrame(data)
imputer = SimpleImputer(strategy='mean')
df_imputes = pd.DataFrame(imputer.fit_transform(df), columns=df.columns)
print(df_imputes)

