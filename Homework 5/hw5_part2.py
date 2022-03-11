# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 01:16:19 2020

@author: cowarj
"""
import hw5_util

def get_global_max(grid):
    '''
    Finds the global max and returns that value and the location

    Parameters
    ----------
    grid : list

    Returns
    -------
    global_max : int
    global_max_location : tuple

    '''
    global_max = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if(grid[i][j] > global_max):
                global_max = grid[i][j]
                global_max_location = (i, j)
    return((global_max, (global_max_location)))

def get_nbrs(location, grid):
    '''
    Finds the global max and returns that value and the location

    Parameters
    ----------
    location : tuple
    grid : list

    Returns
    -------
    neighbors : 

    '''
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

def possible_points(raw_grid, point, step_height):
    nbrs = get_nbrs(point, raw_grid)
    x = []
    for i in nbrs:
        elevation1 = raw_grid[i[0]][i[1]]
        elevation2= raw_grid[point[0]][point[1]]
        diff=elevation1-elevation2
        if (elevation1 > elevation2 and diff <= step_height):
            x.append((elevation1,i))
    x.sort()
    return x
        
def gradual_path(raw_grid, start, step):
    current = start
    path = [start]
    while current != get_global_max(raw_grid)[1]:
        possible = possible_points(raw_grid, current, step)
        if len(possible) == 0:
            return path 
        current = possible[0][1]
        path.append(current)
    return path

def steep_path(raw_grid, start, step):
    current = start
    path = [start]
    while current != get_global_max(raw_grid)[1]:
        possible = possible_points(raw_grid, current, step)
        if len(possible) == 0:
            return path
        elif possible[0][1]==possible[-1][1]:    
            current = possible[0][1]
        else:
            current = possible[-1][1]
        path.append(current)
    return path

index = int(input("Enter a grid index less than or equal to 3 (0 to end): "))
print(index)
raw_grid = hw5_util.get_grid(index)
step_height = int(input("Enter the maximum step height: "))
print (step_height)
print_grid = input("Should the path grid be printed (Y or N): ")
print(print_grid)
print_grid = print_grid.lower()

global_max = 0
row = 0
column = 6
for i in range(len(raw_grid)):
    row+=1
    
global_stats = get_global_max(raw_grid)

print("Grid has {} rows and {} columns".format(row, column))
print("global max: {} {}".format(global_stats[1], global_stats[0]))

start_points = hw5_util.get_start_locations(index)

for i in start_points:
    print("===\nsteepest path")
    x = steep_path(raw_grid, i, step_height) 
    count = 0
    for j in x:
        if (count%5 == 0 and count != 0):
            print("\n{} ".format(j))
            count+=1
        else:
            print(str(j), " ", end="", sep="")
            count=0
    if (len(x) <= 2):
        print("\nno maximum")
    elif (x[-1] == global_stats[1]):
        print("\nglobal maximum")
    else:
        print("\nlocal maximum")
    print("...\nmost gradual path")
    count = 0
    y = gradual_path(raw_grid, i, step_height) 
    for k in y:
        if (count%5 == 0 and count != 0 ):
            print("\n{} ".format(k))
            count+=1
        else:
            print(str(k), " ", end="", sep="")
            count+=1
    if (len(y) <= 2):
        print("\nno maximum")
    elif (y[-1] == global_stats[1]):
        print("\nglobal maximum")
    else:
        print("\nlocal maximum")
print("===")

if (print_grid == "y"):
    print('Path grid')
    path_grid = []
    spot_total = 0
        