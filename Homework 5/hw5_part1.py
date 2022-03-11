# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 14:38:21 2020

@author: cowarj
"""

import math
import hw5_util

index = int(input("Enter a grid index less than or equal to 3 (0 to end): "))
print(index)
raw_grid = hw5_util.get_grid(index)
print_grid = input("Should the grid be printed (Y or N): ")
print(print_grid)
print_grid = print_grid.lower()
start_locations = hw5_util.get_start_locations(index)

# Formatting Grid for Printing & Calculating Number of Rows and Columns

if (print_grid == "y"):
    row = 0
    column = len(raw_grid[0])
    print("Grid ", index, sep="", end='')
    for i in raw_grid:
        print("\n", end='')
        row+=1
        for j in i:
           print(((" "*(4-len(str(j))))) + str(j), end="")
    
    print("\nGrid has {} rows and {} columns".format(row, column))

else: 
    row = 0
    column = len(raw_grid[0])
    for i in raw_grid:
        row+=1
        for j in i:
            x = 0
    print("Grid has {} rows and {} columns".format(row, column))
    
def get_nbrs(location,grid):
    
    neighbors = []
    if (location[0]-1 >= 0):
        spot1 = (location[0]-1, location[1])
        neighbors.append(spot1)
    if (location[1]-1 >= 0):
        spot2 = (location[0], location[1]-1)
        neighbors.append(spot2)
    if (location[0]+1 < len(grid)):
        spot3 = (location[0]+1, location[1])
        neighbors.append(spot3)
    if (location[1]+1 < len(grid[0])):
        spot4 = (location[0], location[1]+1)
        neighbors.append(spot4)
    neighbors.sort()
    return neighbors

for i in range(len(start_locations)):
    neighbors = get_nbrs(start_locations[i], raw_grid)
    print("Neighbors of ({}, {}):".format(start_locations[i][0], start_locations[i][1]), end="")
    for j in range(len(neighbors)):
        print(" {}".format(neighbors[j]),end="")
    print("")

valid_count = 0 
possible_path = hw5_util.get_path(index)
index1 = 0
index2 = 0
index3 = 0
index4 = 0
count_d = []
count_u = []
for i in range(len(possible_path)-1):
   if (possible_path[i] in get_nbrs(possible_path[i+1], raw_grid)):
       index1 = possible_path[i][0]
       index2 = possible_path[i][1]
       index3 = possible_path[i+1][0]
       index4 = possible_path[i+1][1]
       valid_count = 1
       difference =  raw_grid[index3][index4]-raw_grid[index1][index2]
       
       if (difference > 0):
           count_u.append(abs(difference)) 
       elif difference < 0:
           count_d.append(abs(difference))
           
       upward = sum(count_u)
       downward = sum(count_d)
   else:
       valid_count = 0
       spot_1 = possible_path[i]
       spot_2 = possible_path[i+1] 
       break
       
if (valid_count == 1):
    print("Valid path")
    print("Downward", downward)
    print('Upward', upward)

else:
    print('Path: invalid step from {} to {}'.format(spot_1, spot_2))