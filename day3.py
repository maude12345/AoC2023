# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 08:47:51 2023

@author: maude
"""
import numpy as np
file = open("day3.txt", "r")
elementMatrix = []
#we do a "connected map" where true means we are adjacent to a symbol
while True:
   
    content = file.readline()

    if not content:
        break
    currentLine = []
    for element in range(len(content)):
        if content[element].isnumeric():
            currentLine.append(False)
        elif content[element] == "." or content[element] == "\n":
            currentLine.append(False)
        else:
            currentLine.append(True)
        
    elementMatrix.append(currentLine)

#we add the number that are adjacents

height = len(elementMatrix)
width = len(elementMatrix[0])
gearMatrix = np.zeros((height,width))
gearTotal = np.zeros((height,width))
lineNumber = -1
total =0 
totalGear = 0;
file = open("day3.txt", "r")
while True:
    content = file.readline()
    lineNumber = lineNumber+1;
    if not content:
        break
    isCurrentlyNumber = False
    addNumber = False
    currentNumber = ''
    for element in range(len(content)):
        if content[element].isnumeric():
            isCurrentlyNumber = True
            currentNumber = currentNumber + content[element]
        else:
            if isCurrentlyNumber: #we check if we are adjacent
                          
                for x in range(element-len(currentNumber)-1, element+1):
                    
                    for y in range(lineNumber -1, lineNumber +2):
                        
                        if(x>=0 and x<width and y>=0 and y<height):
                           
                            if elementMatrix[y][x]:
                                addNumber = True
                                if gearTotal[y][x] == 0:
                                    gearMatrix[y][x] = currentNumber
                                else:
                                    gearMatrix[y][x] = gearMatrix[y][x]*int(currentNumber)
                                gearTotal[y][x] = gearTotal[y][x]+1
                if addNumber:
                     total = total + int(currentNumber)
                     addNumber = False;
                     print(currentNumber)
                  
                currentNumber = ''
            isCurrentlyNumber = False
            
#we add the gear totals
            
for x in range(width):
    for y in range(height):
        if gearTotal[y][x] ==2:
            totalGear = totalGear+ gearMatrix[y][x]
   
            
print(totalGear)   