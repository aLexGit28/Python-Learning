
# Pocket Money Tracker

# Items bought this month
items = ["ice cream", "comic", "stickers"]
costs = [60, 150, 40]

# Total money spent
total_spent = sum(costs)
print("You spent ₹", total_spent, "this month.")

# Biggest expense
biggest_cost = max(costs)
biggest_index = costs.index(biggest_cost)

print(f"Biggest expense: {items[biggest_index]} - ₹{biggest_cost}")

# Cheapest expense
cheapest_cost = min(costs)
cheapest_index = costs.index(cheapest_cost)

print(f"Cheapest expense: {items[cheapest_index]} - ₹{cheapest_cost}")

# Print receipt
print("\n----- YOUR RECEIPT -----")

for item, cost in zip(items, costs):
    print(f"{item}: ₹{cost}")

# Weekly pocket money
weekly_money = [200, 250, 150, 300]

total_pocket_money = sum(weekly_money)
average_money = total_pocket_money / len(weekly_money)

print("\nTotal pocket money: ₹", total_pocket_money)
print(f"Average pocket money per week: ₹{average_money}")

# Money left over
money_left = total_pocket_money - total_spent
print(f"Money left over: ₹{money_left}")

# Saving goals
saving_goals = {
    "headphones": 1200,
    "school bag": 800,
    "video game": 1500
}

# Choose a saving goal
goal = "headphones"
goal_price = saving_goals[goal]
more_money_needed = goal_price - money_left

print(f"\nSaving goal: {goal}")
print(f"Price: ₹{goal_price}")
print(f"More money needed: ₹{max(0, more_money_needed)}")

# Money-saving tip
money_tip = "Save a little money every week."

print("\nMoney Tip of the Month:")
print(money_tip)

# Show-off bonus: List comprehension
big_spends = [cost for cost in costs if cost > 50]

print("\nBig Spends:", big_spends)
