# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 23:51:10 2022

@author: Piotr
"""

animals = {'u': [10, 15, 5, 2, 6], 'B': [15]}


def how_many(dic):
    values_count = 0
    
    for item in dic:
        if isinstance(dic[item], list):
            values_count += len(dic[item])
        else:
            values_count += 1
        
    return values_count 
   
print(how_many(animals))