# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 19:53:38 2018

@author: Craig
"""
import os
import csv
csv_path_pypoll = os.path.join("limited_eletion_data.csv")



#Set Variables
total_votes = 0
list_candidates = []
Khan_votes =0
Li_votes=0
Correy_votes = 0
O_Tooley_votes = 0

#open file and set up CSV
with open(csv_path_pypoll, newline= '') as csv_file_pypoll:
    csv_file_pypoll = csv.reader(csv_file_pypoll, delimiter=',')  
     
    #review headers
    csv_header = next(csv_file_pypoll)
    #print(f"CSV Header: {csv_header}")

    for initial_loop in csv_file_pypoll:
        total_votes = total_votes + 1
        
        if initial_loop[2] not in list_candidates:
            list_candidates.append(str(initial_loop[2]))
   
        if initial_loop[2] == list_candidates[0]:
            Khan_votes += 1
        elif initial_loop[2] == list_candidates[1]:
            Li_votes += 1
        elif initial_loop[2] == list_candidates[2]:
            Correy_votes += 1
        elif initial_loop[2] == list_candidates[3]:
            O_Tooley_votes += 1

    if (Khan_votes> Li_votes and Khan_votes>Correy_votes and Khan_votes> O_Tooley_votes):    
        Winner="Khan"
    if (Li_votes> Khan_votes and Khan_votes>Correy_votes and Khan_votes> O_Tooley_votes):    
        Winner= "Li"
    if (Correy_votes> Li_votes and Correy_votes>Khan_votes and Correy_votes> O_Tooley_votes):    
        Winner="Coorey"
    if (O_Tooley_votes> Li_votes and O_Tooley_votes>Correy_votes and O_Tooley_votes>Khan_votes):    
        Winner="O_Tooley"    
        
Khan_vote_pct = Khan_votes / total_votes
Li_vote_pct = Li_votes / total_votes
Correy_vote_pct = Correy_votes / total_votes
O_Tooley_vote_pct = O_Tooley_votes /total_votes




          
print("Total Votes: " + str(total_votes))
print("----------------------------------")
#print("List of candidate" + str(list_candidates))
print("Khan: " + str(Khan_votes) +"(" + str(Khan_vote_pct) +"%)")
print("Li: " + str(Li_votes) +"(" + str(Li_vote_pct) +")")
print("Correy: " + str(Correy_votes) +"(" + str(Correy_vote_pct) +")")
print("O'Tooley: " + str(O_Tooley_votes) +"(" + str(O_Tooley_vote_pct) +")")
print("---------------------------------------------------------------")
print("Winner: " + Winner)
print("---------------------------------------------------------------")

import sys
with open('election_results.txt','w') as f:
    sys.stdout = f
    print("Total Votes: " + str(total_votes))
    print("----------------------------------")
    #print("List of candidate" + str(list_candidates))
    print("Khan: " + str(Khan_votes) +"(" + str(Khan_vote_pct) +"%)")
    print("Li: " + str(Li_votes) +"(" + str(Li_vote_pct) +")")
    print("Correy: " + str(Correy_votes) +"(" + str(Correy_vote_pct) +")")
    print("O'Tooley: " + str(O_Tooley_votes) +"(" + str(O_Tooley_vote_pct) +")")
    print("---------------------------------------------------------------")
    print("Winner: " + Winner)
    print("---------------------------------------------------------------")
    