import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error

data = pd.read_excel("/home/superuser/Desktop/Dataset.xlsx")
print(data.head())
print(data.isna().sum())

data['Date'] = pd.to_datetime(data['Date'])

data['Day'] = data['Date'].dt.day
data['Month'] = data['Date'].dt.month
data['Year'] = data['Date'].dt.year

data.drop(['Date'], axis=1, inplace=True)

temp_col = data.columns.to_list()
new_col = temp_col[:3] + temp_col[4:]
new_col.append(temp_col[3])
data = data.reindex(columns=new_col)

scaler = StandardScaler()
data_scaled = scaler.fit_transform(data)

x = data_scaled[:, :-1]  # All columns except the last one
y = data_scaled[:, -1]   # The last column

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.1, random_state=42)

model_linear = LinearRegression()
model_linear.fit(x_train, y_train)

y_pred_linear = model_linear.predict(x_test)

def calculate_accuracy(y_true, y_pred):
    errors = abs(y_true - y_pred)
    mape = 100 * np.mean(errors / y_true)
    accuracy = 100 - mape
    return accuracy

print("Linear Regression Accuracy:", calculate_accuracy(y_test, y_pred_linear))

model_rf = RandomForestRegressor(n_estimators=500, min_samples_split=3, random_state=42)
model_rf.fit(x_train, y_train)

y_pred_rf = model_rf.predict(x_test)

print("Random Forest Accuracy:", calculate_accuracy(y_test, y_pred_rf))

def print_metrics(y_true, y_pred):
    print("Mean Absolute Error:", mean_absolute_error(y_true, y_pred))
    print("Mean Squared Error:", mean_squared_error(y_true, y_pred))
    print("Root Mean Squared Error:", np.sqrt(mean_squared_error(y_true, y_pred)))

print("Linear Regression Metrics:")
print_metrics(y_test, y_pred_linear)

print("Random Forest Metrics:")
print_metrics(y_test, y_pred_rf)

plt.figure(figsize=(14, 7))

plt.subplot(1, 2, 1)
plt.scatter(y_test, y_pred_linear, alpha=0.5)
plt.xlabel('Actual')
plt.ylabel('Predicted')
plt.title('Linear Regression Predictions')

plt.subplot(1, 2, 2)
plt.scatter(y_test, y_pred_rf, alpha=0.5)
plt.xlabel('Actual')
plt.ylabel('Predicted')
plt.title('Random Forest Predictions')

plt.tight_layout()
plt.show()
