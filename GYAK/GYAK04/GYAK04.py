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
Készíts egy függvényt ami a bemeneti dictionary-ből egy DataFrame-et ad vissza.

Egy példa a bemenetre: test_dict
Egy példa a kimenetre: test_df
return type: pandas.core.frame.DataFrame
függvény neve: dict_to_dataframe
'''
def dict_to_dataframe(test_dict:dict):
    test_dict=pd.DataFrame(test_dict)
    return test_dict


    

# %%
stats = {"country": ["Brazil", "Russia", "India", "China", "South Africa"],
       "capital": ["Brasilia", "Moscow", "New Dehli", "Beijing", "Pretoria"],
       "area": [8.516, 17.10, 3.286, 9.597, 1.221],
       "population": [200.4, 143.5, 1252, 1357, 52.98] }

#dict_to_dataframe(stats)

# %%
'''
Készíts egy függvényt ami a bemeneti DataFrame-ből vissza adja csak azt az oszlopot amelynek a neve a bemeneti string-el megegyező.

Egy példa a bemenetre: test_df, 'area'
Egy példa a kimenetre: test_df
return type: pandas.core.series.Series
függvény neve: get_column
'''

# %%
def get_column(df:pd.DataFrame,column:str)-> pd.core.series.Series:
    newdf=df.copy()
    cl=newdf[column]
    return cl
#get_column(dict_to_dataframe(stats),'country')

# %%
'''
Készíts egy függvényt ami a bemeneti DataFrame-ből vissza adja a két legnagyobb területű országhoz tartozó sorokat.

Egy példa a bemenetre: test_df
Egy példa a kimenetre: test_df
return type: pandas.core.frame.DataFrame
függvény neve: get_top_two
'''

# %%
#testing=dict_to_dataframe(stats)
def get_top_two(test_df:pd.DataFrame)->pd.DataFrame:
    newdf=test_df.copy()
    df_sorted = newdf.sort_values(by='area', ascending=False)
    return df_sorted.iloc[:2]

#get_top_two(testing)

# %%
'''
Készíts egy függvényt ami a bemeneti DataFrame-ből kiszámolja az országok népsűrűségét és eltárolja az eredményt egy új oszlopba ('density').
(density = population / area)

Egy példa a bemenetre: test_df
Egy példa a kimenetre: test_df
return type: pandas.core.frame.DataFrame
függvény neve: population_density
'''

# %%
def population_density(test:pd.DataFrame)->pd.DataFrame:
    newdf=test.copy()
    density=newdf["population"]/newdf["area"]
    newdf["density"]=density
    return newdf

#population_density(testing)

# %%
'''
Készíts egy függvényt, ami a bemeneti Dataframe adatai alapján elkészít egy olyan oszlopdiagramot (bar plot),
ami vizualizálja az országok népességét.

Az oszlopdiagram címe legyen: 'Population of Countries'
Az x tengely címe legyen: 'Country'
Az y tengely címe legyen: 'Population (millions)'

Egy példa a bemenetre: test_df
Egy példa a kimenetre: fig
return type: matplotlib.figure.Figure
függvény neve: plot_population
'''

# %%
def plot_population(df:pd.DataFrame)->plt.figure:
    newdf=df.copy()
    fig,ax=plt.subplots()
    ax.bar(newdf["country"],newdf["population"])
    ax.set_xlabel('Country')
    ax.set_ylabel('Population (millions)')
    ax.set_title('Population of Countries')
    return fig

#plot_population(testing)


# %%
'''
Készíts egy függvényt, ami a bemeneti Dataframe adatai alapján elkészít egy olyan kördiagramot,
ami vizualizálja az országok területét. Minden körcikknek legyen egy címe, ami az ország neve.

Az kördiagram címe legyen: 'Area of Countries'

Egy példa a bemenetre: test_df
Egy példa a kimenetre: fig
return type: matplotlib.figure.Figure
függvény neve: plot_area
'''

# %%
def plot_area(df:pd.DataFrame)->plt.figure:
    newdf=df.copy()
    fig,ax=plt.subplots()
    ax.pie(newdf['area'],labels=newdf['country'])
    
    ax.set_title('Area of Countries')
    return fig

#plot_area(testing)


