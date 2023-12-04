# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 10:21:24 2023

@author: maude
"""
total = 0
totalPower = 0

#read the imput
file = open("day2.txt", "r")
while True:
    isOk = True
    content = file.readline()
   
    if not content:
        break
    minGreen = 0
    minRed =0
    minBlue =0 
    gameNumber = int(content.split(":")[0][5:])
    drawData = content.split(":")[1].split(";")
    for draw in drawData:
        colorData = draw.split(",")
        for data in colorData:
            number = int(data.split(' ')[1])
           
            if "green" in data:
                if(number>minGreen):
                    minGreen = number
                if(number >13):
                    isOk = False
            elif "red" in data:
                if(number>minRed):
                    minRed = number
                if(number > 12):
                    isOk = False
            elif "blue" in data:
                if(number>minBlue):
                    minBlue = number
                if(number>14):
                    isOk = False
                
       
    
    power = minGreen*minBlue*minRed
    totalPower = totalPower+power
    if isOk:
        print(gameNumber)
        total = total + gameNumber


print(total)
print(totalPower)
    