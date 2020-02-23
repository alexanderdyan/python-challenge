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
    averageChange = 0
    prevProfitLoss = 0
    greatestProfit = 0
    greatestProfitMonth = ""
    greatestLoss = 0
    greatestLossMonth = ""

    # Read each row of data after the header
    for row in csvreader:
        #save values of current row
        rowDate = row[0]
        rowProfitLoss = int(row[1])
        #count number of months, every row is a new one
        numberMonths += 1
        #accumulate profit losses for every new row
        totalProfitLosses += rowProfitLoss
        #Start calculating Changes after 1st month to get differences
        if numberMonths > 1:
            change = rowProfitLoss - prevProfitLoss
            #accumulate average change to be divided at the end
            averageChange += change
            #check if change is bigger than recorded profit
            if change > greatestProfit:
                greatestProfit = change
                greatestProfitMonth = rowDate
            #check if change is smaller than recorded loss
            if change < greatestLoss:
                greatestLoss = change
                greatestLossMonth = rowDate
        #store profit losses for next row to use
        prevProfitLoss = rowProfitLoss
    
    #compute the average of sum of changes
    averageChange = averageChange / (numberMonths - 1)

    print("Financial Analysis")
    print("----------------------------")
    print(f"Number of Months: {numberMonths}")
    print(f"Total Profit/Losses: {totalProfitLosses}")
    print(f"Average Change: {averageChange}")
    print(f"Greatest Increase in Profits:{greatestProfitMonth} (${greatestProfit})")
    print(f"Greatest Decrease in Profits:{greatestLossMonth} (${greatestLoss})")

     

