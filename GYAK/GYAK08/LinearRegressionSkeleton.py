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
        self.X_train=None
        self.X_test=None 
        self.y_train=None 
        self.y_test=None
    def split_data(self,X,y):
     self.X_train, self.X_test, self.y_train, self.y_test=train_test_split(X,y,test_size=0.2,random_state=42)
     
        

    def fit(self, X: np.array, y: np.array):
       m=0
       c=0
       self.L=0.2
    
       losses=[]
       n=float(len(self.X_train))
       for i in range(self.epochs): 
         y_pred = m*self.X_train + c  

         residuals = y_pred - self.y_train
         loss = np.sum(residuals ** 2)
         losses.append(loss)
         D_m = (-2/n) * sum(self.X_train * residuals) 
         D_c = (-2/n) * sum(residuals)  
         self.m = m - self.L * D_m  
         self.c = c - self.L * D_c
         if i % 100 == 0:
          print(np.mean(self.y_train-y_pred))
       return self.X_train,self.y_train  




    def predict(self, X):
       pred = []
       for self.X in self.X_test:
         self.y_pred = self.m*X + self.c
         pred.append(self.y_pred)
         self.y_pred = self.m*self.X_test + self.c
       return self.y_pred
        

    def evaluate(self,X,y):
        y_pred = self.predict(X)
        mse =np.mean((y_pred - y)**2)
        print("Mean Squared Error:", mse)
         #visszadja az elemeket numpy-ként

    #random összekveri a sort,de tanítás közben ugyanaz marad-> csak egyszer keveri össze, ugyanazt a problémát oldja meg
