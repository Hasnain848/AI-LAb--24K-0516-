import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
data = {
    'student_id': [1,2,3,4,5,6,7,8,9,10],
    'GPA': [3.5, 2.0, 3.8, 1.5, 3.2, 2.5, 3.9, 1.8, 3.0, 2.2],
    'study_hours': [20, 5, 25, 3, 18, 10, 28, 4, 15, 8],
    'attendance_rate': [90, 60, 95, 50, 85, 70, 98, 55, 80, 65]
}
df = pd.DataFrame(data)
X = df[['GPA', 'study_hours', 'attendance_rate']]
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
wcss = []
for i in range(2, 7):  # K from 2 to 6
    kmeans = KMeans(n_clusters=i, random_state=42)
    kmeans.fit(X_scaled)
    wcss.append(kmeans.inertia_)
plt.plot(range(2,7), wcss, marker='o')
plt.title("Elbow Method")
plt.xlabel("Number of Clusters (K)")
plt.ylabel("WCSS")
plt.show()
kmeans = KMeans(n_clusters=3, random_state=42)
df['Cluster'] = kmeans.fit_predict(X_scaled)
print(df[['student_id', 'Cluster']])
plt.scatter(df['study_hours'], df['GPA'], c=df['Cluster'])
plt.xlabel("Study Hours")
plt.ylabel("GPA")
plt.title("Student Clustering based on Performance")

plt.show()
