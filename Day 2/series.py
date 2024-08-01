import pandas as pd
data=[1, 2, 3, 4, 5]
series=pd.Series(data)
print(series)

data=[1, 2, 3, 4, 5]
index = ['a', 'b', 'c', 'd', 'e']
series=pd.Series(data, index=index)
print(series)