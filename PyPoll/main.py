# Import Resource
import csv
# Set Path
csvpath = "Resources/election_data.csv"

# Lists, Dictionaries, and Variables
count = 0
max_votes = 0 
c_dict = {}
c_max = ""   

# Open CSV
with open (csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip header
    csv_header = next(csvreader)

    for row in csvreader:
        count += 1

        # When read add to dictionary (Kid in a Candy Store)
        c_row = row[2]
        if c_row in c_dict.keys():
            c_dict[c_row] += 1
        else:
            c_dict[c_row] = 1

# Create output with total votes count
output = f"""----------------
Election Results
----------------
Total Votes: {count}
-------------------\n"""

# Add candidates to dictionary
# Add number of votes to dictionary
# Add percentage of votes to dictionary
for candidate in c_dict.keys():
    votes = c_dict[candidate]
    perc = 100 * votes / count
    
    # Add candidates with percent and number of votes to output
    line0 = f"{candidate}: {round(perc, 3)}% ({votes})\n"
    output += line0

    # Find the winning candidate
    if votes > max_votes:
        c_max = candidate
        max_votes = votes

# Add the winning candidate to the output
line1 = f"""--------------------------------------
Winner: {c_max}
---------------------"""
output += line1

# Print output into the terminal
print(output)

# Export to output.txt
with(open("output.txt", "w") as f):
    f.write(output)

