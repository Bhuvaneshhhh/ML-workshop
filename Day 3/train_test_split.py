from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

iris = load_iris()
x= iris.data
y= iris.target

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

print("Training features shape:", x_train.shape)
print("Test features shape:", x_test.shape)
print("Training labels shape:", y_train.shape)
print("Test labels shape:", y_test.shape)
