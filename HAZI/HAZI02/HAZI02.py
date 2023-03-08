# %%
import numpy as np

# Írj egy olyan fügvényt, ami megfordítja egy 2d array oszlopait
# Be: [[1,2],[3,4]]
# Ki: [[2,1],[4,3]]
# column_swap()
def column_swap(input:np.array)->np.array:
    return np.fliplr(input)

#pl=np.array([[1,2],[3,4]])
#column_swap(pl)

# %%
#Készíts egy olyan függvényt ami összehasonlít két array-t és adjon vissza egy array-ben, hogy hol egyenlőek 
# Pl Be: [7,8,9], [9,8,7] 
# Ki: [1]
# compare_two_array()
# egyenlő elemszámúakra kell csak hogy működjön
def compare_two_array(input1:np.array,input2:np.array)->np.array:
   out=np.where(np.equal(input1,input2))
   return out  
#pl1=np.array([7,8,9])
#pl2=np.array([9,8,7] )
#compare_two_array(pl1,pl2)


 # %%
#Készíts egy olyan függvényt, ami vissza adja a megadott array dimenzióit:
# Be: [[1,2,3], [4,5,6]]
# Ki: "sor: 2, oszlop: 3, melyseg: 1"
# get_array_shape()
# 3D-vel még műküdnie kell!
def get_array_shape(input:np.array):
    shape=input.shape
    #print(len(shape))
    if len(shape)==1:
        return f"sor: 1, oszlop: {shape[0]}, melyseg: 1"
    elif len(shape)==2:
        return f"sor: {shape[0]}, oszlop: {shape[1]}, melyseg: 1"
    elif len(shape)==3:
        return f"sor: {shape[0]}, oszlop: {shape[1]}, melyseg: {shape[2]}"
    

#pl=np.array([[1,2,3], [4,5,6]])
#get_array_shape(pl)

# %%
# Készíts egy olyan függvényt, aminek segítségével elő tudod állítani egy neurális hálózat tanításához szükséges Y-okat egy numpy array-ből. 
#Bementként add meg az array-t, illetve hogy mennyi class-od van. Kimenetként pedig adjon vissza egy 2d array-t, ahol a sorok az egyes elemek. Minden nullákkal teli legyen és csak ott álljon egyes, ahol a bementi tömb megjelöli
# Be: [1, 2, 0, 3], 4
# Ki: [[0,1,0,0], [0, 0, 1, 0], [1, 0, 0, 0], [0, 0, 0, 1]]
# encode_Y()
def encode_Y(input:np.array,class_num:int)->np.array:
    num_sample=input.shape[0]
    helper=np.zeros((num_sample,class_num))
    for i in range(num_sample):
        helper[i,int(input[i])]=1
    return helper

#pl=np.array([1, 2, 0, 3])
#print(encode_Y(pl,4))

# %%
# A fenti feladatnak valósítsd meg a kiértékelését. Adj meg a 2d array-t és adj vissza a decodolt változatát
# Be:  [[0,1,0,0], [0, 0, 1, 0], [1, 0, 0, 0], [0, 0, 0, 1]]
# Ki:  [1, 2, 0, 3]
# decode_Y()
def decode_Y(input:np.array)->np.array:
    return np.argmax(input,axis=1)

#pl=np.array([[0,1,0,0], [0, 0, 1, 0], [1, 0, 0, 0], [0, 0, 0, 1]])
#decode_Y(pl)

# %%
# Készíts egy olyan függvényt, ami képes kiértékelni egy neurális háló eredményét! Bemenetként egy listát és egy array-t és adja vissza a legvalószínübb element a listából.
# Be: ['alma', 'körte', 'szilva'], [0.2, 0.2, 0.6]. 
# Ki: 'szilva'
# eval_classification()
def eval_classification(input1:list, input2:np.array)->str:
    index=np.argmax(input2)
    return input1[index]

#pl1=['alma', 'körte', 'szilva']
#pl2=np.array([0.2, 0.2, 0.6])
#eval_classification(pl1,pl2)



