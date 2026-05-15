# ======================================================
# OPEN DATASET CAPSTONE PROJECT - DAY 20
# ======================================================

# Import Required Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ------------------------------------------------------
# STEP 1: CREATE SAMPLE SALES DATASET
# ------------------------------------------------------

data = {
    'Product': [
        'Laptop',
        'Mobile',
        'Tablet',
        'Headphones',
        'Smartwatch',
        'Laptop',
        'Mobile',
        'Tablet',
        'Headphones',
        'Smartwatch'
    ],

    'Category': [
        'Electronics',
        'Electronics',
        'Electronics',
        'Accessories',
        'Accessories',
        'Electronics',
        'Electronics',
        'Electronics',
        'Accessories',
        'Accessories'
    ],

    'Sales': [
        55000,
        30000,
        20000,
        5000,
        8000,
        60000,
        35000,
        22000,
        7000,
        10000
    ],

    'Profit': [
        12000,
        7000,
        5000,
        1200,
        2000,
        15000,
        8000,
        5500,
        1500,
        2500
    ],

    'Region': [
        'North',
        'South',
        'East',
        'West',
        'North',
        'South',
        'East',
        'West',
        'North',
        'South'
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

print("========== ORIGINAL DATASET ==========")
print(df)

# ------------------------------------------------------
# STEP 2: DATA CLEANING
# ------------------------------------------------------

# Check Missing Values
print("\n========== MISSING VALUES ==========")
print(df.isnull().sum())

# Remove Duplicate Values
df = df.drop_duplicates()

print("\n========== CLEANED DATASET ==========")
print(df)

# ------------------------------------------------------
# STEP 3: DATA ANALYSIS
# ------------------------------------------------------

# Total Sales
total_sales = df['Sales'].sum()

# Total Profit
total_profit = df['Profit'].sum()

# Average Sales
average_sales = df['Sales'].mean()

print("\n========== SALES ANALYSIS ==========")

print("Total Sales:", total_sales)
print("Total Profit:", total_profit)
print("Average Sales:", average_sales)

# ------------------------------------------------------
# STEP 4: CATEGORY-WISE SALES
# ------------------------------------------------------

category_sales = df.groupby('Category')['Sales'].sum()

print("\n========== CATEGORY WISE SALES ==========")
print(category_sales)

# ------------------------------------------------------
# STEP 5: REGION-WISE PROFIT
# ------------------------------------------------------

region_profit = df.groupby('Region')['Profit'].sum()

print("\n========== REGION WISE PROFIT ==========")
print(region_profit)

# ------------------------------------------------------
# STEP 6: VISUALIZATION - SALES BY CATEGORY
# ------------------------------------------------------

plt.figure(figsize=(8,5))

category_sales.plot(kind='bar')

plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")

plt.grid(True)

plt.show()

# ------------------------------------------------------
# STEP 7: VISUALIZATION - PROFIT BY REGION
# ------------------------------------------------------

plt.figure(figsize=(8,5))

region_profit.plot(kind='pie',
                   autopct='%1.1f%%')

plt.title("Profit Distribution by Region")

plt.ylabel("")

plt.show()

# ------------------------------------------------------
# STEP 8: TOP SELLING PRODUCTS
# ------------------------------------------------------

top_products = df.sort_values(by='Sales',
                              ascending=False)

print("\n========== TOP SELLING PRODUCTS ==========")
print(top_products[['Product', 'Sales']])

# ------------------------------------------------------
# STEP 9: ADVANCED INSIGHTS
# ------------------------------------------------------

highest_sales = df.loc[df['Sales'].idxmax()]

highest_profit = df.loc[df['Profit'].idxmax()]

print("\n========== ADVANCED INSIGHTS ==========")

print("\nHighest Selling Product:")
print(highest_sales)

print("\nHighest Profit Product:")
print(highest_profit)

# ------------------------------------------------------
# STEP 10: DASHBOARD STYLE VISUALIZATION
# ------------------------------------------------------

plt.figure(figsize=(10,5))

plt.plot(df['Product'],
         df['Sales'],
         marker='o',
         label='Sales')

plt.plot(df['Product'],
         df['Profit'],
         marker='s',
         label='Profit')

plt.title("Sales vs Profit Dashboard")
plt.xlabel("Products")
plt.ylabel("Amount")

plt.legend()

plt.grid(True)

plt.show()

# ------------------------------------------------------
# STEP 11: WRITTEN SUMMARY
# ------------------------------------------------------

print("\n========== PROJECT SUMMARY ==========")

print("""
1. Performed Data Cleaning
2. Analyzed Sales and Profit
3. Created Category-wise Analysis
4. Created Region-wise Analysis
5. Visualized Data using Charts
6. Identified Top Selling Products
7. Generated Business Insights
8. Created Dashboard-style Visualization
""")

# ======================================================
# END OF PROJECT
# ======================================================