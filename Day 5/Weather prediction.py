import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from keras.models import Sequential
from keras.layers import Dense, LSTM, Dropout
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint
from tensorflow.keras.losses import MeanSquaredError
from tensorflow.keras.metrics import RootMeanSquaredError
from tensorflow.keras.optimizers import Adam

df = pd.read_csv('/home/superuser/PycharmProjects/pythonProject/.venv/lib/python3.11/seattle-weather.xls')
print(df.head())
training_set = df.iloc[:, 2:3].values
print(training_set)

def df_to_XY(training_set, window_size=10):
    X_train = []
    y_train = []
    for i in range(window_size, len(training_set)):
        X_train.append(training_set[i-window_size:i, 0])
        y_train.append(training_set[i, 0])
    X_train, y_train = np.array(X_train), np.array(y_train)
    return X_train, y_train

WINDOW = 10
X, y = df_to_XY(training_set, WINDOW)
print(len(X), len(y))

X_train = X[:800]
y_train = y[:800]
X_val = X[800:1000]
y_val = y[800:1000]
X_test = X[1000:]
y_test = y[1000:]

X_train = np.reshape(X_train, (X_train.shape[0], X_train.shape[1], 1))
X_val = np.reshape(X_val, (X_val.shape[0], X_val.shape[1], 1))
X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))

regressor = Sequential()
regressor.add(LSTM(units=50, return_sequences=True, input_shape=(X_train.shape[1], 1)))
regressor.add(Dropout(0.2))
regressor.add(LSTM(units=50, return_sequences=True))
regressor.add(Dropout(0.2))
regressor.add(LSTM(units=50, return_sequences=True))
regressor.add(Dropout(0.2))
regressor.add(LSTM(units=50))
regressor.add(Dropout(0.2))
regressor.add(Dense(units=1))
regressor.compile(optimizer='adam', loss='mean_squared_error')

history = regressor.fit(X_train, y_train, validation_data=(X_val, y_val), epochs=100, batch_size=32)
his = pd.DataFrame(history.history)
print(his.head())

print(his.columns)
history_loss = his[['loss', 'val_loss']]
fig, axes = plt.subplots(2, 1, figsize=(14, 8))
plt.subplot(2, 1, 1)
sns.lineplot(data=history_loss)
plt.show()