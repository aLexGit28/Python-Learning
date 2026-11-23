
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read CSV file
df = pd.read_csv("Python Pratice/test scores.csv")

# Set plot style
sns.set_style("whitegrid")

# Create multiple subplots
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# Get all subjects
subjects = df["Subject"].unique()

# Loop through each subject
for i in range(len(subjects)):

    subject = subjects[i]

    # Filter scores for current subject
    scores = df[df["Subject"] == subject]["Scores"]

    # Calculate mean and median
    mean_score = scores.mean()
    median_score = scores.median()

    # Create histogram
    sns.histplot(scores, bins=5, ax=axes[i], color="skyblue")

    # Add mean and median vertical lines
    axes[i].axvline(mean_score, color="red",
                    linestyle="--", label="Mean")

    axes[i].axvline(median_score, color="green",
                    linestyle="-.", label="Median")

    # Add title and labels
    axes[i].set_title(subject + " Score Distribution")
    axes[i].set_xlabel("Scores")
    axes[i].set_ylabel("Frequency")

    # Display legend
    axes[i].legend()

# Adjust spacing
plt.tight_layout()

# Display plots
plt.show()
