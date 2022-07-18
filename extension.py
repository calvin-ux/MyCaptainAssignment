"""
Program to extract extention from filename
@author: Calvin
"""
#using example abc.py 
f_name = input("Enter a filename to extract: ")

file = f_name.split(".")

f_extension = file[-1]

print("Extension of the file is: ", f_extension)