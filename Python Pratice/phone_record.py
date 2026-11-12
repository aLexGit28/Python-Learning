import pandas as pd

# Creating sample device data
data = {
    'Device': ['Mobile', 'Mobile', 'Laptop', 'Tablet'],
    'Brand': ['Samsung', None, 'Dell', 'Apple'],
    'Price': [15500, None, 45000, 25500]
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)

# 1. Fill missing Brand values
df['Brand'] = df['Brand'].fillna(df['Brand'].mode()[0])

# 2. Fill missing Price values using device-wise median
df['Price'] = df['Price'].fillna(
    df.groupby('Device')['Price'].transform('median')
)

print("\nUpdated Data:")
print(df)

# 3. Count each type of device
device_count = df['Device'].value_counts()

print("\nDevice count:")
print(device_count)

# 4. Calculate average price per device
average_price = df.groupby('Device')['Price'].mean()

print("\nAverage price per device:")
print(average_price)