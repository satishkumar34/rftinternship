# ==========================================
# CUSTOMER SEGMENTATION ANALYSIS - DAY 17
# ==========================================

# Import Required Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ------------------------------------------
# STEP 1: CREATE SAMPLE DATASET
# ------------------------------------------

data = {
    'Customer_ID': [101,102,103,104,105,106,107,108,109,110],
    'Age': [22,25,47,52,46,56,28,33,41,39],
    'Spending': [2500,4000,15000,18000,12000,22000,3000,7000,14000,9000],
    'Visits': [5,8,20,22,18,25,4,10,17,12]
}

df = pd.DataFrame(data)

print("========== CUSTOMER DATA ==========")
print(df)

# ------------------------------------------
# STEP 2: CREATE CUSTOMER SEGMENTS
# ------------------------------------------

def segment_customer(spending):
    
    if spending >= 15000:
        return 'High'
    
    elif spending >= 7000:
        return 'Medium'
    
    else:
        return 'Low'

df['Segment'] = df['Spending'].apply(segment_customer)

print("\n========== CUSTOMER SEGMENTS ==========")
print(df)

# ------------------------------------------
# STEP 3: IDENTIFY HIGH VALUE CUSTOMERS
# ------------------------------------------

high_value = df[df['Segment'] == 'High']

print("\n========== HIGH VALUE CUSTOMERS ==========")
print(high_value)

# ------------------------------------------
# STEP 4: IDENTIFY LOW ENGAGEMENT USERS
# ------------------------------------------

low_engagement = df[df['Visits'] < 8]

print("\n========== LOW ENGAGEMENT USERS ==========")
print(low_engagement)

# ------------------------------------------
# STEP 5: SPENDING DISTRIBUTION GRAPH
# ------------------------------------------

plt.figure(figsize=(8,5))

plt.hist(df['Spending'], bins=5)

plt.title("Customer Spending Distribution")
plt.xlabel("Spending Amount")
plt.ylabel("Number of Customers")

plt.show()

# ------------------------------------------
# STEP 6: CUSTOMER CATEGORY COUNT
# ------------------------------------------

segment_count = df['Segment'].value_counts()

plt.figure(figsize=(6,5))

plt.bar(segment_count.index, segment_count.values)

plt.title("Customer Categories")
plt.xlabel("Segment")
plt.ylabel("Number of Customers")

plt.show()

# ------------------------------------------
# STEP 7: BUSINESS STRATEGIES
# ------------------------------------------

print("\n========== BUSINESS STRATEGIES ==========")

print("""
1. High Value Customers
   - Provide premium offers
   - Give loyalty rewards

2. Medium Customers
   - Send discount coupons
   - Encourage more purchases

3. Low Customers
   - Run marketing campaigns
   - Improve engagement using emails/SMS

4. Low Engagement Users
   - Provide special visit offers
   - Personalized recommendations
""")

# ------------------------------------------
# END OF PROJECT
# ------------------------------------------