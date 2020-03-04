import csv
import os

#file is in the same folder as our script
csvpath = 'election_data.csv'

with open(csvPath) as csvFile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvFile, delimiter=',')

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    
    #variables

    # Read each row of data after the header
    for row in csvreader:
        #save values of current row
        rowVoterId = row(0)
        