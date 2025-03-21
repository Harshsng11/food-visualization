# import pandas as pd
# import numpy as np
# from sklearn.cluster import KMeans
# from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import csv
# import seaborn as sns

# # Step 1: Open the Excel file
file_path = 'data.csv'  # Path to your Excel file
file = open("data.csv", "r")
csvreader = csv.reader(file)
header = []
header = next(csvreader)
rows = []
for row in csvreader:
    rows.append(row)
file.close()


# Create a simple line plot
for k in rows:
    plt.plot(k)

# Add titles and labels
plt.title("Simple Line Plot")
# plt.xlabel("X-axis")
# plt.ylabel("Y-axis")
plt.xticks(rotation=0)  # Rotate x-axis labels
plt.yticks(rotation=45)
# plt.figure(figsize=(80, 60))
plt.tight_layout()
# plt.gcf().autofmt_xdate()

plt.savefig('plot.png', format='png')

# Optionally, display the plot
plt.show()