# Smart Food Preference & Feedback Analyzer

# Take food items from the user
food_items = input("Enter food items ordered (Pizza/Burger/Salad): ").split()

# Take feedback from the user
feedback = input("Enter feedback (Poor/Average/Good/Excellent): ").split()


# --- Data Type Classification ---

print("\n--- Data Type Classification ---")

print("Food Items → Nominal Categorical Data")
print("Feedback Levels → Ordinal Categorical Data")


# --- Frequency Table ---

print("\n--- Frequency Table ---")

# Count food items
print("Pizza:", food_items.count("Pizza"), "orders")
print("Burger:", food_items.count("Burger"), "orders")
print("Salad:", food_items.count("Salad"), "orders")

print()

# Count feedback
print("Good:", feedback.count("Good"), "times")
print("Poor:", feedback.count("Poor"), "times")
print("Excellent:", feedback.count("Excellent"), "times")
print("Average:", feedback.count("Average"), "times")