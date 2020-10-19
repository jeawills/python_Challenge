# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 00:13:55 2020

@author: Jeawills
"""
   
   
# Initial variable to track game play
play = "y"

# Still playing...
while play == "y":

    # user input for number
    number = int(input("How many numbers? "))

    # Loop through the number. 
    for x in range(number):

        # Print each number in the range
        print(x)

    # Once complete...
    play = input("Do you want to continue to play? (y)es or (n)o? ")

if play == "n":
    print ("Goodbye, thanks for playing!") 


