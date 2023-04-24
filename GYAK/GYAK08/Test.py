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
Lr=LinearRegression()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model=Lr.fit(X_test,y_test)
pred=Lr.predict(X_test,model)
print(pred)
plt.scatter(X_test,y_test)
plt.plot([min(X_test), max(X_test)], [min(pred), max(pred)], color='red')
plt.show()





