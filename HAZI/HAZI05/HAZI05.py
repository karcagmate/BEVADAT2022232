import pandas as pd
#path="diabetes.csv"
import random as random
from scipy.stats import mode
from typing import Tuple
import seaborn as sns
from sklearn.metrics import confusion_matrix

class KNNClassifier:

    def __init__(self,k:int,test_split_ratio :float) -> None:
         self.k=k
         self.test_split_ratio=test_split_ratio
         self.x_train=None
         self.y_train=None
         self.x_test=None
         self.y_test=None
         self.y_preds=None
    @property
    def k_neighbors(self):
       return self.k
    @staticmethod
    def loadcsv(path:str)->Tuple[pd.DataFrame,pd.DataFrame]:
     #random.seed(42)
     dataset=pd.read_csv(path)
     
     dataset=dataset.sample(frac=1,random_state=42)
     x,y=dataset.iloc[:,:-1],dataset.iloc[:,-1]
     return x,y
    def train_test_split(self,featrues:pd.DataFrame,labels:pd.DataFrame)-> None:
     test_size=int(len(featrues)*self.test_split_ratio)
     train_size=len(featrues)-test_size
     assert len(featrues)==test_size+train_size,"Size mismatch!"
     self.x_train,self.y_train=featrues.iloc[:train_size,:],labels.iloc[:train_size]
     self.x_test,self.y_test=featrues.iloc[train_size:,:],labels.iloc[train_size:]
    def euclidan(self,element_of_x:pd.Series)->pd.Series:
     return ((pd.Series.sum((self.x_train-element_of_x)**2,axis=1))**(1/2))
    def perdict(self,x_test:pd.Series)->pd.Series:
     labels_pred=[]
     for x_test_element in x_test:
            distances= self.euclidan(x_test_element)
            distances=pd.Series(sorted(zip(distances,self.y_train)))
            label_pred=mode(distances[:self.k,1],keepdims=False).mode
            labels_pred.append(label_pred)
     return  pd.Series(labels_pred,dtype=int)
    def accuracy(self) -> float:
     true_positive = (self.y_test == self.y_preds).sum()
     return true_positive / len(self.y_test) * 100
    def confusion_matrix(self):
     return confusion_matrix(self.y_test,self.y_preds)
     
     
