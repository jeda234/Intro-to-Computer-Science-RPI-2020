# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 21:57:25 2020

@author: cowarj
"""

# Encrypting Code - Purpose is to return a ciphered version of 
# the string the user inputted

def encrypt(string):
    encrypted = s
    encrypted = encrypted.replace(" a", "%4%")
    encrypted = encrypted.replace("he", "7!")
    encrypted = encrypted.replace("e", "9(*9(")
    encrypted = encrypted.replace("y", "*%$")
    encrypted = encrypted.replace("u", "@@@")
    encrypted = encrypted.replace("an", "-?")
    encrypted = encrypted.replace("th", "!@+3")
    encrypted = encrypted.replace("o", "7654")
    encrypted = encrypted.replace("9", "2")
    encrypted = encrypted.replace("ck", "%4")
    return encrypted

# Decrypting Code - Purpose is to return an English version
# of the ciphered phrase
def decrypt(s):
     decrypted = s
     decrypted = decrypted.replace("%4", "ck")
     decrypted = decrypted.replace("2", "9")
     decrypted = decrypted.replace("7654", "o")
     decrypted = decrypted.replace("!@+3", "th")
     decrypted = decrypted.replace("-?", "an")   
     decrypted = decrypted.replace("@@@", "u") 
     decrypted = decrypted.replace("*%$", "y")
     decrypted = decrypted.replace("9(*9(", "e")
     decrypted = decrypted.replace("7!", "he")
     decrypted = decrypted.replace("%4%", " a")  
     return decrypted
# Input statements
s = input("Enter a string to encode ==> ")
print (s)
print("")

e = encrypt(s)
d = decrypt(e)

# Final printed code
print("Encrypted as ==> ", e)

# Finding the length
dif = len(e)-len(s)

print("Difference in length ==> ", dif)
print("Deciphered as ==> ", d)

# Finding out if word is reversible
if(s == d):
    word = "reversible"
else:
    word = "not reversible"

print("Operation is ", word, " on the string.", sep='')
