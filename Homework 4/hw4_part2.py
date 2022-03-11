# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 16:33:07 2020

@author: cowarj
"""

import hw4_util

# Finding the State
def find_state(weeklist, state):
    for i in weeklist:
        if i[0]==state:
            return i
    
print ("...")
index = int(input("Please enter the index for a week: "))
print (index)

# While loop that initiates the iteration of find week statistics
if __name__ == "__main__": #GUARD
    while(index > 0):
        if (index > 29):
            print ("No data for that week")
            print("...")
            index = int(input("Please enter the index for a week: "))
            print(index)
    
        totalweeklist = hw4_util.part2_get_week(index)
        request = input("Request (daily, pct, quar, high): ")
        print (request)
        request = request.lower()
        if (request == "daily"):
            state = input("Enter the state: ")
            print(state)
            avg_daily = 0
            week_list = find_state(totalweeklist, state)
            if (week_list == None):
                print("State", state,"not found")
            else:
                for i in range(2,9):
                    avg_daily+=(week_list[i]/week_list[1])*100000
                avg_daily/=7
                print("Average daily positives per 100K population: ", round(avg_daily, 1), sep="")
        
        elif (request == "pct"):
            state = input("Enter the state: ")
            print (state)
            avg_pos_percent = 0
            week_list=find_state(totalweeklist, state)
            if (week_list == None):
                print("State", state,"not found")
            else:
                p = 0
                n = 0
                for i in range(2,9):
                    p += (week_list[i])
                    n += (week_list[i+7])
                avg_pos_percent = ((p)/(p+n))*100
                print("Average daily positive percent: ", round(avg_pos_percent, 1), sep="")
        
        elif (request == "quar"):
            states = []
            for i in totalweeklist:
                p = 0
                n = 0
                for z in range(2,9):
                    p += (i[z])
                    n += (i[z+7])
                avg_pos_percent = ((p)/(p+n))*100
                avg_daily=0
                for q in range(2,9):
                    avg_daily += (i[q]/i[1])*100000
                avg_daily /= 7
                if (avg_daily >= 10 or avg_pos_percent >= 10):
                    states.append(i[0])
            
            print("Quarantine states:")
            hw4_util.print_abbreviations(states)
        
        elif (request == "high"):
            state_high = []
            rate = 0
            i = 0
            while(i < len(totalweeklist)):
                week_list = find_state(totalweeklist, totalweeklist[i][0])
                ratee = 0
                for x in range(2,9):
                    ratee+=(week_list[x]/week_list[1])*100000
                ratee/=7
                if (ratee > rate):
                    rate = ratee
                    state_high.append(totalweeklist[i][0])
                i+=1
            
            print("State with highest infection rate is ", state_high[-1], sep="")
            print("Rate is ", round(rate,1)," per 100,000 people", sep="")
        
        else:
            print("Unrecognized request")
        
        print("...")
        index = int(input("Please enter the index for a week: "))
        print(index)
