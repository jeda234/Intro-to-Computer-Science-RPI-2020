# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 09:17:52 2020

@author: cowarj
"""
'inputs'
minutes =  int(input("Minutes ==> "))
print (minutes)
seconds =  int(input("Seconds ==> "))
print (seconds)
miles =  float(input("Miles ==> "))
print (miles)
target = float(input("Target Miles ==> "))
print (target)
print("")

'converting minutes to seconds'
s = (minutes * 60)+seconds
p= s/miles
pace_m= int(p/60)
pace_s=int(p%60)
print("Pace is ", pace_m, " minutes and ", pace_s, " seconds per mile.", sep="") 

'converting to miles per hour (speed)'
speed=float((miles*60*60)/s)
print("Speed is {0:.2f} miles per hour.".format(speed), sep="")

'finding time to run target distance'
t = (target/speed) * 60
t1 = int(t)
t2 = int((t*60)%60)
print("Time to run the target distance of ", target, " miles is ", t1, " minutes and ", t2, " seconds.", sep="")
