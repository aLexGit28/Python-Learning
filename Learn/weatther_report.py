import pandas as pd
import numpy as np
df = pd.read_csv('datasets/Weatherdataset.csv', na_values=['np.nan'])

# print(df.head())

# Display the original DataFrame
print("Original DataFrame:")
print(df)

# Check missing values
print("\nMissing values in the dataset:")
print(df.isnull().sum())

# Fill missing values with 0
df_zero = df.fillna(0)

print("\nDataFrame after filling missing values with 0:")
print(df_zero)

# Fill missing values with the previous month's value
df = df.ffill()

print("\nDataFrame after filling missing values with the value of the previous month:")
print(df)