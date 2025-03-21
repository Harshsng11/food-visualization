import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Step 1: Create the dataset
data = {
    'Dish Name': ['Chicken Starter', 'Grilled Chicken', 'Paneer Noodles', 'Chicken Noodles', 
                  'Bread Boiled Egg', 'Immunity Dish', 'Butter Chicken', 'Veg Biryani', 
                  'Tandoori Chicken', 'Masala Dosa', 'Chicken Biryani', 'Paneer Tikka', 
                  'Egg Fried Rice', 'Veg Thali', 'Naan'],
    'Price (Rs.)': [499, 359, 250, 350, 99, 350, 450, 300, 500, 150, 400, 320, 280, 350, 50],
    'Orders (Sales)': [120, 90, 150, 130, 80, 70, 200, 110, 140, 100, 160, 90, 85, 95, 250],
    'Rating (out of 5)': [5.0, 4.3, 4.0, 4.5, 5.0, 5.0, 4.8, 4.2, 4.7, 4.5, 4.6, 4.4, 4.1, 4.3, 4.9]
}

df = pd.DataFrame(data)

# Step 2: Select numerical features for clustering
X = df[['Price (Rs.)', 'Orders (Sales)', 'Rating (out of 5)']]

# Step 3: Standardize the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Step 4: Apply K-means clustering
k = 3  # Number of clusters
kmeans = KMeans(n_clusters=k, random_state=42)
df['Cluster'] = kmeans.fit_predict(X_scaled)

# Step 5: Display the results
print("Clustered Data:")
print(df[['Dish Name', 'Price (Rs.)', 'Orders (Sales)', 'Rating (out of 5)', 'Cluster']])

# Step 6: Visualize and save the clusters as PNG
plt.figure(figsize=(10, 6))
scatter = plt.scatter(df['Price (Rs.)'], df['Orders (Sales)'], c=df['Cluster'], cmap='viridis')
plt.xlabel('Price (Rs.)')
plt.ylabel('Orders (Sales)')
plt.title('K-means Clustering of Dishes (k=3)')
plt.colorbar(scatter, label='Cluster')
for i, txt in enumerate(df['Dish Name']):
    plt.annotate(txt, (df['Price (Rs.)'][i], df['Orders (Sales)'][i]), fontsize=8)
plt.savefig('kmeans_clusters.png', dpi=300, bbox_inches='tight')  # Save as PNG
plt.close()  # Close the figure to free memory

# Step 7: Elbow method and save as PNG
inertia = []
K = range(1, 6)
for k in K:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X_scaled)
    inertia.append(kmeans.inertia_)

plt.figure(figsize=(8, 5))
plt.plot(K, inertia, 'bo-')
plt.xlabel('Number of Clusters (k)')
plt.ylabel('Inertia')
plt.title('Elbow Method for Optimal k')
plt.savefig('elbow_method.png', dpi=300, bbox_inches='tight')  # Save as PNG
plt.close()  # Close the figure

print("Plots saved as 'kmeans_clusters.png' and 'elbow_method.png' in the current directory.")