	# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 21:01:59 2020

@author: cowarj
"""
# Input Statements and Variables
turns = int(input("How many turns? => "))
print(turns)
name = input("What is the name of your pikachu? => ")
print(name)
p_turns = int(input("How often do we see a Pokemon (turns)? => "))
print(p_turns)
print("")
spot_row = 75
spot_column = 75
print("Starting simulation, turn 0 ", name, " at (", spot_column, ", ", spot_row, ")", sep="")
x = 1
record = []
spot = (spot_row, spot_column)

# Creating Function that will move the Pokemon
def move_pokemon(row, column, direction, steps):
    direction = direction.lower()
    location = (row, column)
    
    if (direction == ('n')):
        row -= steps
    elif (direction == ('s')):
        row += steps
    elif (direction == ('e')):
        column += steps
    elif(direction == ('w')):
        column -= steps
    else:
        location
        
    if (row < 0):
        row = 0
    elif (row > 150):
        row = 150
    elif (column < 0):
        column = 0
    elif (column > 150):
        column = 150
    return (row, column)

# Loop that runs the simulation x amount of turns
while(x <= turns):
        direction = input("What direction does {0} walk? => ".format(name))
        print(direction)
        spot = move_pokemon(spot[0], spot[1], direction, 5)
        if x % p_turns==0 and x!=0:
            print("Turn ", x, ", ", name, " at ", spot, sep="")
            p_type = input("What type of pokemon do you meet (W)ater, (G)round? => ")
            print(p_type)
            p_type = p_type.lower()
            if(p_type == ('w')):
                spot = move_pokemon(spot[0], spot[1], direction, 1)
                print(name, " wins and moves to ", spot, sep="")
                record.append("Win")
            elif(p_type == ('g')):
                spot = move_pokemon(spot[0], spot[1], direction, -10)
                print(name, " runs away to ", spot, sep="")
                record.append("Lose")
            else:
                record.append("No Pokemon")
        x+=1

# Final print statement at the end of the simulation
print(name + " ends up at ", spot, ", Record: ", record, sep="")
    