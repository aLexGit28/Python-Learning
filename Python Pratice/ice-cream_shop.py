
import pandas as pd
import matplotlib.pyplot as plt

# Create a DataFrame
data = {
    "Temperature": [20, 22, 25, 28, 30, 32, 35],
    "Sales": [40, 50, 65, 80, 95, 110, 130]
}

df = pd.DataFrame(data)

# Store X-axis and Y-axis values
x = df["Temperature"]
y = df["Sales"]

# Plot the line graph
plt.plot(
    x,
    y,
    color=(0.2, 0.6, 0.8),
    marker="o",
    linewidth=2
)

# Add title and labels
plt.title("Temperature vs Ice-Cream Sales")
plt.xlabel("Temperature (°C)")
plt.ylabel("Ice-Cream Sales (Units)")

# Enable grid
plt.grid(True)

# Display the graph
plt.show()
