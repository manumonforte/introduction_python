# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 09:34:42 2018

@author: Manu

TYPES OF VARIABLES

"""

#***********STRINGS*******************

#%%
#Use formate in order to crate a template
name= "Manuel"
city= "Avila (Spain)"

template = "I'm {}, I live in {}".format(name,city)

print(template)
#%%
#Operations with Strings

str1 = "i'm programming in PYTHON"
print(str1.upper())
print(str1.lower())
print(str1.capitalize())

str2 = "use split in order to separte words"
print(str2)
str2 = str2.split(" ")
print(str2)
#%%

#***************NUMBERS******************************

#types of numbers

num1 = 1
num2 = 2.0

print(num1,type(num1))

print (num2*65,type(num2))

#cast from int to float
print(int(num2))
print(float(num1))

#Operations

print(5+5)
print(5-5)

rest = 5%5
print(f"Rest of operation 5/5 is : {rest}",rest)

#%%

#*****************BOOLEANS*****************************
t= True
f = False

none = None

print(type(none))
print("The variable t is",t is True)
num1 = 5
num2 = 6

print(f"{num1} >= {num2} i ",num1 >=num2)

print(f"{num1} >= {num2} or {num1} <= {num2} is",num1 >=num2 or num1 <=num2)

#%%
