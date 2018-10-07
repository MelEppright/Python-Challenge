import os

import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

Total_Months = []
Profit_Loss = []
total=0

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    csv_header = next(csvreader)
    
    '''
    row1 = next(csvreader)
    row2 = next(csvreader)
    Total_Months.append(row1[0])
    Total_Months.append(row2[0])
    Total += int(row1[1])
    Total += int(row2[1])
    print("row 1 ")
    print(row1)
    print("row2 ")
    print(row2)
    print("total")
    print(Total)
    Total_Number_Months = len(Total_Months) 
    '''

    for row in csvreader:
        Total_Months.append(row[0])
        Total_Number_Months = len(Total_Months) 
        Profit_Loss.append(row[1])
        total += int(row[1])
        
        # print(total)
    
    print("Total Months," + str(Total_Number_Months))
    print("Total Profit Loss, " + str(total))

   