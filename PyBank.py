"""
Created on Sat Aug 25 20:26:28 2018

@author: davidmartinez
"""
# os and csv modules
import os
import csv

# files 
csvfile_input = "../Python/budget_data.csv"
txtfile_output = os.path.join("budget_analysis.txt")


# trackers
total_months = 0
prev_revenue = 0
month_of_change = []
revenue_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999]
total_revenue = 0

# read csv
# list of dictionaries
with open(csvfile_input) as revenue_data:
    reader = csv.DictReader(revenue_data)
    
    for row in reader:

        # total months

        total_months = total_months + 1
        total_revenue = total_revenue + int(row["Profit/Losses"])
        
        # revenue change
        revenue_change = int(row["Profit/Losses"]) - prev_revenue
        prev_revenue = int(row["Profit/Losses"])
        revenue_change_list = revenue_change_list + [revenue_change]
        month_of_change = month_of_change + [row["Date"]]

        # calculate greatest increase
        if (revenue_change > greatest_increase[1]):
            greatest_increase[0] = row["Date"]
            greatest_increase[1] = revenue_change

        # calculate greatest decrease
        if (revenue_change < greatest_decrease[1]):
            greatest_decrease[0] = row["Date"]
            greatest_decrease[1] = revenue_change

# average revenue change
revenue_avg = sum(revenue_change_list) / len(revenue_change_list)

# summary
output = (
    f"\nFinancial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total Revenue: ${total_revenue}\n"
    f"Average Revenue Change: ${revenue_avg}\n"
    f"Greatest Increase in Revenue: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Revenue: {greatest_decrease[0]} (${greatest_decrease[1]})\n")

# output
print(output)

# Export the results to text file
with open(txtfile_output, "w") as txt_file:
    txt_file.write(output)
