# DAY 15 PROJECT - MINI EDA DASHBOARD (COMBINED)

import matplotlib.pyplot as plt
import numpy as np

# Sample Dataset
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [120, 150, 170, 160, 200, 220]

products = ["A", "B", "C", "D"]
profits = [40, 70, 30, 90]

marks = [55, 60, 62, 65, 70, 72, 75, 78, 80, 85, 90, 95, 100]

# Create Subplots
fig, axes = plt.subplots(1, 3, figsize=(18, 5))

# ---------------------------
# 1. LINE CHART (Trend)
# ---------------------------
axes[0].plot(months, sales, marker='o', linewidth=3)
axes[0].set_title("Sales Trend")
axes[0].set_xlabel("Months")
axes[0].set_ylabel("Sales")

# ---------------------------
# 2. BAR CHART (Comparison)
# ---------------------------
axes[1].bar(products, profits)
axes[1].set_title("Product Profit Comparison")
axes[1].set_xlabel("Products")
axes[1].set_ylabel("Profit")

# ---------------------------
# 3. HISTOGRAM (Distribution)
# ---------------------------
axes[2].hist(marks, bins=5)
axes[2].set_title("Marks Distribution")
axes[2].set_xlabel("Marks")
axes[2].set_ylabel("Frequency")

# Dashboard Title
plt.suptitle("Mini EDA Dashboard", fontsize=18)

# Adjust Layout
plt.tight_layout()

# Show Dashboard
plt.show()

# ---------------------------
# INSIGHTS
# ---------------------------
print("INSIGHTS:")
print("1. Sales are increasing overall with slight variation in April.")
print("2. Product D has the highest profit.")
print("3. Most marks are distributed between 70 and 90.")
print("4. No major outliers are visible in the dataset.")