# -*- coding: utf-8 -*-
"""
Created on Tue May  5 09:51:14 2020

@author: Edison
"""
"""
You have an array of numbers.
Your task is to sort ascending odd numbers but even numbers must be on their places.
Zero isn't an odd number and you don't need to move it. 
If you have an empty array, you need to return it.
Example
sort_array([5, 3, 2, 8, 1, 4]) == [1, 3, 2, 8, 5, 4]

"""

from collections import deque

def SortMe(sequence):
    toSort = deque(sorted([item for item in sequence if item%2]))
    new_list = []
    for item in sequence:
        if item%2 == 1:
            new_list.append(toSort.popleft())
        else:
            new_list.append(item)
    return new_list
sequence = [5, 3, 2, 8, 1, 4]
print(SortMe(sequence))        

#Returning items in descending order

def quick_sort(sequence):
    length = len(sequence)
    if length <= 1:
        return sequence
    else:
        pivot = sequence.pop()
    items_greater = []
    items_lower = []
    for item in sequence:
        if item > pivot:
            items_greater.append(item)
        else:
            items_lower.append(item)
    return quick_sort(items_greater) + [pivot] + quick_sort(items_lower)
sequence = [5, 3, 2, 8, 1, 4]
print(quick_sort(sequence))

def quick_sort(sequence):
    if len(sequence) <= 1:
        return sequence
    else:
        pivot = sequence.pop()
    items_greater = []
    items_lower = []
    for item in sequence:
        if item > pivot:
            items_greater.append(item)
        else:
            items_lower.append(item)
    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)
sequence = [5, 3, 2, 8, 1, 4]
print(quick_sort(sequence))




        