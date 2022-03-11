# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 16:31:13 2020

@author: cowarj
"""
# Inputs and Defining Variables
sentence = input("Enter a sentence => ")
print(sentence)
happy_count = 0
sad_count = 0

# Defining the function that will count the amount of happy words in a sentence
def number_happy(sentence):
    sentence=sentence.lower()
    happy_count = sentence.count("laugh")
    happy_count += sentence.count("happiness")
    happy_count += sentence.count("love")
    happy_count += sentence.count("excellent")
    happy_count += sentence.count("good")
    happy_count += sentence.count("smile")
    return happy_count
  
# Defining the function that will count the amount of sad words in a sentence 
def number_sad(sentence):
    sentence=sentence.lower()
    sad_count = sentence.count("bad")
    sad_count += sentence.count("sad")
    sad_count += sentence.count("terrible")
    sad_count += sentence.count("horrible")
    sad_count += sentence.count("problem")
    sad_count += sentence.count("hate")
    return sad_count

happy_count = number_happy(sentence)
sad_count = number_sad(sentence)
print("Sentiment: " + ("+"*happy_count) + ("-"*sad_count), sep="")
if (happy_count > sad_count):
    print ("This is a happy sentence.")
elif (happy_count < sad_count):
    print ("This is a sad sentence.")
else:
    print("This is a neutral sentence.")
