import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

iris = load_iris()
x = iris.data
y = iris.target

df = pd.DataFrame(data = x, columns=iris.feature_names)
df['target'] = y

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
print("Training features shape:", x_train.shape)
print("Testing features shape: ", x_test.shape)
print("Training labels shape:", y_train.shape)
print("Testing labels shape:", y_test.shape)

scalar = StandardScaler()
X_train = scalar.fit_transform(x_train)
X_test = scalar.transform(x_test)

model = logistic_regression(random_state=42)
model.fit(x_train_scaled, y_train)
y_pred = model.predict(x_test_scaled)

accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred, target_names=iris.target_names)

print(f'Accuracy: {accuracy}')
print(f'Report: {report}')
