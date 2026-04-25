import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
df = pd.read_csv("/content/Mall_Customers.csv")
df = df.drop("CustomerID", axis=1)
df['Genre'] = df['Genre'].map({'Male': 1, 'Female': 0})
X = df.values
kmeans1 = KMeans(n_clusters=5, random_state=42)
clusters1 = kmeans1.fit_predict(X)
df['Cluster_NoScaling'] = clusters1
scaler = StandardScaler()

age = df[['Age']]
other_features = df.drop(['Age', 'Cluster_NoScaling'], axis=1)

scaled_features = scaler.fit_transform(other_features)

import numpy as np
X_scaled = np.concatenate([age.values, scaled_features], axis=1)

kmeans2 = KMeans(n_clusters=5, random_state=42)
clusters2 = kmeans2.fit_predict(X_scaled)

df['Cluster_Scaled'] = clusters2

print(df.head())
