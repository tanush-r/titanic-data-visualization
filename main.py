import seaborn as sns
import matplotlib.pyplot as plt


# Set seaborn theme
sns.set_style('whitegrid')
# Load titanic dataframe
titanic = sns.load_dataset('titanic')
# Write titanic dataframe to xlsx file
titanic.to_excel('res\\titanic_dataset.xlsx', sheet_name='Sheet1')

# Joint Plot of fare vs age
sns.jointplot(x='fare', y='age', data=titanic)
plt.savefig("res\\1.png", dpi=200)
plt.clf()

# Histogram of fare
plt.hist(x="fare", data=titanic)
plt.savefig("res\\2.png", dpi=200)
plt.clf()

# Boxplot of class vs age
sns.boxplot(x="class", y="age", data=titanic, palette="rainbow")
plt.savefig("res\\3.png", dpi=200)
plt.clf()

# Swarm plot of class vs age
sns.swarmplot(x="class", y="age", data=titanic, palette="coolwarm")
plt.savefig("res\\4.png", dpi=200)
plt.clf()

# Count plot of sex
sns.countplot(x='sex', data=titanic)
plt.savefig("res\\5.png", dpi=200)
plt.clf()

# Heat Map of titanic dataframe
sns.heatmap(data=titanic.corr(), cmap="coolwarm")
plt.savefig("res\\6.png", dpi=200)
plt.clf()

# Facet Grid of age for different sex(histogram)
grid_plot = sns.FacetGrid(col='sex', data=titanic)
grid_plot.map(plt.hist, "age")
plt.savefig("res\\7.png", dpi=200)
plt.clf()


