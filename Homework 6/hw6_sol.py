# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 12:38:29 2020

@author: cowarj
"""

def parse(file):
    """
    This method will parse through a file and return a list with all the words 
    in the file that are not considered stop words or numbers.
    
    Parameters
    ----------
    file : STRING
        string that will be opened as a file to parse through
        
    s : LIST
        list that contains the list of stop words

    Returns
    -------
    listwords : LIST
        list of words that can be evaluted from the file given

    """
    file = open(file)
    s = set([i.strip().replace("'","") for i in open("stop.txt")])
    listwords = file.read().lower().split()
    for i in range(len(listwords)):
        for j in listwords[i]:
            if j.isalpha() == False:
                listwords[i]=listwords[i].replace(j,"")
    listwords = [i for i in listwords if i!="" and i not in s]
    return listwords
 
def avg_word_length(filewords):
    """
    This method finds the average word length within a given file

    Parameters
    ----------
    filewords : LIST
        list that will be used to find the average word length

    Returns
    -------
    avg : FLOAT
        average word length within given file with two decimal points

    """
    length = sum([len(i) for i in filewords])
    avg = length/len(filewords)
    return avg

def ratio(filewords):
    """
    This method calculates the ratio between the number of distinct ords and 
    the total nnumber of words.

    Parameters
    ----------
    filewords : LIST
       list that will be used to find the average word length

    Returns
    -------
    ratio : FLOAT
        variable that contains the calculated ratio

    """
    d = list(dict.fromkeys(filewords))
    ratio = len(d)/len(filewords)
    return ratio

def word_length(filewords):
    """
    This method prints out lengths of words in a list format

    Parameters
    ----------
    filewords : LIST
        list of words in file used to calculate length

    Returns
    -------
    None.

    """
    filewords = list(set(filewords))
    l = []
    lenlist = [len(i) for i in filewords]
    longnum = max(lenlist)+1
    for j in range(1, longnum):
        l = sorted([x for x in filewords if len(x) == j])
        space = 4-len(str(j))
        spacee = 4-len(str(len(l)))
        print(" "*space,str(j),":"," "*spacee,len(l),sep="",end=":")
        if (len(l) <= 6):
            for k in l:
                print(" "+k, end="")
        else:
            print("", l[0], l[1], l[2], "...", l[-3], l[-2], l[-1], end="")
        print("")
            
def word_pairs(filewords, maxstep):
    """
    This function will return a list of word pairs in given line
    
    Parameters
    ----------
    filewords : LIST
        list of words in file used to create word pairs
    maxstep : INT
        max step pairs can take

    Returns
    -------
    pairlist : LIST
        list of all the word pairs in a list

    """
    pairlist = []
    for i in range(len(filewords)):
        for j in range(1, maxstep+1):
            if j+i < len(filewords):
                f=sorted([filewords[i],filewords[i+j]])
                pairlist.append(tuple(f))
    return(pairlist)
            
def distinct_word_pairs(pairs):

    """
    Prints the distinct pair in formats

    Parameters
    ----------
    pairs : LIST
        list of pairs from a given set of list

    Returns
    -------
    None.

    """
    pairs = sorted(list(set(pairs)))
    print(" "*(6-len(str(len(pairs)))+2) + str(len(pairs)) + " distinct pairs")
    if (len(pairs) <= 6):
        for i in pairs:
            print("  ", i[0], " ", i[1], sep="")
    else:
        for x in range(0,5):
           print("  ", pairs[x][0], " ", pairs[x][1], sep="")
        print("  ...")
        for x in range(-5, 0):
            print("  ", pairs[x][0], " ", pairs[x][1], sep="")
        
def pair_ratio(filewords, maxstep):
    """
    Calculates the ratio between the pairs on the files
    
    Parameters
    ----------
    filewords : LIST
        list of words in a file used to find pairs
    
    maxstep: INT
        maximum number of steps the word pair can take

    Returns
    -------
    FLOAT
        the ratio of distinct pairs to total pairs

    """
    x = len(word_pairs(filewords, maxstep))
    y = len(set(word_pairs(filewords, maxstep)))
    return y/x

def jac_word_use(filewords1, filewords2):
    """
    Finds the Jaccard similiarity of average word length

    Parameters
    ----------
    filewords1 : LIST
        list that includes words in file 1
    filewords2 : LIST
        list that includes words in file 2

    Returns
    -------
    FLOAT
        jaccard similiarity of word use

    """
    f1 = set(filewords1)
    f2 = set(filewords2)
    return (len(f1 & f2)/len(f1 | f2))
    
def jac_word_length(file1words, file2words):
    """
    Finds the Jaccard similiarity of the length of words

    Parameters
    ----------
    filewords1 : LIST
        list that includes words in file 1
    filewords2 : LIST
        list that includes words in file 2

    Returns
    -------
    None.

    """
    listword1 = sorted(list(set(file1words)))
    listword2 = sorted(list(set(file2words)))
    maxw1 = set([len(i) for i in listword1])
    maxw2 = set([len(i) for i in listword2])
    maxw = max(max(maxw1), max(maxw2))+1
    for l in range(1, maxw):
        maxw1 = set([i for i in listword1 if len(i)==l])
        maxw2 = set([i for i in listword2 if len(i)==l])
        t = len(maxw1 & maxw2)
        b = len(maxw1 | maxw2)
        if (b == 0):
            jac = 0
        else:
            jac = t/b
        space = " "*(4-len(str(l)))
        print(space, l, ": {:.4f}".format(jac), sep="")
        
def jac_pair(filewords1, filewords2, maxstep):
    """
    Finds the Jaccard similiarity of the pair of words

    Parameters
    ----------
    filewords1 : LIST
        list that includes words in file 1
    filewords2 : LIST
        list that includes words in file 2
    maxstep : INT
        number of maximum steps

    Returns
    -------
    FLOAT
        jaccard similarity of the word pairs

    """
    f1 = set(word_pairs(filewords1, maxstep))
    f2 = set(word_pairs(filewords2, maxstep))
    return len(f1 & f2) / len(f1 | f2)

if __name__ == "__main__":

    file1 = input("Enter the first file to analyze and compare ==> ")
    print(file1)  
    file2 = input("Enter the second file to analyze and compare ==> ")
    print(file2)
    max_sep = int(input("Enter the maximum separation between words in a pair ==> "))
    print(max_sep)
    print("")
    file1words = parse(file1)
    file2words = parse(file2)

# Evaulating the First Document
    print("Evaluating document", file1)
    print("1. Average word length: {:.2f}".format(avg_word_length(file1words)))
    print("2. Ratio of distinct words to total words: {:.3f}".format(ratio(file1words)))
    print("3. Word sets for document {}:".format(file1))
    word_length(file1words)
    print("4. Word pairs for document {}".format(file1))
    pairs1 = word_pairs(file1words, max_sep)
    distinct_word_pairs(pairs1)
    print("5. Ratio of distinct word pairs to total: {:.3f}".format(pair_ratio(file1words, max_sep)))
    print("")

# Evaluating the Second Document
    print("Evaluating document", file2)
    print("1. Average word length: {:.2f}".format(avg_word_length(file2words)))
    print("2. Ratio of distinct words to total words: {:.3f}".format(ratio(file2words)))
    print("3. Word sets for document {}:".format(file2))
    word_length(file2words)
    print("4. Word pairs for document {}".format(file2))
    pairs2 = word_pairs(file2words, max_sep)
    distinct_word_pairs(pairs2)
    print("5. Ratio of distinct word pairs to total: {:.3f}".format(pair_ratio(file2words, max_sep)))
    print("")
    
# Summary Comparison
    print("Summary comparison")
    if (avg_word_length(file1words) > avg_word_length(file2words)):
        print("1. {} on average uses longer words than {}".format(file1, file2))
    else:
        print("1. {} on average uses longer words than {}".format(file2, file1))
    print("2. Overall word use similarity: {:.3f}".format(jac_word_use(file1words, file2words)))
    print("3. Word use similarity by length:")
    jac_word_length(file1words, file2words)
    print("4. Word pair similarity: {:.4f}".format(jac_pair(file1, file2, max_sep)))