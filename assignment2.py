import random
import numpy as np
import matplotlib.pyplot as plt
import  datetime

def calculate_mean(data):
    return sum(data) / len(data)

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

def calculate_std_dev(data, mean):
    squared_diff = [(x - mean) ** 2 for x in data]
    variance = sum(squared_diff) / len(data)
    std_dev = variance ** 0.5
    return std_dev

random_numbers = [random.gauss(10, 0.5) for _ in range(500)]

mean = calculate_mean(random_numbers)
median = calculate_median(random_numbers)
std_dev = calculate_std_dev(random_numbers, mean)

plt.hist(random_numbers, bins=10, edgecolor='black')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title(f'Date: {datetime.datetime.today()}\nHistogram of 500 Random Numbers (Gaussian Distribution)')
plt.grid(True)

print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Standard Deviation: {std_dev}")

plt.show()
