#!/usr/bin/env python
# coding: utf-8

# In[31]:


from pathlib import Path 
import csv
#Renamed Profit/Losses as PL
#Set file path 
budget_datacsv = Path("budget_data.csv") 

line_num = 0
profitloss = []
profitloss_dates = []
profitloss_sum = 0
max_pl = 0
min_pl = 0
sum = 0

with open(budget_datacsv, 'r') as csvfile:
    
    # print(type(csvfile))
    
    csv_reader = csv.reader(csvfile, delimiter = ',')
    
    # print(type(csv_reader))
    
    header = next(csv_reader)
    # print(f"{header} <---- HEADER")
    
    for row in csv_reader:
        # print(row)
        line_num += 1
        profitloss.append(int(row[1]))
        profitloss_sum += int(row[1])
        profitloss_dates.append(row[0])
        

profitloss_change = []

for i in range(1, len(profitloss)):
    x = profitloss[i] - profitloss[i - 1]
    profitloss_change.append(int(x))
    
# print(profitloss_change)

for i in range(0, len(profitloss_change)):
    sum += profitloss_change[i]
    average_change_profitloss = round((sum / (len(profitloss_change))), 2)

# print(average_change_profitloss)

for profloss in profitloss:
    
    if min_pl == 0:
        max_pl == profloss
        min_pl == profloss
    if profloss > max_pl:
        max_pl = profloss
    elif profloss < min_pl:
        min_pl = profloss
        
# print(max_pl, min_pl)

max_pl_index = profitloss.index(max_pl)
min_pl_index = profitloss.index(min_pl)

max_pl_date = profitloss_dates[max_pl_index]
min_pl_date = profitloss_dates[min_pl_index]

# printing answers in an output text file called Financial_Analysis.txt

output_path = Path('Financial_Analysis.txt')

with open(output_path, 'w') as file:

    print(f"Financial Analysis\n")
    print(f"----------------------------\n")
    print(f"Total Months: {line_num} \n")
    print(f"Total: ${profitloss_sum}\n")
    print(f"Average Change: ${average_change_profitloss}\n")
    print(f"Greatest Increase in Profits: {max_pl_date} (${max_pl}) \n")
    print(f"Greatest Decrease in Profits: {min_pl_date} (${min_pl}) \n")

