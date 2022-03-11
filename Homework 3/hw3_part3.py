# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 21:25:35 2020

@author: cowarj
"""

import math

# Variables and Inputs
numBears = int(input("Number of bears => "))
print (numBears)
berryA = float(input("Size of berry area => "))
print (int(berryA))
tourists = numBears*10000

# Functions to Calculate 
def tourists(numBears):
    if (numBears > 15 or numBears < 4):
        tourists = 0
    elif (numBears <= 10):
        tourists = numBears * 10000
    else:
        tourists = ((numBears - 10)*20000) + 100000 
    return tourists
        
def find_next(numBears,berryA, tourists):
    bears_next = berryA/(50*(numBears+1)) + numBears*0.60 - (math.log(1+tourists,10)*0.1)
    berries_next = (berryA*1.5) - (numBears+1)*(berryA/14) - \
	(math.log(1+tourists,10)*0.05)
    if bears_next < 0:
        bears_next = 0
    if berries_next < 0:
        berries_next = 0.0
    nextt = (int(bears_next), berries_next)
    return nextt

# Defining Lists
bear_list = []
berries_list = []
tourists_list = []
bear_list.append(numBears)
berries_list.append(berryA)
tourists_list.append(tourists(numBears))
year = 1
space = " "
    
# Printing the Table
print("Year      Bears     Berry     Tourists")
print(year,space*(8-len(str(year))),numBears, space*(8-len(str(numBears))),berryA,space*(8-len(str(berryA))),tourists(numBears),space*(9-len(str(tourists(numBears)))))

while (year < 10):
    new = find_next(bear_list[year-1], berries_list[year-1], tourists(numBears))
    bear_num = new[0]
    bear_list.append(bear_num)
    berry_area = new[1]
    berries_output = berry_area
    berries_list.append(berries_output)
    tourists_list.append(tourists(int(bear_num)))
    year += 1
    print(year,space*(8-len(str(year))),bear_num,space*(8-len(str(bear_num))),"{:.1f}".format(berries_output),space*(8-len(str(round(berries_output,1)))),tourists(bear_num),space*(9-len(str(tourists(bear_num)))))

min_bears = min(bear_list)
max_bears = max(bear_list)
min_berries = min(berries_list)
max_berries = max(berries_list)
min_tourist = min(tourists_list)
max_tourist = max(tourists_list) 
print("")
print("Min:     ",str(min_bears)+(" "*(10-len(str(min_bears))))+"{:.1f}".format(min_berries)+(" "*(10-len(str(round(min_berries,1)))))+ str(min_tourist)+(space*(9-len(str(min_tourist)))))
print("Max:     ",str(max_bears)+(" "*(10-len(str(max_bears))))+"{:.1f}".format(max_berries)+" "*(10-len(str(round(max_berries,1))))+ str(max_tourist)+(space*(9-len(str(max_tourist)))))
  