import numpy as np

from typing import Tuple
from scipy.stats import mode
from sklearn.metrics import confusion_matrix
import seaborn as sns
#path="iris.csv"
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
    def loadcsv(path:str)->Tuple[np.ndarray,np.ndarray]:
        np.random.seed(42)
        dataset=np.genfromtxt(path,delimiter=',')
        np.random.shuffle(dataset)
        x,y=dataset[:,:-1],dataset[:,-1]

        return x,y
    
    def train_test_split(self,featrues:np.ndarray,labels:np.ndarray)->None:
        test_size=int(len(featrues)*self.test_split_ratio)
        train_size=len(featrues)-test_size
        assert len(featrues)==test_size+train_size,"Size mismatch!"
        x_train,y_train=featrues[:train_size,:],labels[:train_size]
        x_test,y_test=featrues[train_size:,:],labels[train_size:]
        self.x_train,self.y_train=x_train,y_train

        self.x_test,self.y_test=x_test,y_test
    
    def euclidan(self,element_of_x:np.ndarray)->np.ndarray:
      return np.sqrt(np.sum((self.x_train-element_of_x)**2,axis=1))
    
    
    def perdict(self,x_test:np.ndarray)->np.ndarray:
        labels_pred=[]
        for x_test_element in x_test:
            distances= self.euclidean(x_test_element)
            distances=np.array(sorted(zip(distances,self.y_train)))
            label_pred=mode(distances[:self.k,1],keepdims=False).mode
            self.y_pred.append(label_pred)
        return  np.ndarray(labels_pred,dtype=np.int64)
    
    def accuracy(self) -> float:
        true_positive = (self.y_test == self.y_preds).sum()
        return true_positive / len(self.y_test) * 100
    
    def confusion_matrix(self):
        return confusion_matrix(self.y_test,self.y_preds)
    
   



    
    

    

      
        
    
     