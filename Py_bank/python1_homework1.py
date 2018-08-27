# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 15:04:07 2018

@author: Craig
"""

# =============================================================================
# Python1 homeworks
# =============================================================================


# =============================================================================
# #psydo code
# =============================================================================


#current month Income
current_month_net_amt= 0
change_from_prior_month=0

#last month amount
last_month_net_amt =0 

#pnl_mth_change_current
current_month_change = 0
   

Total_net_amt =0 
Count_rows=0
Total_change_prior_month =10      

#Summary
    #Import File, delimit, and index

import os
import csv
csv_path_pybank = os.path.join("budget_data.csv")

#Open the file and Assign import name
with open (csv_path_pybank, newline= '') as csv_file_pybank:
    csv_var_pybank= csv.reader(csv_file_pybank, delimiter=',')

    csv_header = next(csv_var_pybank)
    #print(f"CSV Header: {csv_header}")
    list_current_month = []
    list_current_month_amt = []
    list_current_month_change = []
    for hope_run in csv_var_pybank:
        
        ##count rows
        Count_rows = Count_rows +1
        
        current_month_net_amt = int(hope_run[1])
        current_month = (str(hope_run[0]))
        change_from_prior_month = current_month_net_amt - last_month_net_amt
    
        #print("Date of current month  " + str(current_month))
        #print("Current Monthly Amount  " + str(current_month_net_amt))
        #print ("Change from Prior Month " + str(change_from_prior_month))
        
        list_current_month.append(str(current_month))
        list_current_month_amt.append(str(current_month_net_amt))
        list_current_month_change.append(str(change_from_prior_month))
        
        New_Data= {"month year": list_current_month
                   ,"current month amount": list_current_month_amt,
                   "change from prior month": list_current_month_change}        
    
        

        Total_net_amt = Total_net_amt + current_month_net_amt
        last_month_net_amt = int(current_month_net_amt)
        
print("'''text")
print("Financial Analysis")
print("---------------------------------")        
print("Total Months: " + str(Count_rows))        
print("Total: $" + str(Total_net_amt))
       
#print("month year" + str(New_Data["month year"]))
#print("current month amount" + str(New_Data["current month amount"]))
#print("current month change" + str(New_Data["change from prior month"]))

###Calculate Average Change#######
Row_count_minus_one = Count_rows - 1

Average_change = (int(list_current_month_amt[Row_count_minus_one])-int(list_current_month_amt[0] ))/Row_count_minus_one 

print("Average Change: " + str(Average_change))

####Calculate the Greatest increase in profit 
grt_increase_value_month = "Jan-1980"
grt_increase_value = 0
grt_increase_value_index = 0
grt_increase_value_index_counter = 0
for grt_increase_value_forloop in New_Data["change from prior month"]:
    grt_increase_value_index_counter = grt_increase_value_index_counter +1
    
    if int(grt_increase_value) < int(grt_increase_value_forloop):
        grt_increase_value = grt_increase_value_forloop
        grt_increase_value_index = grt_increase_value_index_counter -1
        
print("Greatest Increase in Profits: " +list_current_month[grt_increase_value_index] + " ($" + str(grt_increase_value)+ ")")           
####Ened

####Calculate the Greatest Decresase in profit 
grt_decr_value_month = "Jan-1980"
grt_decr_value = 0
grt_decr_value_index = 0
grt_decr_value_index_counter = 0
for grt_decr_value_forloop in New_Data["change from prior month"]:
    grt_decr_value_index_counter = grt_decr_value_index_counter + 1
   
    if int(grt_decr_value) > int(grt_decr_value_forloop):
        grt_decr_value = grt_decr_value_forloop
        grt_decr_value_index = grt_decr_value_index_counter-1

print("Greatest Decrease in Profits: " +list_current_month[grt_decr_value_index] + " ($" + str(grt_decr_value)+ ")")          
####End       

import sys
with open('Budget_data.txt','w') as f:
    sys.stdout = f
    print("'''text")
    print("Financial Analysis")
    print("---------------------------------")
    print("Total Months: " + str(Count_rows))        
    print("Total: $" + str(Total_net_amt))
    print("Average Change: " + str(Average_change))
    print("Greatest Increase in Profits: " +list_current_month[grt_increase_value_index] + " ($" + str(grt_increase_value)+ ")")  
    print("Greatest Decrease in Profits: " +list_current_month[grt_decr_value_index] + " ($" + str(grt_decr_value)+ ")") 