import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor


data = pd.read_excel("/home/superuser/Desktop/Dataset.xlsx")
data.head()
data.isna().sum()

data['Date'] = pd.to_datetime(data['Date'])

data['Date'].dt.year.unique()

data['Day'] = data['Date'].dt.day
data['Month'] = data['Date'].dt.month
data['Year'] = data['Date'].dt.year

data.head()

data.drop(['Date'], axis = 1, inplace = True)
data.head()

temp_col = data.columns.to_list()

new_col = temp_col[:3] + temp_col[4:]
new_col.append(temp_col[3])

data = data.reindex(columns = new_col)
data.head()

scaler = StandardScaler()
data = scaler.fit_transform(data)

data[0]

x = data[:, :-1]
y = data[:, -1]
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.1, random_state = 42)



model = LinearRegression()
model.fit(x_train, y_train)


y_pred = model.predict(x_test)


def accuracy(y_true, y_pred):
    errors = abs(y_true - y_pred)
    mape = 100 * np.mean(errors/y_true)
    accuracy = 100 - mape
    return accuracy

accuracy(y_test, y_pred)


model_random_forest = RandomForestRegressor(n_estimators = 500, min_samples_split = 3)
model_random_forest.fit(x_train, y_train)

pred_rf = model_random_forest.predict(x_test)



print(accuracy(y_test, pred_rf))