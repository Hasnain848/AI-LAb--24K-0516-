from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

data = {
    'spending': [500, 2000, 1500, 300, 2500],
    'age': [25, 45, 35, 22, 50],
    'visits': [5, 20, 15, 3, 25],
    'frequency': [1, 5, 4, 1, 6],
    'label': [0, 1, 1, 0, 1]
}
df = pd.DataFrame(data)
X = df.drop('label', axis=1)
y = df['label']
scaler = StandardScaler()
X = scaler.fit_transform(X)
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model = SVC(kernel='linear')
model.fit(x_train, y_train)
y_pred = model.predict(x_test)
print("==============================================================")
print("Accuracy:", accuracy_score(y_test, y_pred))
print("===============================================================")
