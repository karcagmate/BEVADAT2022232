import numpy as np
import pandas as pd
#path="diabetes.csv"
import random as random
from scipy.stats import mode
from typing import Tuple
import seaborn as sns
from sklearn.metrics import confusion_matrix

class KNNClassifier:

    def __init__(self,k:int,test_split_ratio :float) :
         self.k=k
         self.test_split_ratio=test_split_ratio
         #self.x_train=None
         #self.y_train=None
         #self.x_test=None
         #self.y_test=None
         #self.y_preds=None
    @property
    def k_neighbors(self):
       return self.k
    @staticmethod
    def loadcsv(path:str)->Tuple[pd.DataFrame,pd.Series]:
     #random.seed(42)
     dataset=pd.read_csv(path)
     dataset=dataset.sample(frac=1,random_state=42).reset_index(drop=True)
     x,y=dataset.iloc[:,:-1],dataset.iloc[:,-1]
     return x,y
    
    def train_test_split(self,featrues:pd.DataFrame,labels:pd.Series)-> None:
     test_size=int(len(featrues)*self.test_split_ratio)
     train_size=len(featrues)-test_size
     assert len(featrues)==test_size+train_size,"Size mismatch!"

     self.x_train,self.y_train=featrues.iloc[:train_size,:].reset_index(drop=True),labels.iloc[:train_size].reset_index(drop=True)
     self.x_test,self.y_test=featrues.iloc[train_size:train_size+test_size,:].reset_index(drop=True),labels.iloc[train_size:train_size+test_size].reset_index(drop=True)

    def euclidean(self,element_of_x:pd.Series)->pd.Series:
     return pd.np.sqrt(((self.x_train - element_of_x)**2).sum(axis=1))
    
    def predict(self,x_test:pd.DataFrame):

      labels_pred = []
      for  x_test_element in x_test.iterrows():
            distances = self.euclidean(x_test_element)
            distances = pd.DataFrame({'distances': distances, 'labels': self.y_train})
            distances.sort_values(by='distances', inplace=True)
            label_pred = mode(distances.iloc[:self.k,1],axis=0).mode[0]
            labels_pred.append(label_pred)
      self.y_preds = pd.Series(labels_pred)
    def accuracy(self) -> float:
     
     true_positive = (self.y_test == self.y_preds).sum()
     return true_positive / len(self.y_test) * 100
    def confusion_matrix(self):
     return confusion_matrix(self.y_test,self.y_preds)
    def best_k(self) -> Tuple[int, float]:
        accu = []
        for i in range(1, 21):
            self.k = i
            self.predict(self.x_test)
            acc = self.accuracy()
            accu.append((i, acc))
        best_k, best_acc = max(accu, key=lambda x: x[1])
        return (best_k, round(best_acc, 2))
     
     
