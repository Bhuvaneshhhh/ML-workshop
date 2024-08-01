import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

np.random.seed(0)
x = 2* np.random.rand(100, 1)
y = 4+3+x + np.random.rand(100, 1)

model = LinearRegression()
model.fit(x, y)

y_pred = model.predict(x)

plt.scatter(x, y, color='blue')
plt.plot(x, y_pred, color='red')
plt.xlabel('Independent Variables')
plt.ylabel('Dependent Variables')
plt.title('Linear Regression')
plt.show()