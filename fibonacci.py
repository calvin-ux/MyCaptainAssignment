# -*- coding: utf-8 -*-
"""
Fibonacci Series Program
@author: Calvin
"""
#Output Required :0 1 1 2 3 5 8 13 21 34 55 89 144 


print("Program to print Fibonacci series")
a = 0 
b = 1
#a,b are seed values to start the fibonacci sseries
num = int(input("Enter a number to start fibonacci series: "))
if num <= 0:
    print("Wrong number entered!!! TRY AGAIN")
else:
    print("Fibonacci Series:", a, b, end=" ")
    
#starting from index no.2 in num[0,1,1...nth] range
for i in range(2, num):
    c = a + b
    a = b
    b = c
    print(c, end=" ")
