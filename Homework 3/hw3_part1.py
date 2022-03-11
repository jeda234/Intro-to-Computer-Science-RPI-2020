# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 17:39:53 2020

@author: cowarj
"""

import syllables

x = input("Enter a paragraph => ")
print(x)

def calculate_asl(word):
    i = 0
    L = [".","!","?",]
    while (i < len(L)):
        word = word.replace(L[i],"")
        i += 1
    return int(len(word)/i)

def calculate_phw(word):
    x = word.split(" ")
    y = []
    i = 0
    while (i<len(x)):
        if(syllables.find_num_syllables(word[i])>=3 and word[i].find("-")==-1):
            y.append(x[i])
        i+=1
    return ((len(y)/len(x))*100), y

def calculate_aysl(word):
    x = word.split(" ")
    i = 0
    z = 0
    while (i<len(x)):
        z+= syllables.find_num_syllables(word[i])
        i+=1
    return(z/len(x))

asl = calculate_asl(x)
phw, hard_words = calculate_phw(x)
aysl = calculate_aysl(x)
gfri = 0.4*(asl + phw)
fkri = 206.835-1.015*asl-86.4*aysl

print("")
print("Here are the hard words in this paragraph:")
print (hard_words)
print ("Statistics: ASL:", asl, " PHW:", phw, "% ASYL:", aysl, sep="")
print ("Readability index (GFRI): {:.2f}".format(gfri), sep="")
print ("Readability index (FKRI): {:.2f}".format(fkri), sep="")
