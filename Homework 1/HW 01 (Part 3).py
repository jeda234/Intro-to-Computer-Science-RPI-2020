# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 14:45:29 2020

@author: cowarj
"""
# Collecting Inputs
frame = input("Enter frame character ==> ")
print (frame)
height = int(input("Height of box ==> "))
print (height)
width = int(input("Width of box ==> "))
print (width)

# Setting up the Box
print("")
print("Box:")
print(frame*width)
print((frame+" "*(width-2)+frame+"\n")*(int(height/2)-1), sep="", end="")

# Coding the middle of the box with the dimensions in it
print(frame," "*(int((width/2)-1-(len(str(width))))), width, "x", height, " "*(int((width/2)-1-(len(str(height))))), frame, sep="")
print((frame+" "*(width-2)+frame+"\n")*(int(height/2)-1), sep="", end="")
print(frame*width)
