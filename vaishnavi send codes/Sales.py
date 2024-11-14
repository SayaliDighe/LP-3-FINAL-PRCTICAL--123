import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from scipy.cluster.hierarchy import dendrogram, linkage

sales_data = pd.read_csv('sales_data_sample.csv', encoding='ISO-8859-1')
sales_data.head()

sales_data.isnull()
sales_data.dropna(inplace=True)
sales_data.isnull().sum()
# Select relevant numerical features for clustering
data_for_clustering = sales_data[['QUANTITYORDERED', 'PRICEEACH', 'SALES']]

# Standardize the features for better clustering performance
scaler = StandardScaler()
data_scaled = scaler.fit_transform(data_for_clustering)

# Determine the optimal number of clusters using the elbow method
inertia = []
cluster_range = range(1, 11)  # Testing cluster counts from 1 to 10

for k in cluster_range:
    kmeans = KMeans(n_clusters=k, random_state=0)
    kmeans.fit(data_scaled)
    inertia.append(kmeans.inertia_)

# Plot the elbow graph
plt.figure(figsize=(10, 6))
plt.plot(cluster_range, inertia, marker='o')
plt.xlabel('Number of Clusters')
plt.ylabel('Inertia')
plt.title('Elbow Method for Optimal Number of Clusters')
plt.show()

# Implement K-Means clustering with the chosen number of clusters (e.g., 3 clusters)
optimal_clusters = 3  # Replace this with the number of clusters determined by the elbow method
kmeans = KMeans(n_clusters=optimal_clusters, random_state=0)
kmeans_labels = kmeans.fit_predict(data_scaled)

# Append cluster labels to the original data
sales_data['Cluster'] = kmeans_labels

# Hierarchical clustering
linked = linkage(data_scaled, method='ward')

# Plot dendrogram
plt.figure(figsize=(10, 7))
dendrogram(linked, orientation='top', distance_sort='descending', show_leaf_counts=False)
plt.title('Hierarchical Clustering Dendrogram')
plt.xlabel('Sample index')
plt.ylabel('Distance')
plt.show()