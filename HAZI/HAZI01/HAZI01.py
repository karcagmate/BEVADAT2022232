# %%
#Create a function that returns with a subsest of a list.
#The subset's starting and ending indexes should be set as input parameters (the list aswell).
#return type: list
#function name must be: subset
#input parameters: input_list,start_index,end_index

# %%
def subset(input_list,start_index,end_index):
    out_list=[]
    for index in range(start_index,end_index):
        out_list.append(input_list[index])
    return out_list

##pl=[1,2,4,5,6]
##subset(pl,0,2)

# %%
#Create a function that returns every nth element of a list.
#return type: list
#function name must be: every_nth
#input parameters: input_list,step_size

# %%
def every_nth(input_list,step_size):
    out_list=[]
    length=len(input_list)
    for index in range(0,length,step_size):
        out_list.append(input_list[index])
    return out_list

##pl=[1,2,4,5,6]
##every_nth(pl,3)

# %%
#Create a function that can decide whether a list contains unique values or not
#return type: bool
#function name must be: unique
#input parameters: input_list

# %%
def unique(input_list):
    unique_list=set(input_list)
    i=len(input_list)
    j=len(unique_list)
    contains= j!=i
    return contains

##pl=[1,2,3,4,1,6,9,10]
##unique(pl)


# %%
#Create a function that can flatten a nested list ([[..],[..],..])
#return type: list
#fucntion name must be: flatten
#input parameters: input_list

# %%
##matrix
def flatten(input_list):
    out_list=[]
    for i in input_list:
     if isinstance(i,list):
        out_list.extend(flatten(i))
     else:
      out_list.append(i)
    return out_list 

##pl=[1, [2, [3, 4], 5], 6]
##latten(pl)


# %%
#Create a function that concatenates n lists
#return type: list
#function name must be: merge_lists
#input parameters: *args


# %%
def merge_lists(*args):
    output_list=[]
    for arg in args:
        output_list.append(arg)
    return output_list
##pl=[1,2,3,4]
##pl2=[5,6,7]
##pl3=[8,9]
##merge_lists(pl,pl2,pl3)


# %%
#Create a function that can reverse a list of tuples
#example [(1,2),...] => [(2,1),...]
#return type: list
#fucntion name must be: reverse_tuples
#input parameters: input_list

# %%
def reverse_tuples(input_list):
    return [tuple(reversed(x)) for x in input_list]

##pl=[(1,2),(3,4),(5,6)]
##reverse_tuples(pl)

# %%
#Create a function that removes duplicates from a list
#return type: list
#fucntion name must be: remove_tuplicates
#input parameters: input_list

# %%



def remove_tuplicates(input_list):
 data=set(input_list)
 out_list=[]
 for datas in data:
  out_list.append(datas)
 return out_list
##pl=[1,2,3,4,1,2,2,2]
##remove_tuplicates(pl)


# %%
#Create a function that transposes a nested list (matrix)
#return type: list
#function name must be: transpose
#input parameters: input_list

# %%
def transpose(input_list):
    transposed=[list(row) for row in zip(*input_list)]
    
    return transposed

##pl=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
##transpose(pl)

# %%
#Create a function that can split a nested list into chunks
#chunk size is given by parameter
#return type: list
#function name must be: split_into_chunks
#input parameters: input_list,chunk_size

# %%
def split_into_chunks(input_list,chunk_size):
    output_list=[]
    for i in range(0,len(input_list),chunk_size):
        output_list.append(input_list[i:i+chunk_size])

    return output_list

##pl = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
##split_into_chunks(pl,1)


# %%
#Create a function that can merge n dictionaries
#return type: dictionary
#function name must be: merge_dicts
#input parameters: *dict

# %%
def merge_dicts(*dict):
    output_dict={}
    for d in dict:
        output_dict.update(d)
    return output_dict

##pl1={'a':'1'}
##pl2={'b':'2'}
##merge_dicts(pl1,pl2)


# %%
#Create a function that receives a list of integers and sort them by parity
#and returns with a dictionary like this: {"even":[...],"odd":[...]}
#return type: dict
#function name must be: by_parity
#input parameters: input_list

# %%
def by_parity(input_list):
    even=[]
    odd=[]
    for i in input_list:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
    return {"even":even,"odd":odd}

##pl=[1,2,3,4,5,6,7,8,9,10]
##by_parity(pl)

# %%
#Create a function that receives a dictionary like this: {"some_key":[1,2,3,4],"another_key":[1,2,3,4],....}
#and return a dictionary like this : {"some_key":mean_of_values,"another_key":mean_of_values,....}
#in short calculates the mean of the values key wise
#return type: dict
#function name must be: mean_key_value
#input parameters: input_dict

# %%
def mean_key_value(input_dict):
    output_dict={}
    for key,list in input_dict.items():
        output_dict[key]=sum(list)/len(list)
    return output_dict

    
##pl={"some_key":[1,2,3,4],"another_key":[1,2,3,4]}
##mean_key_value(pl)

# %%
#If all the functions are created convert this notebook into a .py file and push to your repo


