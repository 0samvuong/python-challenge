import os
import csv
from unicodedata import decimal

# Path to collect data from the Resources folder
election_csv = os.path.join('Resources', 'election_data.csv')
#Path to export
report_txt = os.path.join('analysis', 'report.txt')
# Read in the CSV file
with open(election_csv, 'r') as csvfile:

    # splits data based on comma's as it's a CSV file
    csvreader = csv.reader(csvfile, delimiter=',')
    #skips header
    header = next(csvreader)

    #variables
    total_votes = 0
    #dictionary of candidates and number of votes
    candidate_list = {}
    winner = ""
    winner_votes = 0


    #loop every row
    for row in csvreader:

        #count total votes
        total_votes += 1

        #if candidate not in candidate list, add candidate to dict  and 1 to it's vote

        if str(row[2]) not in candidate_list:
            candidate_list.update({str(row[2]): 1})
            continue
            
        # add a vote to candidate in dict 
        candidate_list[str(row[2])] += 1
 
# txt file export
f = open(report_txt, "w")

f.write(f"Election Results\n")
f.write(f"--------------------------------\n")
f.write(f"Total Votes: {total_votes}\n")
f.write(f"--------------------------------\n")

# iterate through every candidate in the list, then do the math with thier total votes, then put assign it to a varaible, then print
for candidate in candidate_list:

    candidate_votes = candidate_list[candidate]
    candidate_percent = (candidate_votes / total_votes) * 100
    f.write(f"{candidate}: {round(candidate_percent,2)}% ({candidate_votes})\n")

    #calculate winner
    if candidate_votes > winner_votes:
        winner_votes = candidate_votes
        winner = candidate

#print winner 
f.write(f"--------------------------------\n")
f.write(f"Winner is {winner}")

#read txt in terminal
f = open(report_txt, "r")
print(f.read())






