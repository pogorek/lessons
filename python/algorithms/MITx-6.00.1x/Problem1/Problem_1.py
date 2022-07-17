# -*- coding: utf-8 -*-
"""
Created on Fri Jan 28 03:24:31 2022

@author: Piotr
"""
s = 'azcbobobegghakl'

vowels = ['a', 'e', 'i', 'o', 'u']

v = 0

for letter in s:
    if letter in vowels:
        v += 1
        
print("Number of vowels: " + str(v))