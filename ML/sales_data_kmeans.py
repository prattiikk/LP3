# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from kneed import KneeLocator


# Load dataset and select only numeric columns
df = pd.read_csv('sales_data_sample.csv', encoding='latin1')
numeric_data = df[['QUANTITYORDERED', 'SALES']].dropna()  # Keep only necessary numeric columns and drop any NA rows

# Standardize the data
scaler = StandardScaler()
scaled_data = scaler.fit_transform(numeric_data)

# Use the elbow method to determine the optimal number of clusters (k)
inertia = []
K_range = range(1, 11)

for k in K_range:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(scaled_data)
    inertia.append(kmeans.inertia_)

# Plot the inertia to find the elbow
plt.plot(K_range, inertia, marker='o')
plt.xlabel('Number of clusters (k)')
plt.ylabel('Inertia')
plt.title('Elbow Method to Determine Optimal k')
plt.show()

# Use KneeLocator to find the optimal k
kneedle = KneeLocator(K_range, inertia, curve="convex", direction="decreasing")
optimal_k = kneedle.elbow
print("Optimal k based on elbow:", optimal_k)

# Perform KMeans clustering with optimal k
kmeans = KMeans(n_clusters=optimal_k, random_state=42)
numeric_data['Cluster'] = kmeans.fit_predict(scaled_data)
centroids = kmeans.cluster_centers_

# Plot the clusters with centroids
plt.scatter(numeric_data['SALES'], numeric_data['QUANTITYORDERED'], c=numeric_data['Cluster'], cmap='viridis')
plt.scatter(centroids[:, 1], centroids[:, 0], marker='x', s=200, color='red', label='Centroids')
plt.xlabel('SALES')
plt.ylabel('QUANTITYORDERED')
plt.title('K-Means Clustering with Centroids')
plt.legend()
plt.show()

# Alternative plot using seaborn
sns.scatterplot(x='SALES', y='QUANTITYORDERED', hue='Cluster', data=numeric_data, palette='viridis')
plt.scatter(centroids[:, 1], centroids[:, 0], marker='x', s=200, color='red', label='Centroids')
plt.xlabel('SALES')
plt.ylabel('QUANTITYORDERED')
plt.title('K-Means Clustering with Centroids')
plt.legend()
plt.show()