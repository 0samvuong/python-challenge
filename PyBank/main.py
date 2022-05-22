import os
import csv

# Path to collect data from the Resources folder
budget_csv = os.path.join('Resources', 'budget_data.csv')
#Path to export
report_txt = os.path.join('analysis', 'report.txt')

# Analysis function, argument takes in a row and

def analysis(budget_data):
    # assign the date column and profit/losses column as a variable
    date = str(budget_data[0])
    profit_loss = float(budget_data[1])
    
# Read in the CSV file
with open(budget_csv, 'r') as csvfile:

    # splits data based on comma's as it's a CSV file
    csvreader = csv.reader(csvfile, delimiter=',')
    #skips header
    header = next(csvreader)

    # create a varaible which records number of months in the CSV, counting every row
    months_total = 0    
    money_total = 0
    total_change = 0
    previous_month_profit = 0 
    gi_name = " "
    gd_name = " "
    gi_value = 0
    gd_value = 0

    for row in csvreader:
        #add 1 to the total row (month) count and calculator total profit
        months_total += 1 
        money_total += float(row[1])

         # checking the greatest increase and decrease in profits
        if float(row[1]) > gi_value:
            gi_value = float(row[1])
            gi_name = str(row[0])

        if float(row[1]) < gd_value:
            gd_value = float(row[1])
            gd_name = str(row[0])
        
        # need to store the previous month's profit to calculate rate of change, for the first month i am skipping it as it will ruin the calculation
        if months_total == 1:
            previous_month_profit = money_total
            continue
        
        # adding the total rate of change and assigning current row value as previous month's profit.
        total_change += (float(row[1]) - previous_month_profit)
        previous_month_profit = float(row[1])

     # calculating average change of profits  (outside of loop)
    average_change = total_change / (months_total - 1)

    #writing to txt 
    f = open(report_txt, "w")

    f.write(f"Financial Analysis by Sam Vuong \n")
    f.write(f"--------------------------------\n")
    f.write(f"Total Months: {months_total}\n")
    f.write(f"Total: ${round(money_total,2)}\n")
    f.write(f"Average Change: ${round(average_change,2)}\n")
    f.write(f"Greatest Increase in Profits: ${gi_name} (${round(gi_value,2)})\n")
    f.write(f"Greatest Decrease in Profits: ${gd_name} (${round(gd_value,2)})\n")

    #read txt in terminal
    f = open(report_txt, "r")
    print(f.read())