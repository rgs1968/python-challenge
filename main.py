# Modules
import os
import csv
import pandas as df
import os.path
from os import path
OutPutFile = "output.txt"
with open('/Users/rhondasampson/Documents/GitHub/python-challenge/PyBank/Resources/budget_data.csv') as csvfile:
    csvreader = csv.reader(csvfile)
    data = list(csvreader)
data
profit=0
loss=0
realcount=0
#GreatestProfitIncrease=0
#GreatestProfitDecrease=0
lastvalue=0
total=0
deltaincrease=0
deltadecrease=0

#find list length
for i in range(len(data)):
    
    #print i and move to next value
    reviewlength=len(data[i])
    hh=data[i];

    #skip the header
    for k in range(reviewlength):
        if (( i > 0 ) & ( k == 1)):

            realcount = realcount + 1
            value=int(hh[1])

            total = total + value
            if (value > 0 ):
                profit = profit + value

            else:
                loss = loss + value
            curdelta = value - lastvalue

            if ( curdelta > deltaincrease ):
                deltaincrease = curdelta
                maxmonth = ThisRecord[0]

            if (curdelta < deltadecrease ):
                deltadecrease = curdelta
                minmonth = ThisRecord[0]

                lastvalue = value

# Generate Output Summary
output = (
    f"\nFinancial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {str(csvpath.count)}\n"
    f"Total: ${str(total)}\n"
    #f"Average  Change: ${net_monthly_avg:.2f}\n"
    f"Greatest Increase in Profits: {str(profit)}\n"
    f"Greatest Decrease in Profits: {str(loss)}\n")
# Print the output (to terminal)
print(output)