# %%
# Készíts egy olyan függvényt, ahol az 1D array-ben a páratlan számokat -1-re cseréli
# Be: [1,2,3,4,5,6]
# Ki: [-1,2,-1,4,-1,6]
# repalce_odd_numbers()
def replace_odd_numbers(input:np.array)->np.array:
    return np.where(input%2==1,-1,input)

#pl=np.array([1,2,3,4,5,6])
#replace_odd_numbers(pl)

# %%
# Készíts egy olyan függvényt, ami egy array értékeit -1 és 1-re változtatja, attól függően, hogy az adott elem nagyobb vagy kisebb a paraméterként megadott számnál.
# Ha a szám kisebb mint a megadott érték, akkor -1, ha nagyobb vagy egyenlő, akkor pedig 1.
# Be: [1, 2, 5, 0], 2
# Ki: [-1, 1, 1, -1]
# replace_by_value()
def replace_by_value(input:np.array,treshold:int)->np.array:
    input[input<treshold]=-1
    input[input>=treshold]=1
    return input

#pl=np.array([1, 2, 5, 0])
#replace_by_value(pl,2)


# %%
# Készítsd egy olyan függvényt, ami az array értékeit összeszorozza és az eredmény visszaadja
# Be: [1,2,3,4]
# Ki: 24
# array_multi()
# Ha több dimenziós a tömb, akkor az egész tömb elemeinek szorzatával térjen vissza
def array_multi(input:np.array):
    return np.prod(input)

#pl=np.array([1,2,3,4])
#array_multi(pl)

# %%
# Készítsd egy olyan függvényt, ami a 2D array értékeit összeszorozza és egy olyan array-el tér vissza, aminek az elemei a soroknak a szorzata
# Be: [[1, 2], [3, 4]]
# Ki: [2, 12]
# array_multi_2d()
def array_multi_2d(input:np.array)->np.array:
    rows=np.prod(input,axis=1)
    return rows

#pl=np.array([[1, 2], [3, 4]])
#array_multi_2d(pl)

# %%
# Készíts egy olyan függvényt, amit egy meglévő numpy array-hez készít egy bordert nullásokkal. Bementként egy array-t várjon és kimenetként egy array jelenjen meg aminek van border-je
# Be: [[1,2],[3,4]]
# Ki: [[0,0,0,0],[0,1,2,0],[0,3,4,0],[0,0,0,0]]
# add_border()
def add_border(input:np.array)->np.array:
    ori=input.shape
    border=(ori[0]+2,ori[1]+2)
    out=np.zeros(border)
    out[1:-1,1:-1]=input
    return out

#pl=np.array([[1,2],[3,4]])
#add_border(pl)

# %%
# Készíts egy olyan függvényt ami két dátum között felsorolja az összes napot.
# Be: '2023-03', '2023-04'
# Ki: ['2023-03-01', '2023-03-02', .. , '2023-03-31',]
# list_days()
from datetime import timedelta,datetime
def list_days(start,finish):
    starter = datetime.strptime(start, '%Y-%m')
    end = datetime.strptime(finish, '%Y-%m')
    delta=timedelta(days=1)
    out=[]
    while starter<=end:
        out.append(starter.strftime('%Y-%m-%d'))
        starter+=delta
    return out

#starti='2023-03'
#fin='2023-04'
#list_days(starti,fin)




# %%
 #Írj egy fügvényt ami vissza adja az aktuális dátumot az alábbi formában: YYYY-MM-DD
# Be:
# Ki: 2017-03-24 
from datetime import datetime
def datetime_now():
    return datetime.now().strftime('%Y-%m-%d')

#datetime_now()

# %%
# Írj egy olyan függvényt ami visszadja, hogy mennyi másodperc telt el 1970 január 01. 00:00:00 óta.
# Be: 
# Ki: másodpercben az idó, int-é kasztolva
# sec_from_1970()
import time
def sec_from_1970()->int:
    return int(time.time())

#sec_from_1970()


