import csv
from collections import defaultdict

# Step 1: Read CSV file
file_name = "D:/RFTINTERNSHIP/sales_data.csv"

data = []

with open(file_name, mode='r') as file:
    reader = csv.DictReader(file)
    
    for row in reader:
        # Convert values to proper types
        product = row['PRODUCT']
        quantity = int(row['QUANTITY'])
        price = int(row['PRICE'])
        
        # Bonus: Add TOTAL column
        total = quantity * price
        
        data.append({
            'PRODUCT': product,
            'QUANTITY': quantity,
            'PRICE': price,
            'TOTAL': total
        })

# Step 2: Calculate total sales per product
product_sales = defaultdict(int)

for row in data:
    product_sales[row['PRODUCT']] += row['TOTAL']

# Step 3: Calculate total revenue
total_revenue = sum(row['TOTAL'] for row in data)

# Step 4: Find top-selling product
top_product = max(product_sales, key=product_sales.get)

# Step 5: Sort data by revenue (TOTAL)
sorted_data = sorted(data, key=lambda x: x['TOTAL'], reverse=True)

# ---------------- OUTPUT ---------------- #

print("\n--- Data with TOTAL Column ---")
for row in data:
    print(row)

print("\n--- Total Sales Per Product ---")
for product, total in product_sales.items():
    print(f"{product}: {total}")

print("\n--- Total Revenue ---")
print(total_revenue)

print("\n--- Top Selling Product ---")
print(top_product)

print("\n--- Data Sorted by Revenue ---")
for row in sorted_data:
    print(row)