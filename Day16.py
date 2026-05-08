# ==========================================
# COMPLETE SALES DATA EDA PROJECT - DAY 16
# ==========================================

# Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ==========================================
# STEP 1: CREATE SAMPLE SALES DATASET
# ==========================================

data = {
    'Date': [
        '2025-01-01', '2025-01-05', '2025-01-10',
        '2025-01-15', '2025-01-20', '2025-02-01',
        '2025-02-05', '2025-02-10', '2025-02-15',
        '2025-03-01'
    ],

    'Product': [
        'Laptop', 'Mobile', 'Tablet',
        'Laptop', 'Mobile', 'Tablet',
        'Laptop', 'Mobile', 'Tablet',
        'Laptop'
    ],

    'Region': [
        'North', 'South', 'East',
        'West', 'North', 'South',
        'East', 'West', 'North',
        'South'
    ],

    'Sales': [
        50000, 30000, np.nan,
        45000, 35000, 25000,
        60000, 40000, np.nan,
        70000
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

# ==========================================
# STEP 2: DISPLAY ORIGINAL DATA
# ==========================================

print("\n========== ORIGINAL DATA ==========\n")
print(df)

# ==========================================
# STEP 3: HANDLE MISSING VALUES
# ==========================================

# Fill missing sales values with mean
df['Sales'].fillna(df['Sales'].mean(), inplace=True)

print("\n========== DATA AFTER CLEANING ==========\n")
print(df)

# ==========================================
# STEP 4: CONVERT DATE COLUMN
# ==========================================

df['Date'] = pd.to_datetime(df['Date'])

# ==========================================
# STEP 5: TOTAL SALES PER PRODUCT
# ==========================================

product_sales = df.groupby('Product')['Sales'].sum()

print("\n========== TOTAL SALES PER PRODUCT ==========\n")
print(product_sales)

# ==========================================
# STEP 6: REGION-WISE PERFORMANCE
# ==========================================

region_sales = df.groupby('Region')['Sales'].sum()

print("\n========== REGION-WISE SALES ==========\n")
print(region_sales)

# ==========================================
# STEP 7: MONTHLY SALES ANALYSIS
# ==========================================

df['Month'] = df['Date'].dt.month_name()

monthly_sales = df.groupby('Month')['Sales'].sum()

print("\n========== MONTHLY SALES ==========\n")
print(monthly_sales)

# ==========================================
# STEP 8: BEST PERFORMING REGION
# ==========================================

best_region = region_sales.idxmax()

print("\n========== BEST PERFORMING REGION ==========\n")
print("Best Region:", best_region)

# ==========================================
# STEP 9: SALES TREND LINE CHART
# ==========================================

plt.figure(figsize=(10, 5))

daily_sales = df.groupby('Date')['Sales'].sum()

plt.plot(
    daily_sales.index,
    daily_sales.values,
    marker='o'
)

plt.title('Sales Trend Over Time')
plt.xlabel('Date')
plt.ylabel('Sales')

plt.grid(True)

plt.show()

# ==========================================
# STEP 10: TOP PRODUCTS BAR CHART
# ==========================================

plt.figure(figsize=(8, 5))

product_sales.plot(kind='bar')

plt.title('Total Sales Per Product')
plt.xlabel('Product')
plt.ylabel('Sales')

plt.xticks(rotation=0)

plt.show()

# ==========================================
# STEP 11: KEY INSIGHTS
# ==========================================

print("\n========== KEY INSIGHTS ==========\n")

print("1. Laptop has the highest total sales.")

print("2. North and South regions performed strongly.")

print("3. Sales increased in March.")

print("4. Missing values were successfully handled.")

print("5. Sales trends show business growth over time.")

# ==========================================
# END OF PROJECT
# ==========================================