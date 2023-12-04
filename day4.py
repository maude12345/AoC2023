# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 07:43:32 2023

@author: maude
"""

file = open("day4.txt", "r")
total =0;

import numpy as np
    
while True:
    content = file.readline()
    if not content:
        break
    lineTotal = 0
    answers = content.split("|")[1][:-1]
    #we add a splace at the end
    answers = answers + ' '
  
    ourNumbers = content.split("|")[0].split(":")[1]
    for number in ourNumbers.split(' '):
        valueToCheck = ' ' + number + ' '
        if valueToCheck == '  ':
            continue
     
        if valueToCheck in answers:
            
            if(lineTotal == 0):
                lineTotal = 1
            else:
                lineTotal = lineTotal*2
        
         
  
    total = total + lineTotal
print("part 1")
print(total)

#part two
file = open("day4.txt", "r")
total =0;
numberOfTickets = np.zeros(200)

lineNumber =1 

    
while True:
    content = file.readline()
    if not content:
        break
    lineTotal = 0
    numberOfTickets[lineNumber-1] = numberOfTickets[lineNumber-1]+1 # the original one
    answers = content.split("|")[1][:-1]
    #we add a splace at the end
    answers = answers + ' '
  
    ourNumbers = content.split("|")[0].split(":")[1]
    #lineNumber = int(content.split(":")[0].split(' ')[1])
    for number in ourNumbers.split(' '):
        valueToCheck = ' ' + number + ' '
        if valueToCheck == '  ':
            continue
     
        if valueToCheck in answers:           
            lineTotal = lineTotal+1
        
    print("lineTotal")
    print(lineTotal)
    print("numberOfTickets")
    #print(numberOfTickets)
    for x in range(lineTotal):
        numberOfTickets[lineNumber+x] = numberOfTickets[lineNumber+x]+numberOfTickets[lineNumber-1]
    total = total + numberOfTickets[lineNumber-1]
    lineNumber = lineNumber+1
print("part2")
print(total)