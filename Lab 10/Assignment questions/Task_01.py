import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from imblearn.over_sampling import SMOTE

df = pd.read_csv("creditcard.csv")

X = df.drop("Class", axis=1)   
y = df["Class"]
print(y.value_counts())

sm = SMOTE(random_state=42)
X, y = sm.fit_resample(X, y)

scaler = StandardScaler()
X = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# -------- MODEL 1: Logistic Regression --------
lr = LogisticRegression(max_iter=1000)
lr.fit(X_train, y_train)
y_pred_lr = lr.predict(X_test)

print("Logistic Regression:\n")
print(classification_report(y_test, y_pred_lr))

# -------- MODEL 2: Random Forest --------
rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)
y_pred_rf = rf.predict(X_test)

print("Random Forest:\n")
print(classification_report(y_test, y_pred_rf))
