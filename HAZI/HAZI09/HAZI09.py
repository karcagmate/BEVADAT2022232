import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics import accuracy_score
from scipy.stats import mode
from sklearn.metrics import confusion_matrix
from sklearn.datasets import load_digits
class KMeansOnDigits():

    def __init__(self,n_clusters,random_state) -> None:
        self.n_clusters=n_clusters
        self.random_state=random_state
        

    def load_dataset(self):
        digits=load_digits()
        self.digits=digits
        return self.digits
    
    def predict(self):
        km=KMeans(n_clusters=self.n_clusters,random_state=self.random_state)
        clusters=km.fit_predict(self.digits.data)
        self.clusters=clusters
        return self.clusters
    
    def get_labels(self):
        result=np.zeros_like(self.clusters)
        for cluster in range(10):
            mask=(cluster==self.clusters)
            indices=np.where(mask)[0]
            subarray=self.digits.target[indices]
            mode=np.bincount(subarray).argmax()
            result[mask]=mode
        self.labels=result
        return self.labels
    
    def calc_accuracy(self):
        accuracy=accuracy_score(self.digits.target,self.labels)
        self.accuracy=accuracy
        return round(self.accuracy,2)
    
    def confusion_matrix(self):
        mat=confusion_matrix(self.digits.target,self.labels)
        self.mat=mat
        return self.mat


#km=KMeansOnDigits(10,0)
#km.load_dataset()
#km.predict()
#km.get_labels()
#print(km.calc_accuracy())
