x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]
import seaborn as sns
import matplotlib.pyplot as plt
categories = ['A', 'B', 'C', 'D']
values = [4, 7, 1, 8]
sns.lineplot(x=categories, y=values)
plt.title("scatter plot with seaborn")
plt.show()