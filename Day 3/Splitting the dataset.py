import pandas as pd
from sklearn.model_selection import train_test_split

data = {
    'Feature1':[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Feature2':[11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
    'Target':[0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
}


df = pd.DataFrame(data)

x= df[['Feature1', 'Feature2']]
y= df['Target']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
print("Training features:\n", x_train)
print("Test features:\n", x_test)
print("Training labels:\n", y_train)
print("Test labels:\n", y_test)
