# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 20:54:18 2020

@author: cowarj
"""
def drop (word, dictionary):
    """
    Method that takes list of words and drops one letter to see 
    if the word is a possible substitute
    
    Parameters
    ----------
    word : LIST
        list of a bunch of words
    dictionary : LIST
        list of words

    Returns
    -------
    words : LIST
        list of tuples with words and frequencies

    """
    words = []
    word_parts = []
    for i in word:
        word_parts.append(i)
    for j in range(0, len(word_parts)):
        w = word_parts[:j] + word_parts[j+1:len(word_parts)]
        w = str(w)
        w = w.replace("[", "").replace("'", "")\
            .replace("]", "").replace(",", "").replace(" ", "")
        w = w.strip()
        if (w in dictionary):
            words.append((dictionary[w], w))
    return words     

def insert (word, dictionary, keyboard):
    """
    Method that takes list of words and inserts one letter to see 
    if the word is a possible substitute
    
    Parameters
    ----------
    word : LIST
        list of a bunch of words
    dictionary : LIST
        list of words
    keyboard : LIST
        list of letters and their possible substitutes

    Returns
    -------
    words : LIST
        list of tuples with words and frequencies

    """
    words = []
    word_parts = []
    for i in word:
        word_parts.append(i)
    for j in range(0, len(word_parts)):
        for f in keyboard:
            w = word_parts[:j] + list(f) + word_parts[j:len(word_parts)]
            w = str(w)
            w = w.replace("[", "").replace("'", "")\
            .replace("]", "").replace(",", "").replace(" ", "")
            w = w.strip()
            if (w in dictionary):
                words.append((dictionary[w], w))
    return words     
    
def swap (word, dictionary):
    """
    Method that takes list of words and switches consecutive letters to
    see if the word is a possible substitute
    
    Parameters
    ----------
    word : LIST
        list of a bunch of words
    dictionary : LIST
        list of words

    Returns
    -------
    words : LIST
        list of tuples with words and frequencies

    """
    words = []
    word_parts = []
    for i in word:
        word_parts.append(i)
    for j in range(0, len(word_parts)-1):
        x = [word_parts[j+1],word_parts[j]]
        w = word_parts[:j] + x + word_parts[j+2:len(word_parts)]
        w = str(w)
        w = w.replace("[", "").replace("'", "")\
            .replace("]", "").replace(",", "").replace(" ", "")
        w = w.strip()
        if (w in dictionary):
            words.append((dictionary[w], w))
    return words

def replace (word, dictionary, keyboard):
    """
    Method that takes list of words and replaces one letter with
    a letter subsitutue to see if the word is a possible substitute
    
    Parameters
    ----------
    word : LIST
        list of a bunch of words
    dictionary : LIST
        list of words
    keyboard : LIST
        list of letters and their possible substitutes

    Returns
    -------
    words : LIST
        list of tuples with words and frequencies

    """
    dictionary2=[i.strip() for i in dictionary]
    words = []
    word_parts = []
    for i in word:
        word_parts.append(i)
    for j in range(0, len(word_parts)):
        for f in keyboard[word_parts[j]]:
            w=word_parts.copy()
            w[j]=f
            w = str(w)
            w = w.replace("[", "").replace("'", "")\
            .replace("]", "").replace(",", "").replace(" ", "")
            w = w.strip()
            if (w in dictionary2):
                words.append((dictionary[w], w))
    return words

def autocorrect(word, dictionary, keyboard):
    """
    Method that calls drop, insert, swap, and replace
    and adds all of the possible autocorrected words.

    Parameters
    ----------
    word : LIST
        list of a bunch of words
    dictionary : LIST
        list of words
    keyboard : LIST
        list of letters and their possible substitutes

    Returns
    -------
    A list casted as a set casted as a list with all of the 
    autocorrected words

    """
    l1 = drop(word, dictionary)
    l2 = insert(word, dictionary, keyboard)
    l3 = swap(word, dictionary)
    l4 = replace(word, dictionary, keyboard)
    l = l1 +l2 +l3+ l4
    return(list(set(l)))

dic_file = input("Dictionary file => ")
print(dic_file)
input_file = input("Input file => ")
print(input_file)
key_file = input("Keyboard file => ")
print(key_file)

dic_file = open(dic_file).read()
dic_file = dic_file.split("\n")
d = dict([])
for i in dic_file:
     i = i.split(",")
     if len(i) >1:
         d[i[0].strip()] = float(i[1].strip())
sub_letters = dict([])
key_file = open(key_file).read()
key_file = key_file.split("\n")
for j in key_file:
    j = j.split()
    if len(j)>1:    
        sub_letters[j[0].strip()] = j[1:len(j)]
        
input_file = open(input_file)
for k in input_file:
    k = k.strip()
    if (k in d):
        print((15-len(k))*" "+k+" -> FOUND")
        continue
    l = autocorrect(k, d, sub_letters)
    l = sorted(l)
    if (len(l) == 0):
        print((15-len(k))*" "+k+" -> NOT FOUND")
    elif(len(l) <= 3):
        print((15-len(k))*" "+k+" -> FOUND  {}:  ".format(len(l)), end='')
        for i in range(0, len(l)):
            print(l[len(l)-1-i][1], end='')
            if (i != len(l)-1):
                print(" ", end="")
        print()
    else:
        print((15-len(k))*" "+k+" -> FOUND  {}:  ".format(len(l)), end='')
        for i in range(0, 3):
            print(l[len(l)-1-i][1], end='')
            if (i != 2):
                print(" ", end="")
        print()