import csv
import statistics
import math

# Read data from CSV file
data = []
with open("telecom_tps_latency.csv", mode="r") as file:
    reader = csv.reader(file)
    next(reader)  # Skip header row
    for row in reader:
        data.append((float(row[0]), float(row[1])))  # (TPS, Latency)

# Separate into two lists
tps_values, latency_values = zip(*data)

# Compute Mean (Average)
mean_tps = statistics.mean(tps_values)
mean_latency = statistics.mean(latency_values)

# Compute Standard Deviation
std_dev_tps = statistics.stdev(tps_values)
std_dev_latency = statistics.stdev(latency_values)

# Print results
print(f"Mean TPS: {mean_tps}")
print(f"Mean Latency: {mean_latency} ms")
print(f"Standard Deviation (TPS): {std_dev_tps}")
print(f"Standard Deviation (Latency): {std_dev_latency}")

# Compute Pearson Correlation Coefficient manually
def pearson_correlation(x, y):
    mean_x, mean_y = statistics.mean(x), statistics.mean(y)
    numerator = sum((xi - mean_x) * (yi - mean_y) for xi, yi in zip(x, y))
    denominator = math.sqrt(sum((xi - mean_x) ** 2 for xi in x) * sum((yi - mean_y) ** 2 for yi in y))
    return numerator / denominator if denominator else 0

# Compute correlation
correlation = pearson_correlation(tps_values, latency_values)

# Print Correlation
print(f"Pearson Correlation Coefficient: {correlation:.3f}")

# Compute Z-scores for TPS
z_scores_tps = [(x - mean_tps) / std_dev_tps for x in tps_values]

# Compute Z-scores for Latency
z_scores_latency = [(y - mean_latency) / std_dev_latency for y in latency_values]

# Print first 5 Z-scores
print("First 5 Z-scores for TPS:", z_scores_tps[:5])
print("First 5 Z-scores for Latency:", z_scores_latency[:5])
