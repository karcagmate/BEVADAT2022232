import numpy as np

from typing import Tuple
from scipy.stats import mode
from sklearn.metrics import confusion_matrix
import seaborn as sns
path="iris.csv"
class KNNClassifier:

 
    def __init__(self,k:int,test_split_ratio :float) -> None:
        self.k=k
        self.test_split_ratio=test_split_ratio
    @staticmethod
    def loadcsv(path)->Tuple[np.ndarray,np.ndarray]:
        np.random.seed(42)
        dataset=np.genfromtxt(path,delimiter=',')
        np.random.shuffle(dataset)
        x,y=dataset[:,:-1],dataset[:,-1]
        return x,y
    @classmethod
    def train_test_split(featrues:np.ndarray,labels:np.ndarray,self)->Tuple[np.ndarray,np.ndarray,np.ndarray]:
        test_size=int(len(featrues)*self.test_split_ratio)
        train_size=len(featrues)-test_size
        assert len(featrues)==test_size+train_size,"Size mismatch!"
        x_train,y_train=featrues[:train_size,:],labels[:train_size]
        x_test,y_test=featrues[train_size:,:],labels[train_size:]
        self.x_train,self.y_train=x_train,y_train
        self.x_test,self.y_test=x_test,y_test
    @classmethod
    def euclidan(points:np.ndarray,self)->np.ndarray:
      return np.sqrt(np.sum((points-self.element_of_x)**2,axis=1))
      
        
    
     