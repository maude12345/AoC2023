# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 07:29:51 2023

@author: maude
"""
import numpy as np
total = 0
totalPower = 0

#read the imput
file = open("testday5.txt", "r")
firstLine = file.readline()
firstLine = firstLine.split(":")[1][1:-1]#remove first space + \n

#find original seeds
seeds = firstLine.split(" ")
previousData = seeds
totalData = []
hasChanged = []
content = file.readline()
while True:
  
    content = file.readline()
 
    content = file.readline()


   
    if not content:
        break
    
    
    #for each nest 
    newData = np.zeros(len(previousData))
    hasChanged = []
    for x in range(len(previousData)):
        hasChanged.append(False)
    
    while not content == "\n":
        line = content[:-1].split(' ')
        
        
        newData = previousData
        for prevData in range(len(previousData)):
            data = int(previousData[prevData])
            
            if int(line[1])<=data and int(line[1])+int(line[2])> data and not hasChanged[prevData]:
                newData[prevData] = int(newData[prevData]) - int(line[1])+int(line[0])
                hasChanged[prevData] = True
                
              
        content = file.readline()
        if not content:
            break
        
        
        
   # print(newData)
    previousData = newData
    totalData.append(previousData)
#print(np.min(previousData))  

#part2
print("part2")
file = open("day5.txt", "r")
firstLine = file.readline()
firstLine = firstLine.split(":")[1][1:-1]#remove first space + \n

#find original seeds
seeds = firstLine.split(" ")
print(seeds)
previousData = seeds
totalData = []
hasChanged = []
content = file.readline()
while True:
  
    content = file.readline()
 
    content = file.readline()


   
    if not content:
        break
    
    
    #for each nest 
    newData = np.zeros(len(previousData))
    hasChanged =[]
    for x in previousData:
        hasChanged.append(False) 
    
    while not content == "\n":
        line = content[:-1].split(' ')
        #print(line)
        
        newData = previousData
     
        
        extraData = []
        for prevData in range(len(previousData)):
            if(np.mod(prevData,2)==1):
                continue
            if hasChanged[prevData]:
                continue
            mindata = int(previousData[prevData])
            maxdata = mindata+int(previousData[prevData+1])
            #we find the new ranges
            minRange = int(line[1])
            maxRange = int(line[1])+int(line[2])
         
            
            if minRange<=maxdata and maxRange> mindata: #at least part of the range will be changed
                if mindata<minRange: #np.minimum gives overflow error
                    newData[prevData] = minRange- int(line[1])+int(line[0])
                else:
                    newData[prevData] = mindata - int(line[1])+int(line[0])
                if(mindata<minRange): #we keep the unchanged data, could be changed by something else
                    previousData.append(mindata)
                    previousData.append(minRange-mindata)
                    hasChanged.append(False)
                    hasChanged.append(False)
                if(maxdata>maxRange):
                    previousData.append(maxRange)
                    previousData.append(maxdata-maxRange)
                    hasChanged.append(False)
                    hasChanged.append(False)
                #becase overflow error when using np.minimum
                maxlocal = maxdata
                if maxdata>maxRange:
                    maxlocal = maxRange
                minlocal= mindata
                if(minRange>mindata):
                    minlocal = minRange
                newData[prevData+1] = maxlocal-minlocal
                hasChanged[prevData] = True
              #  print(newData)
               # print(hasChanged)
                
            
                
              
        content = file.readline()
        if not content:
            break
        
        
        
    print(newData)
    
    previousData = newData
    totalData.append(previousData)
    trueData =[]
    for value in range(len(previousData)):
        if(np.mod(value,2) == 0):
            trueData.append(previousData[value])
print(np.min(trueData))  