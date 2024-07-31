x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]
import seaborn as sns
import matplotlib.pyplot as plt
sns.lineplot(x=x, y=y)
plt.title("Line plot with seaborn")
plt.show()