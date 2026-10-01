import statistics

ratings = input("Enter product ratings (1-5) separated by space: ")

ratings = [int(rating) for rating in ratings.split()]

mean = statistics.mean(ratings)
median = statistics.median(ratings)
mode = statistics.mode(ratings)
std_dev = statistics.stdev(ratings)

q1 = statistics.quantiles(ratings, n=4)[0]
q2 = median
q3 = statistics.quantiles(ratings, n=4)[2]

iqr = q3 - q1

above_average = []
below_average = []

for rating in ratings:
    if rating > mean:
        above_average.append(rating)
    elif rating < mean:
        below_average.append(rating)

print("\n--- Analysis Results ---")
print("Mean Rating:", mean)
print("Median Rating:", median)
print("Mode Rating:", mode)
print("Standard Deviation:", round(std_dev, 3))
print("Q1:", q1, "Q2 (Median):", q2, "Q3:", q3)
print("Interquartile Range (IQR):", iqr)
print("Ratings above average:", above_average)
print("Ratings below average:", below_average)