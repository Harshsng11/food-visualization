import matplotlib.pyplot as plt
import csv

# Step 1: Open and read the CSV file
file_path = 'data.csv'
with open(file_path, 'r') as file:
    csvreader = csv.reader(file)
    header = next(csvreader)  # Extract header
    rows = [row for row in csvreader]  # Store all rows

# Step 2: Extract data for plotting (e.g., Orders)
dish_names = [row[0] for row in rows]  # Dish Name (column 0)
orders = [float(row[4]) for row in rows]  # Orders (Sales) (column 4)

# Step 3: Create a line plot
plt.plot(orders)  # Plot Orders as a line

# Step 4: Customize the plot
plt.title("Orders (Sales) per Dish")
plt.xlabel("Dish Index")
plt.ylabel("Number of Orders")
plt.xticks(ticks=range(len(dish_names)), labels=dish_names, rotation=45)  # Use dish names as x-ticks
plt.tight_layout()

# Step 5: Save and display
plt.savefig('plot2.png', format='png')
plt.show()