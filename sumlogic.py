# -*- coding: utf-8 -*-
"""
Created on Tue May  5 13:07:45 2020

@author: Edison Kagona
"""
"""
15.	Given two integers a and b, which can be positive or negative, find the sum of all the numbers between including them too and return it. If the two numbers are equal return a or b.
Note: a and b are not ordered!
Examples
get_sum(1, 0) == 1   // 1 + 0 = 1
get_sum(1, 2) == 3   // 1 + 2 = 3
get_sum(0, 1) == 1   // 0 + 1 = 1
get_sum(1, 1) == 1   // 1 Since both are same
get_sum(-1, 0) == -1 // -1 + 0 = -1
get_sum(-1, 2) == 2  // -1 + 0 + 1 + 2 = 2
"""

def get_sum(a,b):
    if a == b:
        return a
    s = 0
    for i in range(min(a,b), max(a,b)+1):
        s+=i
        return s
print(get_sum(-1,0,))

