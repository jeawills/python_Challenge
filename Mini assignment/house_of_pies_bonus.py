# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 11:30:26 2020

@author: Jeawills
"""

# The list of pies to print to the screen
pie_list = [
    "Pecan",
    "Apple Crisp",
    "Bean",
    "Banoffee",
    "Black Bun",
    "Blueberry",
    "Buko",
    "Burek",
    "Tamale",
    "Steak"
]
# %%
i = 0
print(f'Welcome to the House of Pies! Here are our pies')
for pie in pie_list:
    if i <= len(pie_list):
        pie_list[i] = str(f"({i+1}) {pie_list[i]}")
        print(pie_list[i])
        i += 1
#%%
more = "yes"
cart = []
n_pie_cart = []
while more in ("yes", "y"):
   choices = int(input("Please select the pie you'd like to buy: "))
   n_pies = int(input("How many of that would you like? "))
   cart.append(pie_list[choices -1][4:])
   n_pie_cart.append(f"{n_pies} {pie_list[choices - 1][4:]}")
   print(f"Great! We'll have {n_pies} {pie_list[choices - 1][4:]} pie(s) right out for you.")
   more = input("Would you like anything else? ").lower()
for i in range(len(pie_list)):
    if pie_list[i][4:] not in cart:
        n_pie_cart.append(f"0 {pie_list[i][4:]}")
print("You have ordered: ")
for i in range(len(pie_list)):                   
    print(n_pie_cart[i])
print("Thanks for shopping with us!")