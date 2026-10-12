import pandas as pd

# Create a Pandas Series
games = pd.Series({
    'Alice': 'Monopoly',
    'Bob': 'Settlers of Catan',
    'Charlie': 'Ticket to Ride',
    'David': 'Scrabble',
    'Emma': 'Codenames'
})

# Display the original dataset
print("Before update:")
print(games)

# Update the favorite board games
games['Alice'] = 'Carcassonne'
games['Bob'] = 'Pandemic'
games['Charlie'] = 'Azul'
games['David'] = 'Chess'
games['Emma'] = 'Risk'

print("\nFriends' favorite board games have been updated successfully.")

# Display the updated dataset
print("\nAfter update:")
print(games)

# Function to access the first and last elements using slicing
def access_games(s):
    first_game = s[:1]
    last_game = s[-1:]

    print("\nFirst game in the list:", first_game)
    print("Last game in the list:", last_game)

# Call the function
access_games(games)