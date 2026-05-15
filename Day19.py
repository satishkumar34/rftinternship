# ==========================================
# STOCK / TIME-SERIES ANALYSIS - DAY 19
# ==========================================

# Import Required Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ------------------------------------------
# STEP 1: CREATE STOCK DATASET
# ------------------------------------------

data = {
    'Date': [
        '2025-01-01',
        '2025-01-02',
        '2025-01-03',
        '2025-01-04',
        '2025-01-05',
        '2025-01-06',
        '2025-01-07',
        '2025-01-08',
        '2025-01-09',
        '2025-01-10'
    ],
    
    'Stock_Price': [
        100,
        105,
        102,
        108,
        115,
        111,
        118,
        120,
        117,
        125
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

# Convert Date column into datetime
df['Date'] = pd.to_datetime(df['Date'])

print("========== STOCK DATASET ==========")
print(df)

# ------------------------------------------
# STEP 2: CALCULATE MOVING AVERAGE
# ------------------------------------------

df['Moving_Average'] = df['Stock_Price'].rolling(window=3).mean()

print("\n========== MOVING AVERAGE ==========")
print(df)

# ------------------------------------------
# STEP 3: IDENTIFY PEAKS & DROPS
# ------------------------------------------

highest_price = df['Stock_Price'].max()
lowest_price = df['Stock_Price'].min()

peak_day = df[df['Stock_Price'] == highest_price]
drop_day = df[df['Stock_Price'] == lowest_price]

print("\n========== HIGHEST STOCK PRICE ==========")
print(peak_day)

print("\n========== LOWEST STOCK PRICE ==========")
print(drop_day)

# ------------------------------------------
# STEP 4: DETECT VOLATILITY
# ------------------------------------------

volatility = df['Stock_Price'].std()

print("\n========== VOLATILITY ==========")
print("Stock Volatility:", volatility)

# ------------------------------------------
# STEP 5: VISUALIZE PRICE TREND
# ------------------------------------------

plt.figure(figsize=(10,5))

plt.plot(df['Date'], df['Stock_Price'], marker='o')

plt.title("Stock Price Trend")
plt.xlabel("Date")
plt.ylabel("Stock Price")

plt.grid(True)

plt.show()

# ------------------------------------------
# STEP 6: VISUALIZE MOVING AVERAGE
# ------------------------------------------

plt.figure(figsize=(10,5))

plt.plot(df['Date'], df['Stock_Price'],
         marker='o',
         label='Stock Price')

plt.plot(df['Date'], df['Moving_Average'],
         marker='s',
         label='Moving Average')

plt.title("Stock Price & Moving Average")
plt.xlabel("Date")
plt.ylabel("Price")

plt.legend()

plt.grid(True)

plt.show()

# ------------------------------------------
# STEP 7: COMPARE MULTIPLE STOCKS
# ------------------------------------------

stock_A = [100,105,102,108,115,111,118,120,117,125]
stock_B = [95,97,99,101,100,104,106,108,110,112]

plt.figure(figsize=(10,5))

plt.plot(df['Date'], stock_A,
         marker='o',
         label='Stock A')

plt.plot(df['Date'], stock_B,
         marker='s',
         label='Stock B')

plt.title("Comparison of Multiple Stocks")
plt.xlabel("Date")
plt.ylabel("Stock Price")

plt.legend()

plt.grid(True)

plt.show()

# ------------------------------------------
# STEP 8: PROJECT SUMMARY
# ------------------------------------------

print("\n========== PROJECT SUMMARY ==========")

print("""
1. Created stock time-series dataset
2. Calculated moving average
3. Identified stock peaks and drops
4. Detected stock volatility
5. Visualized stock price trend
6. Visualized moving average line
7. Compared multiple stocks
""")

# ==========================================
# END OF PROJECT
# ==========================================