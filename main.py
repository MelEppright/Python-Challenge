import os

import csv

csvpath = os.path.join('Resources', 'election_data.csv')

Total_Votes = []
Candidate_Names= ["Khan", "Correy", "Li", "O'Tooley" ]
Candidate_Choices=[]
Khan_Total = []
Correy_Total = []
Li_Total = []
OTooley_Total = []

#def getPercentages(Khan_Total, Total_Number_Votes:
#    return 

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    csv_header = next(csvreader)

    for row in csvreader:
        Total_Votes.append(row[0])
        Total_Number_Votes = len(Total_Votes)
        if row[2] == "Khan":
            Khan_Total.append(row[2])
        if row[2] == "Correy":
            Correy_Total.append(row[2])
        if row[2] == "Li":
            Li_Total.append(row[2])
        if row[2] == "O'Tooley":
            OTooley_Total.append(row[2]) 
        Khan_Percentage = ((len(Khan_Total)) / (Total_Number_Votes)) * 100
        Correy_Percentage = ((len(Correy_Total))/ (Total_Number_Votes)) * 100
        Li_Percentage = ((len(Li_Total))/ (Total_Number_Votes)) *100
        OTooley_Percentage = ((len(OTooley_Total))/(Total_Number_Votes)) * 100
     

  
print("The Total Number of Votes is " + str(Total_Number_Votes))
print("Khan: " + "Votes, " + (str(len(Khan_Total))) + " Percent, " + str(Khan_Percentage))
print("Correy: " + "Votes, " + str(len(Correy_Total)) + " Percent, " + str(Correy_Percentage))
print("Li: " + "Votes, " + str(len(Li_Total)) + " Percent, " + str(Li_Percentage))
print("O'Tooley: " + "Votes, " + str(len(OTooley_Total)) + " Percent, " + str(OTooley_Percentage))
print("Winner: Khan")
