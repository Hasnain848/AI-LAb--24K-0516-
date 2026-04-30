import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor

df = pd.read_csv("/content/boston.csv")
df.fillna(df.mean(numeric_only=True), inplace=True)
df = pd.get_dummies(df)

X = df.drop("MEDV", axis=1)  
y = df["MEDV"]            
scaler = StandardScaler()
X = scaler.fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# -------- MODEL 1: Linear Regression --------
lr = LinearRegression()
lr.fit(X_train, y_train)
y_pred_lr = lr.predict(X_test)

mae_lr = mean_absolute_error(y_test, y_pred_lr)
rmse_lr = np.sqrt(mean_squared_error(y_test, y_pred_lr))

print("Linear Regression:")
print("MAE:", mae_lr)
print("RMSE:", rmse_lr)

# -------- MODEL 2: Decision Tree --------
dt = DecisionTreeRegressor(random_state=42)
dt.fit(X_train, y_train)
y_pred_dt = dt.predict(X_test)

mae_dt = mean_absolute_error(y_test, y_pred_dt)
rmse_dt = np.sqrt(mean_squared_error(y_test, y_pred_dt))

print("\nDecision Tree:")
print("MAE:", mae_dt)
print("RMSE:", rmse_dt)
