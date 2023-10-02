import random
import matplotlib.pyplot as plt
import datetime

# User-defined function to calculate the mean
def calculate_mean(data):
    return sum(data) / len(data)

# User-defined function to calculate the median
def calculate_median(data):
    sorted_data = sorted(data)
    n = len(sorted_data)
    if n % 2 == 0:
        middle1 = sorted_data[n // 2]
        middle2 = sorted_data[n // 2 - 1]
        median = (middle1 + middle2) / 2
    else:
        median = sorted_data[n // 2]
    return median

# User-defined function to calculate the standard deviation
def calculate_std_dev(data, mean):
    squared_diff = [(x - mean) ** 2 for x in data]
    variance = sum(squared_diff) / len(data)
    std_dev = variance ** 0.5
    return std_dev

# Generate 500 random numbers from -20 to +20
random_numbers = [random.uniform(-20, 20) for _ in range(500)]

# Calculate mean, median, and standard deviation using user-defined functions
mean = calculate_mean(random_numbers)
median = calculate_median(random_numbers)
std_dev = calculate_std_dev(random_numbers, mean)

# Plot a histogram with 10 bins
plt.hist(random_numbers, bins=10, edgecolor='black')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title(f'Date: {datetime.datetime.today()}\nHistogram of 500 Random Numbers (Uniform Distribution)')
plt.grid(True)

# Display the calculated mean, median, and standard deviation
print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Standard Deviation: {std_dev}")

# Show the histogram plot
plt.show()
