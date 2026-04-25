import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

data={
    'sqft': [1000, 1500, 1800, 2400, 3000],
    'bedrooms': [2, 3, 3, 4, 5],
    'bathrooms': [1, 2, 2, 3, 4],
    'age': [10, 5, 8, 2, 1],
    'location': ['A', 'B', 'A', 'B', 'C'],
    'price': [200000, 300000, 320000, 400000, 500000]
}
df=pd.DataFrame(data)
df=df.dropna()
df = pd.get_dummies(df, columns=['location'])
x=df.drop('price',axis=1)
y=df['price']
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
model=LinearRegression()
model.fit(x_train,y_train)
y_pred=model.predict(x_test)
print("==============================================================")
print("Predicted: ",y_pred)
print("MSE:", mean_squared_error(y_test, y_pred))
print("R2 Score:", r2_score(y_test, y_pred))

new_house = [[2000, 3, 2, 5, 1, 0, 0]]  # encoded location
print("New Price:", model.predict(new_house))
print("==============================================================")
