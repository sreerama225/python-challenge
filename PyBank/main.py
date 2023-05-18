# import modules for OS and CSV

import os
import csv

# variables declaration
total_months = 0
total_profit_loss = 0
profit_loss = 0
past_month_profit_loss = 0
profit_loss_change = 0
greatest_increase_profits = 0
greatest_decrease_profits = 0

months = []
profit_loss_changes = []

# Set the file path
csvpath = os.path.join('Resources','budget_data.csv')

# open the csv file from the above path and read it to process further
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    for row in csvreader:
        # total number of months
        total_months = total_months+1

        # read the profit/loss from column1 for each row and add it to the total variable
        profit_loss = int(row[1])
        total_profit_loss = profit_loss + total_profit_loss

        # skip the first month from profit loss change calculation
        if(total_months == 1):
            past_month_profit_loss = profit_loss
        
        else:
            # calculate the profit loss change from second month onwards
            profit_loss_change = profit_loss - past_month_profit_loss

            # create a list of months to find the greatest increase and decrease in profits - month
            months.append(row[0])

            # create a list of months to find the greatest increase and decrease in profits - month
            profit_loss_changes.append(profit_loss_change)

            # assign present month value to past month for calculating the change
            past_month_profit_loss = profit_loss
    
    # calculate sum of profit/loss changes from the above list
    total_profit_loss_change = sum(profit_loss_changes)

    # calculate average from the above some and reduce the one month from total months
    avg_profit_loss_change = round(total_profit_loss_change/(total_months-1),2)

    # maximum of profit/loss changes
    greatest_increase_profits = max(profit_loss_changes)

    # minimum of profit/loss changes
    greatest_decrease_profits = min(profit_loss_changes)

    # finding the greatest month increase using the index of the profit_loss_changes 
    greatest_increase_month = months[profit_loss_changes.index(greatest_increase_profits)]

    # finding the greatest month decrease using the index of the profit_loss_changes 
    greatest_decrease_month = months[profit_loss_changes.index(greatest_decrease_profits)]

    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: ${total_profit_loss}")
    print(f"Average Change: ${avg_profit_loss_change}")
    print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase_profits})")
    print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease_profits})")

    # Export the analysis to a text file

    budget_analysis_file = os.path.join("analysis", "budget_analysis.txt")
    with open(budget_analysis_file, "w") as budgetfile:

        budgetfile.write("Financial Analysis\n")
        budgetfile.write("----------------------------\n")
        budgetfile.write(f"Total Months: {total_months}\n")
        budgetfile.write(f"Total: ${total_profit_loss}\n")
        budgetfile.write(f"Average Change: ${avg_profit_loss_change}\n")
        budgetfile.write(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase_profits})\n")
        budgetfile.write(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease_profits})\n")