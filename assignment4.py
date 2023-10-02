import numpy as np
import datetime

data = [
    11, 14, 15, 15, 16, 16, 17, 18, 19, 21, 25, 36,
    12, 14, 15, 15, 16, 16, 17, 18, 19, 21, 25, 39,
    13, 14, 15, 15, 16, 17, 17, 18, 20, 22, 26, 43,
    13, 14, 15, 15, 16, 17, 17, 18, 20, 22, 26, 46,
    13, 14, 15, 16, 16, 17, 17, 18, 20, 22, 27, 50,
    13, 14, 15, 16, 16, 17, 17, 19, 20, 23, 27, 54,
    13, 14, 15, 16, 16, 17, 18, 19, 20, 23, 29, 59,
    13, 15, 15, 16, 16, 17, 18, 19, 20, 23, 30, 67,
    14, 15, 15, 16, 16, 17, 18, 19, 21, 24, 31,
    14, 15, 15, 16, 16, 17, 18, 19, 21, 24, 34
]

# Calculate the median
sorted_data = sorted(data)
n = len(sorted_data)
median = sorted_data[n // 2] if n % 2 != 0 else (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2

# Calculate the mode
from collections import Counter
counted_data = Counter(data)
mode = [k for k, v in counted_data.items() if v == max(counted_data.values())]

# Calculate the quartiles and percentiles
q1 = np.percentile(sorted_data, 25)
q3 = np.percentile(sorted_data, 75)
p10 = np.percentile(sorted_data, 10)
p95 = np.percentile(sorted_data, 95)

# Print the results
print(f"Date: {datetime.datetime.today()}")
print(f"Median: {median}")
print(f"Mode: {', '.join(map(str, mode))}")
print(f"Q1 (First Quartile): {q1}")
print(f"Q3 (Third Quartile): {q3}")
print(f"P10 (10th Percentile): {p10}")
print(f"P95 (95th Percentile): {p95}")
