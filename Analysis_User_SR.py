import csv
import statistics
import matplotlib.pyplot as plt  # Can be omitted if not installed

# Read CSV data
data = []
with open("telecom_data.csv", mode="r") as file:
    reader = csv.reader(file)
    next(reader)  # Skip header
    for row in reader:
        data.append((int(row[0]), float(row[1])))

# Split into separate lists
user_counts, success_rates = zip(*data)


# Calculate basic statistics
mean_users = statistics.mean(user_counts)
mean_success = statistics.mean(success_rates)
corr = statistics.correlation(user_counts, success_rates)  # Only in Python 3.10+, alternative needed for 3.6

# Alternative correlation calculation (for Python 3.6)
def manual_correlation(x, y):
    mean_x, mean_y = statistics.mean(x), statistics.mean(y)
    numerator = sum((xi - mean_x) * (yi - mean_y) for xi, yi in zip(x, y))
    denominator = (sum((xi - mean_x) ** 2 for xi in x) * sum((yi - mean_y) ** 2 for yi in y)) ** 0.5
    return numerator / denominator if denominator else 0

corr = manual_correlation(user_counts, success_rates)

# Compute Z-scores for user counts
z_scores_users = [(x - mean_users) / std_dev_users for x in user_counts]

# Compute Z-scores for success rates
z_scores_success = [(y - mean_success) / std_dev_success for y in success_rates]

# Print first 5 Z-scores
print("First 5 Z-scores for User Count:", z_scores_users[:5])
print("First 5 Z-scores for Success Rate:", z_scores_success[:5])

# Print summary
print(f"Mean User Count: {mean_users}")
print(f"Mean Success Rate: {mean_success}%")
print(f"Correlation Coefficient: {corr:.3f} (Interpret: Close to ±1 → Strong relationship)")

