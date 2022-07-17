# -*- coding: utf-8 -*-
"""
Created on Sat Jan 29 15:01:50 2022

@author: Piotr
"""

# s = 'azcbobobegghaklbob'
bob_count = 0

for i in range(len(s)):
    if i < (len(s) - 2) and s[i] == "b" and s[i + 1] == "o" and s[i + 2] == "b":
        bob_count += 1
    
        
print("Number of times bob occurs is: " + str(bob_count))

