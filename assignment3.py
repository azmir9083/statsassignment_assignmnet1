import matplotlib.pyplot as plt
import datetime
# Data
causes_of_death = [
    "Heart Disease", "Malignant Neoplasms", "Stroke", "Chronic Respiratory Disease",
    "Accidents", "Diabetes", "Alzheimer's", "Influenza/Pneumonia",
    "Nephritis/Nephrosis", "Septicemia"
]
number_of_deaths = [632000, 560000, 137000, 125000, 122000, 72000, 72000, 56000, 45000, 34000]

# Sort the causes and deaths in descending order
sorted_data = sorted(zip(causes_of_death, number_of_deaths), key=lambda x: x[1], reverse=True)
sorted_causes, sorted_deaths = zip(*sorted_data)

# Calculate the cumulative percentage
total_deaths = sum(sorted_deaths)
cumulative_percentage = [100 * sum(sorted_deaths[:i+1]) / total_deaths for i in range(len(sorted_deaths))]

# Create the Pareto chart
fig, ax1 = plt.subplots()

ax1.bar(sorted_causes, sorted_deaths, color='b')
ax1.set_xlabel('Cause of Death')
ax1.set_ylabel('Number of Deaths', color='b')
ax1.tick_params('y', colors='b')

ax2 = ax1.twinx()
ax2.plot(sorted_causes, cumulative_percentage, color='r', marker='o', linestyle='-', linewidth=2)
ax2.set_ylabel('Cumulative Percentage', color='r')
ax2.tick_params('y', colors='r')

plt.xticks(rotation=90)
plt.title(f'Date: {datetime.datetime.today()}\nPareto Chart of Leading Causes of Death in the United States (2006)')
plt.tight_layout()
plt.show()
