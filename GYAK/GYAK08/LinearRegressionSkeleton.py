import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression as lr


class LinearRegression:
    def __init__(self, epochs: int = 1000, lr: float = 1e-3):
        self.epochs = epochs
        self.lr = lr
        
    


    def fit(self,X:np.array,y:np.array):
    
        model=lr.fit(X,y)
        return model
        

        

        

    def predict(self, X,model):
       y_pred=model.predict(X)
       return y_pred