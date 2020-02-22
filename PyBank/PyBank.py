import csv
import os

#file is in the same folder as our script
csvPath = 'budget_data.csv'

with open(csvPath) as csvFile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvFile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    numberMonths = 0
    totalProfitLosses = 0

    # Read each row of data after the header
    for row in csvreader:
        print(row[0])
        numberMonths += 1
        totalProfitLosses += int(row[1])


    print(f"Number of Months: {numberMonths}")
    print(f"Total Profit/Losses: {totalProfitLosses}")
