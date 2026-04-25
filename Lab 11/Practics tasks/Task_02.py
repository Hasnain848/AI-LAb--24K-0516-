data = {
'vehicle_serial_no': [5, 3, 8, 2, 4, 7, 6, 10, 1, 9],
'mileage': [150000, 120000, 250000, 80000, 100000, 220000, 180000, 300000, 75000, 280000],
'fuel_efficiency': [15, 18, 10, 22, 20, 12, 16, 8, 24, 9],
'maintenance_cost': [5000, 4000, 7000, 2000, 3000, 6500, 5500, 8000, 1500, 7500],
'vehicle_type': ['SUV', 'Sedan', 'Truck', 'Hatchback', 'Sedan', 'Truck', 'SUV', 'Truck', 'Hatchback', 'SUV']
}

df = pd.DataFrame(data)
df['vehicle_type'] = df['vehicle_type'].map({
    'SUV': 0, 'Sedan': 1, 'Truck': 2, 'Hatchback': 3
})
X = df.drop('vehicle_serial_no', axis=1)

kmeans1 = KMeans(n_clusters=3, random_state=42)
df['Cluster_NoScaling'] = kmeans1.fit_predict(X)
scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)

kmeans2 = KMeans(n_clusters=3, random_state=42)
df['Cluster_Scaled'] = kmeans2.fit_predict(X_scaled)
print(df.head())

#Analysis
#Without Scaling: Mileage dominates (very large numbers) Clusters mainly based on mileage With Scaling: All features contribute Better grouping (fuel + maintenance + type)

#Conclusion:

#Feature scaling is necessary when features have different units.

