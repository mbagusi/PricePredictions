import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np
from ..server import data_emas as data
import datetime

time = datetime.date.today() + datetime.timedelta(days=1)

x = data["date"]
X = x.values.reshape(-1, 1)
y = data["price"]

#plt.scatter(X, y)

#Linear
lin = LinearRegression()
lin.fit(X, y)

intercept = lin.intercept_
coef = lin.coef_

X_future = np.array(time.day)
X_future = X_future.reshape(-1, 1)

lin_predict = lin.predict(X)
lin_predict_future = lin.predict(X_future)

#plt.plot(X, lin_predict)
#plt.plot(X_future, lin_predict_future)

#plt.show()