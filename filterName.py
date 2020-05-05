# -*- coding: utf-8 -*-
"""
Created on Tue May  5 09:38:32 2020

@author: Edison Kagona
"""
"""
Make a program that filters a list of strings and returns a list with only your friends name in it.
If a name has exactly 4 letters in it, you can be sure that it has to be a friend of yours! Otherwise, you can be sure he's not...
Ex: Input = ["Ryan", "Kieran", "Jason", "Yous"], Output = ["Ryan", "Yous"]

"""
def nameList(names):
    new_list = [i for i in names if len(i) == 4]
    return new_list
names = ["Ryan", "Kieran", "Jason", "Yous"]
print(nameList(names))

#Another way

def findMe(j):
    nameslist = []
    for i in j:
        if len(i) == 4:
            nameslist.append(i)
    return nameslist
j = ["Ryan", "Kieran", "Jason", "Yous"]
print(findMe(j))