import matplotlib.pyplot as plt

# Dataset
dates = ["Mon", "Tue", "Wed", "Thu", "Fri"]
sales = [200, 250, 300, 280, 350]

# Find highest and lowest sales
max_sales = max(sales)
min_sales = min(sales)

max_day = dates[sales.index(max_sales)]
min_day = dates[sales.index(min_sales)]

# Create line plot
plt.figure()
plt.plot(dates, sales, marker='o')

# Highlight highest and lowest points
plt.scatter(max_day, max_sales)
plt.scatter(min_day, min_sales)

# Annotate points
plt.text(max_day, max_sales, f" Highest: {max_sales}", ha='left')
plt.text(min_day, min_sales, f" Lowest: {min_sales}", ha='left')

# Labels and title
plt.xlabel("Days")
plt.ylabel("Sales")
plt.title("Sales Trend Over the Week")

# Show grid
plt.grid()

# Display plot
plt.show()