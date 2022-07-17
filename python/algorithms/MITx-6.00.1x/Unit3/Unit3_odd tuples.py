# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 23:53:39 2022

@author: Piotr
"""

def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    # Your Code Here
    new_tuple = []
    
    for i in range(len(aTup)):
        if i % 2 == 0:
            new_tuple.append(aTup[i])
            
    new_tuple = tuple(new_tuple)
    return new_tuple

print(oddTuples(('I', 'am', 'a', 'test', 'tuple')))