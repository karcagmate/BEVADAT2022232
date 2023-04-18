import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd
from matplotlib import pyplot as plt


class LinearRegression:
    def __init__(self, epochs: int = 1000, lr: float = 1e-3):
        self.epochs=epochs
        self.lr=lr

    def fit(self, X: np.array, y: np.array):
      iris=load_iris()
      df = pd.DataFrame(iris.data, columns=iris.feature_names) 
      X=df['petal width (cm)'].values
      y=df['sepal length (cm)'].values 
      self.m=0
      self.c=0
      self.X_train,self.X_test,self.y_train,self.y_test=train_test_split(X,y,test_size=0.2,random_state=42)
      losses=[]
      n=float(len(self.X_train))
      for i in range(self.epochs): 
         y_pred = m*self.X_train + c  

         residuals = y_pred - self.y_train
         loss = np.sum(residuals ** 2)
         losses.append(loss)
         D_m = (-2/n) * sum(self.X_train * residuals) 
         D_c = (-2/n) * sum(residuals)  
         m = m - self.lr * D_m  
         c = c - self.lr * D_c  



    def predict(self, X):
        self.pred = []
        for X in self.X_test:
         y_pred = self.m*X + self.c
         self.pred.append(y_pred)

    def evaluate(self,X,y):
        np.mean(np.abs(self.y_pred-self.y_test))
        np.mean((self.y_pred -self. y_test)**2)

        

    
