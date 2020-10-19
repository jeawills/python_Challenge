# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 22:15:45 2020

@author: Jeawills
"""

import os 
import csv

# %% Path to collect data from the Resources folder
wrestling_csv = os.path.join("C:/Users/Jeawills/python_Challenge/Mini assignment/Resources/WrestlingData.csv")

# %% defining functions 
def print_percentages(WrestlingData):
    #assigning variables 
    name = str(WrestlingData[0])
    wins = int(WrestlingData[1])
    losses = int(WrestlingData[2])
    draws = int(WrestlingData[3])

    # Total equals wins + losses + draws 
    total = wins + losses + draws

    # Winning percentage 
    winpercent = (wins / total) * 100

    # Lossing percentage
    losspercent = (losses / total) * 100

    # Draw percentage
    drawpercent = (draws / total) * 100

    # setitng conditions for "Jobber" or "Superstar".
    if losspercent > 50:
        wrestlertype = "Jobber"
    else:
        wrestlertype = "Superstar"

    # Output percentage stats
    print(f"Stats for {name}")
    print(f"Percent of Games Won: {winpercent}")
    print(f"Percent of Games lost: {losspercent}")
    print(f"Percent of Games draw: {drawpercent}")
    print(f"{name} is a {wrestlertype}")

# %% Read in the CSV file
with open(wrestling_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    # Prompt the user for what wrestler they would like to search for
    name_to_check = input("What wrestler do you want to look for? ")

    # Loop through the data
    for row in csvreader:

        # If the wrestler's name in a row is equal to that which the user input, run the 'print_percentages()' function
        if name_to_check == row[0]:
            print_percentages(row)
