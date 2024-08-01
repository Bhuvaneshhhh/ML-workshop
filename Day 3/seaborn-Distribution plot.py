import seaborn as sns
import matplotlib.pyplot as plt

data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
sns.histplot(data, bins=4, kde=True)
plt.title("Histogram and KDE plot")
plt.show()