recipes = []

n = int(input("How many recipes to add? "))

for i in range(n):
    name = input("Recipe name: ")
    difficulty = input("Difficulty (Easy/Medium/Hard): ")
    recipes.append({"name": name, "difficulty": difficulty})


# Sort alphabetically
for i in range(n):
    for j in range(n - i - 1):
        if recipes[j]["name"].lower() > recipes[j + 1]["name"].lower():
            temp = recipes[j]
            recipes[j] = recipes[j + 1]
            recipes[j + 1] = temp


print("\nAll Recipes (sorted):")
for recipe in recipes:
    print(recipe["name"], "-", recipe["difficulty"])


# Recursive search
def search(recipes, name, i=0):
    if i == len(recipes):
        return None

    if recipes[i]["name"].lower() == name.lower():
        return recipes[i]

    return search(recipes, name, i + 1)


name = input("\nSearch recipe: ")
result = search(recipes, name)

if result:
    print("Found:", result)
else:
    print("Recipe not found")