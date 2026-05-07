# DAY 14 PROJECT - CATEGORY BREAKDOWN (PIE CHART)

import matplotlib.pyplot as plt

# Dataset
categories = ["Food", "Travel", "Shopping"]
expenses = [500, 300, 200]

# Highlight highest category
explode = [0.1, 0, 0]

# Create Pie Chart
plt.figure(figsize=(7,7))

plt.pie(
    expenses,
    labels=categories,
    autopct='%1.1f%%',   # Percentage labels
    explode=explode,     # Highlight highest category
    shadow=True,
    startangle=90
)

# Title
plt.title("Category Breakdown of Expenses")

# Display Chart
plt.show()