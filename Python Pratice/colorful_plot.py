import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# 1. Generate random height data using numpy
# Group A: average height = 50 inches, Group B: average height = 55 inches
np.random.seed(42)  # Ensures reproducible random numbers
group_a_heights = np.random.normal(loc=50, scale=3, size=100)
group_b_heights = np.random.normal(loc=55, scale=3, size=100)

# 2. Create a DataFrame combining both groups and adding a group column
df = pd.DataFrame({
    'Height': np.concatenate([group_a_heights, group_b_heights]),
    'Group': ['Group A'] * 100 + ['Group B'] * 100,
})

# 3. Create the figure and subplots using matplotlib.pyplot
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# 4. First plot: Density plot using the default color palette
sns.set_palette('deep')  # Reset to Seaborn's default color palette
sns.kdeplot(
    data=df,
    x='Height',
    hue='Group',
    fill=True,
    ax=axes[0],
    palette='deep',
)
axes[0].set_title('Height Distribution (Default Palette)')
axes[0].set_xlabel('Height (inches)')

# 5. Second plot: Set the palette to 'dark' using sns.set_palette('dark')
sns.set_palette('dark')
sns.kdeplot(
    data=df,
    x='Height',
    hue='Group',
    fill=True,
    ax=axes[1],
    palette='dark',
)
axes[1].set_title('Height Distribution (Dark Palette)')
axes[1].set_xlabel('Height (inches)')

# Display the plots cleanly
plt.tight_layout()
plt.show()
