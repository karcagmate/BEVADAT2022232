# %%
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# %%
'''
FONTOS: Az első feladatáltal visszaadott DataFrame-et kell használni a további feladatokhoz. 
A függvényeken belül mindig készíts egy másolatot a bemenő df-ről, (new_df = df.copy() és ezzel dolgozz tovább.)
'''

# %%
'''
Készíts egy függvényt, ami egy string útvonalat vár paraméterként, és egy DataFrame ad visszatérési értékként.

Egy példa a bemenetre: 'test_data.csv'
Egy példa a kimenetre: df_data
return type: pandas.core.frame.DataFrame
függvény neve: csv_to_df
'''

# %%
def csv_to_df(path:str)->pd.DataFrame:
   data=pd.read_csv(path)
   return data
#path="~\Desktop\StudentsPerformance (1).csv"
#test=csv_to_df(path)
#test.head()
#jó






# %%
'''
Készíts egy függvényt, ami egy DataFrame-et vár paraméterként, 
és átalakítja azoknak az oszlopoknak a nevét nagybetűsre amelyiknek neve nem tartalmaz 'e' betüt.

Egy példa a bemenetre: df_data
Egy példa a kimenetre: df_data_capitalized
return type: pandas.core.frame.DataFrame
függvény neve: capitalize_columns
'''

# %%
def capitalize_columns(data:pd.DataFrame)->pd.DataFrame:
    newdata=data.copy()
    newcol=[]
    for col in newdata.columns:
        if 'e' not in col:
            newcol.append(col.upper())
        else:
         newcol.append(col)
    newdata.columns=newcol
    return newdata

#capit=capitalize_columns(test)
#capit.head()
#jó



    



    
    
   

# %%
'''
Készíts egy függvényt, ahol egy szám formájában vissza adjuk, hogy hány darab diáknak sikerült teljesíteni a matek vizsgát.
(legyen az átmenő ponthatár 50).

Egy példa a bemenetre: df_data
Egy példa a kimenetre: 5
return type: int
függvény neve: math_passed_count
'''

# %%
def math_passed_count(data:pd.DataFrame)->int:
    newdata=data.copy()
    num=newdata['math score'].where(lambda x:(x>=50))
    return num.count()

#mathpassed=math_passed_count(test)
#print(mathpassed)
#jó




# %%
'''
Készíts egy függvényt, ahol Dataframe ként vissza adjuk azoknak a diákoknak az adatait (sorokat), akik végeztek előzetes gyakorló kurzust.

Egy példa a bemenetre: df_data
Egy példa a kimenetre: df_did_pre_course
return type: pandas.core.frame.DataFrame
függvény neve: did_pre_course
'''

# %%
def did_pre_course(data:pd.DataFrame)->pd.DataFrame:
    newdata=data.copy()
    filtered=newdata.loc[np.where(newdata['test preparation course']=="completed")]
    return filtered

#did_pre_course(test)
#jó


# %%
'''
Készíts egy függvényt, ahol a bemeneti Dataframet a diákok szülei végzettségi szintjei alapján csoportosításra kerül,
majd aggregációként vegyük, hogy átlagosan milyen pontszámot értek el a diákok a vizsgákon.

Egy példa a bemenetre: df_data
Egy példa a kimenetre: df_average_scores
return type: pandas.core.frame.DataFrame
függvény neve: average_scores
'''

# %%
def average_scores(data:pd.DataFrame)->pd.DataFrame:
    newdata=data.copy()
    return newdata.groupby('parental level of education').aggregate({'math score': 'mean',
                                                                     'reading score': 'mean',
                                                                     'writing score': 'mean'})

#average_scores(test)
#jó


# %%
'''
Készíts egy függvényt, ami a bementeti Dataframet kiegészíti egy 'age' oszloppal, töltsük fel random 18-66 év közötti értékekkel.
A random.randint() függvényt használd, a random sorsolás legyen seedleve, ennek értéke legyen 42.

Egy példa a bemenetre: df_data
Egy példa a kimenetre: df_data_with_age
return type: pandas.core.frame.DataFrame
függvény neve: add_age
'''

# %%
import random
def add_age(data:pd.DataFrame)->pd.DataFrame:
    newdata=data.copy()
    
    random.seed(42)
    ages=[random.randint(17,67) for _ in range(len(newdata))]
    newdata['age']=ages
    return newdata

#age=add_age(test)
#age.head()



# %%
'''
Készíts egy függvényt, ami vissza adja a legjobb teljesítményt elérő női diák pontszámait.

Egy példa a bemenetre: df_data
Egy példa a kimenetre: (99,99,99) #math score, reading score, writing score
return type: tuple
függvény neve: female_top_score
'''

