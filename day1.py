# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 10:33:09 2023

@author: maude
"""

file = open("day1.txt", "r")
total =0;


    
while True:
    content = file.readline()
    if not content:
        break
    firstdigit = False
    dozenvalue =0
    unityvalue = 0
    substring = ""
    for caracter in content:
       if(caracter == '0' or caracter == '1' or caracter == '2' or caracter == '3'
          or caracter == '4' or caracter == '5' or caracter == '6' or caracter == '7'
          or caracter == '8' or caracter == '9'):
           substring = ''
           if not firstdigit:
               dozenvalue = int(caracter)
               firstdigit = True
               unityvalue = dozenvalue
               
           else:
               unityvalue = int(caracter)
       else:
            substring = substring + caracter 
            #print(substring) 
            if "one" in substring:
                unityvalue = 1
                print("ONE")
            elif "two" in substring:
                unityvalue = 2
                print("TWO")
            elif "three" in substring:
                unityvalue = 3
                print("three")
            elif "four" in substring:
                unityvalue = 4
                print("four")
            elif "five" in substring:
                unityvalue = 5
            elif "six" in substring:
                unityvalue = 6
            elif "seven" in substring:
                unityvalue = 7
            elif "eight" in substring:
                unityvalue = 8
            elif "nine" in substring:
                unityvalue =9
            else:
                continue
                
            if not firstdigit:
                dozenvalue= unityvalue
                firstdigit = True
            substring = substring[-1]
                
              
                
                
                    

                
    print(dozenvalue*10+unityvalue)          
    total = total + dozenvalue*10+unityvalue;
    #print(total)
    	