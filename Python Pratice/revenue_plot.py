
import matplotlib.pyplot as plt
import seaborn as sns

# Monthly revenue data (in lakhs)
revenue = [45, 50, 55, 60, 65, 70, 75, 80, 85, 90]

# Create histogram with bell-shaped KDE curve
sns.histplot(revenue, bins=6, kde=True)

# Add title and labels
plt.title("Distribution of Company Revenue (in Lakhs)")
plt.xlabel("Monthly Revenue (Lakhs)")
plt.ylabel("Number of Months")

# Display the graph
plt.show()