# %%
def female_top_score(data:pd.DataFrame)->tuple:
    newdata=data.copy()
    filtered=newdata.loc[np.where(newdata['gender']=="female")]
    filtered['sumscore']=filtered['math score']+filtered['reading score']+filtered['writing score']
    index=np.argmax(filtered['sumscore'])
    best=filtered.iloc[index]
    out=(best['math score'],best['reading score'],best['writing score'])
    return out
     
#female=female_top_score(test)
#print(female)
#jó


# %%
'''
Készíts egy függvényt, ami a bementeti Dataframet kiegészíti egy 'grade' oszloppal. 
Számoljuk ki hogy a diákok hány százalékot ((math+reading+writing)/300) értek el a vizsgán, és osztályozzuk őket az alábbi szempontok szerint:

90-100%: A
80-90%: B
70-80%: C
60-70%: D
<60%: F

Egy példa a bemenetre: df_data
Egy példa a kimenetre: df_data_with_grade
return type: pandas.core.frame.DataFrame
függvény neve: add_grade
'''

# %%
def add_grade(data:pd.DataFrame)->pd.DataFrame:
    newdata=data.copy()
    newdata['grade']=(newdata['math score']+newdata['reading score']+newdata['writing score'])/300
    knewdata=newdata
    for i in range(len(knewdata)):
        if knewdata['grade'][i]>=0.9:
            knewdata['grade'][i]='A'
        elif knewdata['grade'][i]<0.9 and knewdata['grade'][i]>=0.8:
            knewdata['grade'][i]='B'
        elif knewdata['grade'][i]<0.8 and knewdata['grade'][i]>=0.7:
            knewdata['grade'][i]='C'
        elif knewdata['grade'][i]<0.7 and knewdata['grade'][i]>=0.6:
            knewdata['grade'][i]='D'
        else:
            knewdata['grade'][i]='F'

    return knewdata

#graded=add_grade(test)
#graded.head()
#jó



# %%
'''
Készíts egy függvényt, ami a bemeneti Dataframe adatai alapján elkészít egy olyan oszlop diagrammot,
ami vizualizálja a nemek által elért átlagos matek pontszámot.

Oszlopdiagram címe legyen: 'Average Math Score by Gender'
Az x tengely címe legyen: 'Gender'
Az y tengely címe legyen: 'Math Score'

Egy példa a bemenetre: df_data
Egy példa a kimenetre: fig
return type: matplotlib.figure.Figure
függvény neve: math_bar_plot
'''

# %%
def math_bar_plot(data:pd.DataFrame)->plt.figure:
    newdata=data.copy()
    scores=newdata.groupby('gender')['math score'].mean()
    fig,ax=plt.subplots()
    ax.bar(scores.index,scores.values)
    ax.set_xlabel('Gender')
    ax.set_ylabel('Math score')
    ax.set_title('Average Math Score by Gender')
    return fig

#math_bar_plot(test)


# %%
''' 
Készíts egy függvényt, ami a bemeneti Dataframe adatai alapján elkészít egy olyan histogramot,
ami vizualizálja az elért írásbeli pontszámokat.

A histogram címe legyen: 'Distribution of Writing Scores'
Az x tengely címe legyen: 'Writing Score'
Az y tengely címe legyen: 'Number of Students'

Egy példa a bemenetre: df_data
Egy példa a kimenetre: fig
return type: matplotlib.figure.Figure
függvény neve: writing_hist
'''

# %%
def writing_hist(data:pd.DataFrame)->plt.figure:
    newdata=data.copy()
    fig,ax=plt.subplots()
    ax.hist(newdata['writing score'], bins=10)
    ax.set_xlabel('Writing Score')
    ax.set_ylabel('Number of Students')
    ax.set_title('Distribution of Writing Scores')
    return fig

#writing_hist(test)
#jó
    

# %%
''' 
Készíts egy függvényt, ami a bemeneti Dataframe adatai alapján elkészít egy olyan kördiagramot,
ami vizualizálja a diákok etnikum csoportok szerinti eloszlását százalékosan.

Érdemes megszámolni a diákok számát, etnikum csoportonként,majd a százalékos kirajzolást az autopct='%1.1f%%' paraméterrel megadható.
Mindegyik kör szelethez tartozzon egy címke, ami a csoport nevét tartalmazza.
A diagram címe legyen: 'Proportion of Students by Race/Ethnicity'

Egy példa a bemenetre: df_data
Egy példa a kimenetre: fig
return type: matplotlib.figure.Figure
függvény neve: ethnicity_pie_chart
'''

# %%
def ethnicity_pie_chart(data:pd.DataFrame)->plt.figure:
    newdata=data.copy()
    distribution=newdata['race/ethnicity'].value_counts()
    #print(distribution)
    #distribution=newdata.('race/ethnicity').value_counts(normalize=True)
    fig,ax=plt.subplots()
    ax.pie(distribution.values,labels=distribution.index,autopct='%1.1f%%')
    ax.set_title('Proportion of Students by Race/Ethnicity')
    return fig

#ethnicity_pie_chart(test)

    



# %%
