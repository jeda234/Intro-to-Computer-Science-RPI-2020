# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 23:55:43 2020

@author: cowarj
"""
import hw4_util
password = input("Enter a password => ")
print(password)
score = 0

# Methods that will be called later to help calculate score
def score_length(password):
    s = 0
    l = len(password)
    if (l < 6):
        s += 0
    elif (l == 6 or l == 7):
        s += 1
        print("Length: +1")
    elif (l == 8 or l == 9 or l == 10):
        s += 2
        print("Length: +2")
    else:
        s += 3
        print("Length: +3")
    return s

def score_case(password):
    s = 0
    uCount = 0
    lCount = 0
    aList = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    for i in range(len(aList)):
        uCount += password.count(aList[i]) 
        lCount += password.count(aList[i].lower())
    if (uCount >= 2 and lCount >= 2):
        s += 2
        print("Cases: +2")
    elif (uCount >= 1 and lCount >= 1):
        s += 1
        print("Cases: +1")
    else:
        s += 0
    return s

def score_digits(password):
    s = 0
    dCount = 0
    nList = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    for i in range(len(nList)):
        dCount += password.count(nList[i])
    if (dCount >= 2):
        s += 2
        print("Digits: +2")
    elif (dCount == 1):
        s += 1
        print("Digits: +1")
    else:
        s += 0
    return s

def score_punctuation(passsword):
    s = 0
    p1Count = 0
    p2Count = 0
    p1List = ["!", "@", "#" ,"$"]
    p2List = ["%", "^", "&", "*"]
    for i in range(len(p1List)):
        p1Count += password.count(p1List[i])
    for i in range(len(p2List)):
        p2Count += password.count(p2List[i])
    if (p1Count >= 1):
        s += 1
        print("!@#$: +1")
    elif (p2Count >= 1):
        s += 1
        print("%^&*: +1")
    else:
        s += 0
    return s

def score_nylicense(password):
    score = 0
    for i in range(0,len(password),3):
        front = password[i:i+3]
        afront = front.isalpha()
        back = password[i+3:i+8]
        aback = back.isdigit()
        if (afront == True and aback == True):
            if (len(front) == 3 and len(back) == 4):
                score -= 2  
                print("License: -2")
    return score
        
def score_common(password):
    password = password.lower()
    s = 0
    for i in hw4_util.part1_get_top():
        if (password == i):
            s -= 3
            print ("Common: -3")
            break
    return s

# Method calls to help calculate score
score += score_length(password)
score += score_case(password)
score += score_digits(password)
score += score_punctuation(password)
score += score_nylicense(password)
score += score_common(password)
print("Combined score:", score)

# Nested If Statements to determine quality of password
if (score <= 0):
    print ("Password is rejected")
elif (score == 1 or score == 2):
    print("Password is poor")
elif (score == 3 or score == 4):
    print ("Password is fair")
elif (score == 5 or score == 6):
    print ("Password is good")
else:
    print ("Password is excellent")
