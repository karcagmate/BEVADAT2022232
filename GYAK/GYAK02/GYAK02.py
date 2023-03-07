# %%
import numpy as np
#FONTOS!!!
#  CSAK OTT LEHET HASZNÁLNI FOR LOOP-OT AHOL A FELADAT KÜLÖN KÉRI!
#Készíts egy függvényt ami létre hoz egy nullákkal teli numpy array-t.
#Paraméterei: mérete (tupel-ként), default mérete pedig legyen egy (2,2)
#Be: (2,2)
#Ki: [[0,0],[0,0]]
#create_array()
def create_array(input: tuple)->np.array:
    
    arr=np.zeros(input)
    return arr

    
    
#input=(2,2)
#create_array(input)





# %%
#Készíts egy függvényt ami a paraméterként kapott array-t főátlót feltölti egyesekkel
#Be: [[1,2],[3,4]]
#Ki: [[1,2],[3,1]]
#set_one()
def set_one(input:np.array)->np.array:
   out= np.fill_diagonal(input, 1)
   return out

#proba=np.array([[1,5],[3,5]])
#print(set_one(proba))

# %%
# Transzponáld a paraméterül kapott mártix-ot:
# Be: [[1, 2], [3, 4]]
# Ki: [[1, 2], [3, 4]]
# do_transpose()
def do_transponse(input:np.array)->np.array:
    out=np.transpose(input)
    return out

#proba=np.array([[1, 2], [5, 6]])
#do_transponse(proba)

# %%
# Készíts egy olyan függvényt ami az array-ben lévő értékeket N tizenedjegyik kerekíti, alapértelmezetten 
# Be: [0.1223, 0.1675], n = 2
# Ki: [0.12, 0.17]
# round_array()
def round_array(input:np.array,num:int)->np.array:
    out_array=np.round(input,num)
    return out_array

#proba=np.array([0.1223, 0.1675])
#round_array(proba,2)


# %%
# Készíts egy olyan függvényt, ami a bementként  0 és 1 ből álló tömben a 0 - False-ra az 1 True-ra cserélni
# Be: [[1, 0, 0], [1, 1, 1],[0, 0, 0]]
# Ki: [[ True False False], [ True  True  True], [False False False]]
# bool_array()
def bool_array(inarray:np.array)->np.array:
    newarr=inarray.astype(bool)
    
    return newarr
#proba=np.array([[1, 0, 0], [1, 1, 1],[0, 0, 0]])
#bool_array(proba)
    


# %%
# Készíts egy olyan függvényt, ami a bementként  0 és 1 ből álló tömben a 1 - False-ra az 0 True-ra cserélni
# Be: [[1, 0, 0], [1, 1, 1],[0, 0, 0]]
# Ki: [[ True False False], [ True  True  True], [False False False]]
# invert_bool_array()
def invert_bool_array(array:np.array)->np.array:
    newarr =np.invert (array.astype(bool))
    
    return newarr

#proba=np.array([[1, 0, 0], [1, 1, 1],[0, 0, 0]])
#invert_bool_array(proba)

# %%

# Készíts egy olyan függvényt ami a paraméterként kapott array-t kilapítja
# Be: [[1,2], [3,4]]
# Ki: [1,2,3,4]
# flatten()
def flatten(input:np.array)->np.array:
    out=input.reshape(-1)
    return out

#proba=np.array([[1,2], [3,4]])
#flatten(proba)
    



