import os
import csv

pybank_csv = os.path.join('Pybank','Resources', 'budget_data.csv')

greatest_increase = 0.0
greatest_increase_date = ""
greatest_decrease = 0.0
greatest_decrease_date = ""
average_change = 0.0
total_month = 0
previous_month_profit_loss = 0.0
all_changes = 0.0
total_profit = 0.0

with open(pybank_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader, None)

    for row in csvreader:
        current_row_value = float(row[1])
        total_month += 1
        total_profit = total_profit + current_row_value
        if total_month == 1:
            greatest_increase = current_row_value
            greatest_decrease = current_row_value
            greatest_increase_date = str(row[0])
            greatest_decrease_date = str(row[0])
        
        else:
            if current_row_value > greatest_increase:
                greatest_increase = current_row_value
                greatest_increase_date = str(row[0])
            if current_row_value < greatest_decrease:
                greatest_decrease = current_row_value
                greatest_decrease_date = str(row[0])
            all_changes = all_changes + current_row_value 

    average_change = all_changes / total_month

    total_profit = '{:,.2f}'.format(total_profit)
    average_change = '{:,.2f}'.format(average_change)
    greatest_increase = '{:,.2f}'.format(greatest_increase)
    greatest_decrease = '{:,.2f}'.format(greatest_decrease)

    print("Financial Analysis")
    print("---------------------------------------")
    print(f"Total Months: {str(total_month)}")
    print(f"Total: ${str(total_profit)}")
    print(f"Average Change: ${str(average_change)}")
    print(f"Greatest Increase in Profits: {str(greatest_increase_date)} ${str(greatest_increase)}")
    print(f"Greatest Decrease in Profits: {str(greatest_decrease_date)} ${str(greatest_decrease)}")

output_file = os.path.join('PyBank','Analysis','analysis.txt')

with open(output_file, "w") as datafile:
    datafile.write("Financial Analysis\n") 
    datafile.write("---------------------------------------\n")
    datafile.write(f"Total Months: {str(total_month)}\n")
    datafile.write(f"Total: ${total_profit}\n")
    datafile.write(f"Average Change: ${str(average_change)}\n")
    datafile.write(f"Greatest Increase in Profits: {str(greatest_increase_date)} ${str(greatest_increase)}\n")
    datafile.write(f"Greatest Decrease in Profits: {str(greatest_decrease_date)} ${str(greatest_decrease)}\n")
    
    


