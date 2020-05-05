# -*- coding: utf-8 -*-
"""
Created on Tue May  5 07:56:09 2020

@author: Edison Kagona
"""
""" 
In this kata you will create a function that takes a list of non-negative integers and strings
 and returns a new list with the strings filtered out.
Example
filter_list([1,2,'a','b']) == [1,2]
filter_list([1,'a','b',0,15]) == [1,0,15]
filter_list([1,2,'aasf','1','123',123]) == [1,2,123]
"""
def filter_list(j):
    new_list = [ ]
    for i in j:
        if type(i) == int:
            new_list.append(i)
    return new_list
j = [1,2,'a','b']
print(filter_list(j))

#Another method

def filterMe(random):
    newList = [a for a in random if type(a) == int]
    return newList
random = [1,'a','b',0,15]
print(filterMe(random))


