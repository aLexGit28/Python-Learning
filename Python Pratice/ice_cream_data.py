import pandas as pd

# Step 1: Read both CSV files
sales = pd.read_csv("Data of sales.csv")
expenses = pd.read_csv("Data of expenses..csv")

# Step 2: Merge DataFrames using Days
df = pd.merge(sales, expenses, on="Days")

print("Merged DataFrame:")
print(df)

# Step 3: Update Wednesday's Cups Sold
df.loc[df["Days"] == "Wednesday", "Cups Sold"] = 55

# Step 4: Remove Cups Sold column
df.drop("Cups Sold", axis=1, inplace=True)

# Step 5: Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Fill missing values with 0
df.fillna(0, inplace=True)

# Step 6: Statistical summary
print("\nStatistical Summary:")
print(df.describe())

# Display DataFrame information
print("\nDataFrame Information:")
df.info()

# Step 7: Print final DataFrame
print("\nFinal DataFrame:")
print(df)
