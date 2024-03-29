from LinearRegressionSkeleton import LinearRegression
import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
iris=load_iris()
data=pd.DataFrame(iris.data,columns=iris.feature_names)
X=data['petal width (cm)'].values
y=data['sepal length (cm)'].values
Lr=LinearRegression(data)

X_train, X_test, y_train, y_test = Lr.split(X,y)
Lr.fit(X_test,y_test)
pred=Lr.predict(X)
print(pred)
plt.scatter(X_test,y_test)
plt.plot([min(X_test), max(X_test)], [min(pred), max(pred)], color='red')
plt.show()





