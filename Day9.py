# DATA FILTERING TOOL (Project Day 9)

import pandas as pd

# Sample dataset (you can replace this with a CSV file)
data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eve"],
    "Age": [25, 32, 28, 45, 22],
    "Salary": [60000, 48000, 52000, 75000, 51000]
}

df = pd.DataFrame(data)

# Display original data
print("Original Dataset:\n")
print(df)

# -----------------------------
# FILTER CONDITIONS
# Salary > 50000 AND Age < 30
# -----------------------------
filtered_df = df[(df["Salary"] > 50000) & (df["Age"] < 30)]

# Display filtered results
print("\nFiltered Results (Salary > 50000 AND Age < 30):\n")
print(filtered_df)

# -----------------------------
# BONUS 1: Combine multiple conditions (already done using &)
# You can also use OR with |
# Example:
# filtered_df = df[(df["Salary"] > 50000) | (df["Age"] < 30)]
# -----------------------------

# -----------------------------
# BONUS 2: Save filtered data to new file
# -----------------------------
filtered_df.to_csv("filtered_data.csv", index=False)

print("\nFiltered data saved to 'filtered_data.csv'")