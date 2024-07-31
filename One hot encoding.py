import pandas as pd
from sklearn.preprocessing import OneHotEncoder
data = {'Category':['A', 'B', 'A', 'C']}
df = pd.DataFrame(data)

one_hot_encoder = OneHotEncoder(sparse_output=False)
encoded = one_hot_encoder.fit_transform(df[['Category']])

encoded_df = pd.DataFrame(encoded, columns=one_hot_encoder.get_feature_names_out(['Category']))
df_one_hot_encoded = pd.concat([df, encoded_df], axis=1)
print(df_one_hot_encoded)