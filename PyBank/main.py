# Import resource
import csv
# Set Path
csvpath = "Resources/budget_data.csv"

# Variables
count = 0
total_profit = 0

# Changes
last_month_profit = 0 # none
changes = []
month_changes= []

# Open CSV
with open (csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvreader)

    for row in csvreader:

        count = count + 1

        total_profit = total_profit + int(row[1])

        if (count == 1):

            last_month_profit = int(row[1])
        else:
            change = int(row[1]) - last_month_profit
            changes.append(change)
            month_changes.append(row[0])

            last_month_profit = int(row[1])

    # average change
    avg_change = sum(changes) / len(changes)
    avg_change_rounded = round(avg_change, 2)

    # max change
    max_change = max(changes)
    max_month_indx = month_changes[changes.index(max_change)]

    # min change 
    min_change = min(changes)
    min_month_indx = month_changes[changes.index(min_change)]
    
    # print to terminal
    print("------------------")
    print("Financial Analysis")
    print("------------------")
    print(f"Total Months: {count}")
    print(f"Total: ${total_profit}")
    print(f"Average Change: ${avg_change_rounded}")
    print(f"Greatest Increase in Profits: {max_month_indx} (${max_change})")
    print(f"Greatest Decrease in Profits: {min_month_indx} (${min_change})")
    print("------------------------------------------------")

# export to output.txt
with open("output.txt", "w") as text:
    text.write("------------------\n")
    text.write("Financial Analysis\n")
    text.write("------------------\n")
    text.write(f"Total Months: {count}\n")
    text.write(f"Total: ${total_profit}\n")
    text.write(f"Average Change: ${avg_change_rounded}\n")
    text.write(f"Greatest Increase in Profits: {max_month_indx} (${max_change})\n")
    text.write(f"Greatest Decrease in Profits: {min_month_indx} (${min_change})\n")
    text.write("------------------------------------------------")