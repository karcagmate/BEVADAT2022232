from LinearRegressionSkeleton import LinearRegression
import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from matplotlib import pyplot as plt
iris=load_iris()
data=pd.DataFrame(iris.data,columns=iris.feature_names)
X=data['petal width (cm)'].values
y=data['sepal length (cm)'].values
Lr=LinearRegression()
X_test,y_test=Lr.fit(X,y)
pred=Lr.predict(X)
print(pred)
plt.scatter(X_test,y_test)
plt.plot([min(X_test), max(X_test)], [min(pred), max(pred)], color='red')
plt.show()