import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn import datasets
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import matplotlib.pyplot as plt

data = datasets.load_iris()
x = data.data
y = data.target

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0)

clf = SVC(kernel='linear', random_state=42)
clf.fit(x_train, y_train)

y_pred = clf.predict(x_test)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy: ", accuracy)

print('classification report: ')
print(classification_report(y_test, y_pred, target_names=data.target_names))

print('confusion matrix:')
print(confusion_matrix(y_test, y_pred))

def plot_decision_boundaries(x, y, model, title):
    h = .02
    x_min, x_max = x[:, 0].min() -1, x[:, 0].max() +1
    y_min, y_max = x[:, 1].min() -1, x[:, 1].max() +1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
    z = model.predict(np.c_[xx.ravel(), yy.ravel()])
    z = z.reshape(xx.shape)
    plt.contourf(xx, yy, z, cmap=plt.cm.coolwarm, alpha=0.8)
    plt.scatter(x[:, 0], x[:, 1], c=y, cmap=plt.cm.coolwarm, edgecolors='k')
    plt.xlabel('Feature 1')
    plt.ylabel('Feature 2')
    plt.title(title)
    plt.show()

x_reduced = x[:, :2]
x_train_reduced, x_test_reduced, y_train_reduced, y_test_reduced = train_test_split(x_reduced, y, test_size=0.3, random_state=42)

clf_reduced = SVC(kernel='linear', random_state=42)
clf_reduced.fit(x_train_reduced, y_train_reduced)
plot_decision_boundaries(x_test_reduced, y_test_reduced, clf_reduced, 'SVM Decision Boundaries (2D Features)')


