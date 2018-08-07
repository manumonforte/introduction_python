# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 16:11:12 2018

@author: Manu
"""

#%%
#LIST IN PYTHON

fruits = ["orange" , "watermelon" , "apple", "banana", "strawberry"]

print(fruits[2])
print (fruits[::2])

#%%
fruits.pop(fruits.index("apple"))
print(fruits)

#%%
fruits.sort()
print(fruits)
#%%
print(fruits[::-1])
print(list(range(100)))

#%%
#TUPLES IN PYTHON

sisters = ("Anne", "Helen", "Iris")
print(sisters.count("Iris"))
boolean = sisters.__contains__("Anne")
print(boolean is True)

##ERROR, can't modify tuples

sisters[0]= "ad"

#%%
#MAPS IN PYTHON
bookMap = {
        "The Revenge" : 10,
        "The Chair" : 8,
        }
print(bookMap.keys())
print(bookMap["The Chair"])


#%%
#EXERCISES
#1) 
weekMap = {
        "Monday": 1,
        "Tuesday" : 2,
        "Wednesday" : 3,
        }
print(weekMap)

#%%
#2)

weekMap["MONDAY"]=weekMap.pop("Monday")
weekMap["TUESDAY"]=weekMap.pop("Tuesday")
weekMap["WEDNESDAY"]=weekMap.pop("Wednesday")
print(weekMap)


