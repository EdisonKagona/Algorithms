# -*- coding: utf-8 -*-
"""
Created on Tue May  5 12:46:40 2020

@author: Edison
"""
"""
In this little assignment you are given a string of space separated numbers, 
and have to return the highest and lowest number.
Example:
high_and_low("1 2 3 4 5")  # return "5 1"
high_and_low("1 2 -3 4 5") # return "5 -3"
high_and_low("1 9 3 4 -5") # return "9 -5"
Notes:
i.	All numbers are valid Int32, no need to validate them.
ii.	There will always be at least one number in the input string.
iii.	Output string must be two numbers separated by a single space, and highest number is first.
"""

def newOutput(lists):
    maxval = max(lists)
    minval = min(lists)
    return f'{maxval} {minval}'

lists = [1,9,3,4,-5]
print(newOutput(lists))

