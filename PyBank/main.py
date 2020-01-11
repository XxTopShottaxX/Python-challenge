## Import modules for reading csv, file directory resolution and date/time manipulation
import os
import csv
import datetime as dt

## Setting file directory as a string and opeining it
#path = "./Resourses/budget_data.csv"
#csvreader = os.path.join(path)
csvreader = "budget_data.csv"
## file directory verification
print(csvreader)
##budget_data = os.path.join("Resources", "budget_data.csv")

## months = {"Jan":0, "Feb":1, "Mar":2, "Apr":3, "May":4, "Jun":5, "Jul":6, "Aug":7, "Sep":8, "Oct":9, "Nov":10, "Dec":11 }

##  sortedMonthList = sorted()


##from datetime import datetime
##months_sorted = sorted(budget_data, key=lambda month: datetime.strptime(month, "%b-%Y"))
##print(months_sorted)

dates = []
profitLoss_net = []
profitLoss_avg = []


with open(csvreader,newline='') as csvfile: 
    csvreader = csv.reader(csvfile, delimiter=",")

csv_header = next(csvreader)

for row in csvreader:
     row_date = dt.dt.strptime(row[2],"%b-%Y" )
print(row_date)