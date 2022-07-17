# -*- coding: utf-8 -*-
"""
Created on Sat Feb 12 01:29:54 2022

@author: Piotr
"""
from math import floor

low = 0
high = 100
guess = 0
ans = ""

print("Please think of a number between 0 and 100!")

while True:
    guess = floor((high + low) / 2)
    print("Is your secret number {}?".format(guess))
    ans = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    if ans == 'h':
        high = guess
    elif ans == 'l':
        low = guess
    elif ans == 'c':
        print("Game over. Your secret number was: {}".format(guess))
        break
    else:
        print("Sorry, I did not understand your input.")
