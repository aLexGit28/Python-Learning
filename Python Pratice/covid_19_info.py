import pandas as pd

df = pd.read_csv('covid_19_info.csv')

print(df.head())

#1. Find the total number of cases 
total_cases = df['Total Cases'].sum()
print('\nTotal no. of cases in India: ')
print(total_cases)

filtered_data = df[(df['Death Ratio']> 1) & (df['Population'] > 4000000)]


print('\nStates with death ratio more than 1 and population more than 4000000: ')
print(filtered_data['State/UTs'])

print('\n Statistical Description of Data: ')
print(df.describe())

print('\nInformation about Dataset: ')
print(df.info())