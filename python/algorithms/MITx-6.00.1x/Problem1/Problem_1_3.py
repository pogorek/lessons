# -*- coding: utf-8 -*-
"""
Created on Sat Jan 29 19:57:19 2022

@author: Piotr
"""

s = 'vbnizqouxz'
# Longest substring in alphabetical order is: beggh

temp = s[0]
longest = ""
#  i < (len(s)) and 

for i in range(len(s) - 1):
    # if len(temp) == 0:
    #     temp = s[i]
        
    if s[i] <= s[i + 1]:
        temp += s[i + 1]
    else:
        if len(temp) > len(longest):
            longest = temp
        temp = s[i + 1]
        
if len(temp) > len(longest):
    longest = temp
            
print("Longest substring in alphabetical order is: " + longest)