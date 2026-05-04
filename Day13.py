# Import libraries
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# -----------------------------
# Create Dataset (Example)
# -----------------------------
# You can replace this with your own dataset (marks or salary)
np.random.seed(42)

# Example: Student marks (normal distribution)
marks = np.random.normal(loc=70, scale=10, size=200)

# Convert to DataFrame
df = pd.DataFrame({'Marks': marks})

# -----------------------------
# Plot Histogram + KDE
# -----------------------------
plt.figure(figsize=(8,5))

sns.histplot(df['Marks'], kde=True, bins=20)

plt.title("Distribution of Student Marks")
plt.xlabel("Marks")
plt.ylabel("Frequency")

plt.show()

# -----------------------------
# Identify Skewness
# -----------------------------
skewness = df['Marks'].skew()

print("Skewness Value:", skewness)

# Interpretation
if skewness > 0:
    print("Distribution is Positively Skewed (Right Skewed)")
elif skewness < 0:
    print("Distribution is Negatively Skewed (Left Skewed)")
else:
    print("Distribution is Symmetrical")