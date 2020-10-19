# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 23:57:08 2020

@author: Jeawills
"""

import os
import csv

budget_file = os.path.join('C:/Users/Jeawills/python_Challenge/Resources/Budget.csv')

data = [ ]
change =[]
net_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 999999999999]

with open(budget_file) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

       # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    first_row =next(csvreader)
    previous_month = int(first_row[1])
            
  #converting each string to the correct data type      

    for row in csvreader:
    #row = [date, profit/losses]
        pro_loss = int(row[1])
        data.append(pro_loss)
        current_month =  int(row[1])

        Monthly_change = (current_month - previous_month)
        change.append(Monthly_change)
        previous_month = current_month
        
        if Monthly_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = Monthly_change
            
        if Monthly_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = Monthly_change

Month_count = len(data)+1
Sum = sum(data) + int(first_row[1])
average = round(sum(change)/len(change),2)
print(average)
print(greatest_increase)
print(greatest_decrease)


output = (
    f"Budget Analysis\n"
    f"----------------------------\n"
    f"Total Months: {Month_count}\n"
    f"Total: ${Sum}\n"
    f"Average  Change: ${average:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")
print(output)

# Set variable for output file
output_path = os.path.join('C:/Users/Jeawills/python_Challenge/Resources/Budget_analysis.csv')


# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the first row (column headers)
    csvwriter.writerow(output)

    # Write the second row
    csvwriter.writerow(['Average', 'Greatest Increase', 'Greatest Decrease'])
   
#with open(Budget_analysis, "w") as csv_file:
    csvfile.write(output)