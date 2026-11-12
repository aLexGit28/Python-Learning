import pandas as pd

data = {
    "Name": ['Charmander', 'Bulbasur', 'Pikachu', 'Jigglypuff', 'Squirtle'],
    "Type": ['Fire', 'Grass/Poison', 'Electric', 'Water', 'Normal'],
    'Speed': [65, 50, 90, 20, 45]
}

df = pd.DataFrame(data)

print('Original Pokémon Data: ')
print(df)

sorted_df = df.sort_values(by='Speed', ascending=False)

print('\nPokèmon Data sorted according to their Speed stat in Descending Order: ')

print(sorted_df)