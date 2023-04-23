import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split


class LinearRegression:
    def __init__(self, dataset : pd.DataFrame, epochs: int = 1000, lr: float = 1e-3):
        self.epochs = epochs
        self.lr = lr
        self.dataset = dataset

    def fit(self, X: np.array, y: np.array):
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        m = 0
        c = 0

        self.L = 0.2  
        self.epochs = 1000  

        n = float(len(self.X_train)) 

        # Performing Gradient Descent 
        losses = []
        for i in range(self.epochs): 
            y_pred = m*self.X_train + c  

            residuals = y_pred - self.y_train
            loss = np.sum(residuals ** 2)
            losses.append(loss)
            D_m = (-2/n) * sum(self.X_train * residuals)  
            D_c = (-2/n) * sum(residuals)  
            self.m = m + self.L * D_m  
            self.c = c + self.L * D_c  

        return self.X_train, self.y_train

    def predict(self, X):
        pred = []
        for self.X in self.X_test:
            self.y_pred = self.m*X + self.c
            pred.append(self.y_pred)

        self.y_pred = self.m*self.X_test + self.c
        return self.y_pred