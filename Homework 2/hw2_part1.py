# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 15:02:41 2020

@author: cowarj
"""
from math import pi, ceil

# Necessary functions in order to find the amount of gumballs needed in the machine
def find_volume_sphere(radius):
    return ((4/3)*pi*(radius**3))

def find_volume_cube(side):
    return (side**3)

# Input Statements
r =  input("Enter the gum ball radius (in.) => ")
print (r)

weekly_sales = input("Enter the weekly sales => ")
print (weekly_sales)
print(" ")

# Calculations
r = float(r)
weekly_sales = int(weekly_sales)
target = ceil(weekly_sales*1.25)
balls_per_side = ceil(target**(1/3))
edgelength = balls_per_side*2*r
max_gumballs = balls_per_side**3
extra = max_gumballs - target
waste = find_volume_cube(edgelength)-find_volume_sphere(r)*target
fill = find_volume_cube(edgelength)-(max_gumballs*find_volume_sphere(r))

# Print Statements
print("The machine needs to hold {} gum balls along each edge.".format(balls_per_side))
print("Total edge length is {:.2f} inches.".format(edgelength))
print("Target sales were {}, but the machine will hold {} extra gum balls.".format(target, extra))
print("Wasted space is {:.2f} cubic inches with the target number of gum balls,".format(waste))
print("or {:.2f} cubic inches if you fill up the machine.".format(fill))
