# -*- coding: utf-8 -*-
"""

@author: Calvin
"""
"""
letter = {
    "m" : 0,
    "s" : 0,
    "p" : 0,
    "i" : 0
    }

def most_frequent(word):
   for i in word:
       if i == "m":
           letter["m"] = letter["m"] + 1
       elif i == "p":
           letter["p"] = letter["p"] + 1
       elif i == "s":
           letter["s"] = letter["s"] + 1
       elif i == "i":
           letter["i"] = letter["i"] + 1
           print(letter)

most_frequent("mississippi")
"""

letter = {
    "m" : 0,
    "i" : 0,
    "s" : 0,
    "p" : 0
    }

print("Input: mississippi")

def most_frequent(word="default args"):
   for i in word: 
       if i == "m":
           letter["m"] = letter["m"] + 1
       elif i == "i":
           letter["i"] = letter["i"] + 1
       elif i == "s":
           letter["s"] = letter["s"] + 1
       elif i == "p":
           letter["p"] = letter["p"] + 1 
   print("Count of each letter: ", letter)
   change_val = ((value, key) for (key,value) in letter.items())
   desc_values = sorted(change_val, reverse=True)
   print("Descending Output: ", desc_values)   

most_frequent("mississippi")







letter = {"Math": 34, "Science": 12, "English": 89, "Physics": 8}
change_do = ((value, key) for (key,value) in letter.items())
desc_values = sorted(change_do, reverse=True)
print(desc_values)

