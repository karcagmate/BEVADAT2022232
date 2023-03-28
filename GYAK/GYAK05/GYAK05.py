import numpy as np

from typing import Tuple
from scipy.stats import mode
from sklearn.metrics import confusion_matrix, euclidean_distances
import seaborn as sns
#path="iris.csv"
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
    
    def euclidan(element_of_x:np.ndarray,self)->np.ndarray:
      return np.sqrt(np.sum((self.x_train-element_of_x)**2,axis=1))
    
    @classmethod
    def perdict(x_test:np.ndarray,self)->np.ndarray:
        labels_pred=[]
        for x_test_element in x_test:
            distances= euclidean_distances(self.x_train,x_test_element)
            distances=np.array(sorted(zip(distances,self.y_train)))
            label_pred=mode(distances[:self.k,1],keepdims=False).mode
            self.y_pred.append(label_pred)
        return  np.ndarray(labels_pred,dtype=np.int64)
    @classmethod
    def accuracy(self) -> float:
        true_positive = (self.y_test == self.y_preds).sum()
        return true_positive / len(self.y_test) * 100
    @classmethod
    def plot_confusion_matrix(self):
        conf_matrix = confusion_matrix(self.y_test,self.y_preds)
        sns.heatmap(conf_matrix,annot=True)
    def k_neighbors(self):
        return self.k




    
    

    

      
        
    
     