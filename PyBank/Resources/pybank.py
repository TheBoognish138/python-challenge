import csv

csvpath = "Resources/budget_data.csv"

#variable
month_count = 0
total_profit = 0

# for changes
last_month_profit = 0 # none
changes = []
month_changes= []

with open (csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header - next(csvreader)
    print(f"CSV Header: {csv_header}")

    for row in csvreader:
        print(row)

        month_count = month_count + 1 # month_count += 1

        total_profit = total_profit + int(row[1])

        # need previous month profit
        # difference between this and the previous
        # Append the change to the list

        # IF first row, there is no change
        if (month_count == 1):

            last_month_profit = int(row[1])
        else:
            change = int(row[1]) - last_month_profit
            changes.append(change)
            month_changes.append(row[0])

            last_month_profit = int(row[1])

    print(month_count)
    print(total_profit)
    print(len(changes))

    avg_change = sum(changes) / len(changes)
    print(avg_change)

    max_change = max(changes)
    max_month_indx = changes.index(max_change)
    max_month = month_changes
