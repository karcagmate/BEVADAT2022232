# %%
#Create a function that decides if a list contains any odd numbers.
#return type: bool
#function name must be: contains_odd
#input parameters: input_list

# %%
def  contains_odd(input_list):
  
  i=0
  while((i<len(input_list)) and (not (input_list[i]%2!=0))):
   i+=1
  odd=(i<len(input_list))
  return odd
  
##listi=[2,10,1,8,4]
##contains_odd(listi)

# %%


# %%
#Create a function that accepts a list of integers, and returns a list of bool.
#The return list should be a "mask" and indicate whether the list element is odd or not.
#(return should look like this: [True,False,False,.....])
#return type: list
#function name must be: is_odd
#input parameters: input_list

# %%
def is_odd(input_list):
 mask=[]
 for index in range(len(input_list)):
   if input_list[index]%2==0:
    ##mask[index]=False
    mask.append(False)
   else:
    ##mask[index]=True
    mask.append(True)
 return mask


##listi=[10,2,3,4,5,6,7,8]
##is_odd(listi)



# %%

#Create a function that accpects 2 lists of integers and returns their element wise sum. <br>
#(return should be a list)
#return type: list
#function name must be: element_wise_sum
#input parameters: input_list_1, input_list_2

# %%
def element_wise_sum(input_list_1, input_list_2):
    output_list=[]
    for index1 in range(len(input_list_1)) :
       output_list.append(input_list_1[index1]+input_list_2[index1])
        
           
    return output_list

##list1=[1,2,3,4,5]
##list2=[4,6,8,10,12]
##element_wise_sum(list1,list2)

# %%
#Create a function that accepts a dictionary and returns its items as a list of tuples
#(return should look like this: [(key,value),(key,value),....])
#return type: list
#function name must be: dict_to_list
#input parameters: input_dict

# %%
def dict_to_list(input_dict):
    list_help=[]
    for key,value in input_dict.items():
        list_help.append(f"({key},{value})")
    _tuple=tuple(list_help)
    return _tuple

##person = {
  ##  'first_name': 'John',
   ## 'last_name': 'Doe',
   ## 'age': 25,
   ## 'favorite_colors': ['blue', 'green'],
   ## 'active': True
##}
##dict_to_list(person)

# %%
#If all the functions are created convert this notebook into a .py file and push to your repo


