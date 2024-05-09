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


with open (csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvreader)
    print("------------------")
    print("Financial Analysis")
    print("------------------")

    for row in csvreader:

        count = count + 1

        total_profit = total_profit + int(row[1])

        # need previous month profit
        # difference between this and the previous
        # Append the change to the list

        # IF first row, there is no change
        if (count == 1):

            last_month_profit = int(row[1])
        else:
            change = int(row[1]) - last_month_profit
            changes.append(change)
            month_changes.append(row[0])

            last_month_profit = int(row[1])

    print(f"Total Months: {count}")
    print(f"Total: ${total_profit}")

    avg_change = sum(changes) / len(changes)
    avg_change_rounded = round(avg_change, 2)
    print(f"Average Change: ${avg_change_rounded}")

    max_change = max(changes)
    max_month_indx = month_changes[changes.index(max_change)]
    print(f"Greatest Increase in Profits: {max_month_indx} (${max_change})")

    min_change = min(changes)
    min_month_indx = month_changes[changes.index(min_change)]
    print(f"Greatest Decrease in Profits: {min_month_indx} (${min_change})")
    print("------------------------------------------------")

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