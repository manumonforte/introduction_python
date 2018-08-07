# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 11:52:10 2018

@author: Manu
"""

#FUNCTIONS

#%%

def resta(a,b):
    return a-b 
print (resta(8,5))
#%%
user = input ("Enter a word in order to transform in lower:")
minus = lambda mayus : mayus.lower()
print (minus(user))
#%%
def option (a,b,opt):
    if opt == "suma":
        return a+b
    elif opt == "resta":
        return a-b
    else:
        raise Exception ("You must check resta or suma")
    
print (option(5,3,"suma"))
print (option(5,3,"resta"))
print (option(5,3,"a"))

#%%

def invSentence(line):
    lista = line.split(" ")
    print(lista[::-1])
    
user = input ("Enter a sentence:")
invSentence(user)

