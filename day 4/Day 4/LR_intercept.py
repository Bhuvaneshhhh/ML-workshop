import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

square_footage = np.array([1500, 1600, 1700, 1800, 1900, 2000]).reshape(-1,1)
prices = np.array([300000, 320000, 340000, 360000, 380000, 400000])

model = LinearRegression()
model.fit(square_footage, prices)

predicted_prices = model.predict(square_footage)

plt.scatter(square_footage, prices, color='blue', label='Actual Prices')
plt.plot(square_footage, predicted_prices, color='red', label='Predicted Prices')
plt.xlabel('Square Footage')
plt.ylabel('Prices')
plt.title('Linear Regression')
plt.legend()
plt.show()

print(f'Intercept: {model.intercept_}')
print(f'slope: {model.coef_[0]}')