# -*- coding: utf-8 -*-
"""
Print all Positive numbers in a range
@author: Calvin
"""
#Given list1 = [12, -7, 5, 64, -14]
#Given list2 = [12, 14, -95, 3]

"""        
#end=' ' doesn't go on newline by passing whitespace(space)
therefore the values are in same line

#default print function is newline
"""

list1 = [12, -7, 5, 64, -14]
list2 = [12, 14, -95, 3]

print("Program to print Positive Number from range")

print("Input:list1 =", list1)
print("Output:", end=' ')

for i in list1:
    if i >= 0:
        print(i,end=' ')
print(" ")

print("Input:list2 =", list2)
print("Output:", end=' ')

for i in list2:
    if i >= 0:
        print(i,end=' ')
        
        
