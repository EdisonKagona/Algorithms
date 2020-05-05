# -*- coding: utf-8 -*-
"""
Created on Tue May  5 07:45:57 2020

@author: Edison Kagona
"""
""" 
Write a function that takes in a string of one or more words, and returns the same string,
 but with all five or more letter words reversed (Just like the name of this Kata).
 Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.
Examples:
spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw" 
spinWords( "This is a test") => returns "This is a test" 
spinWords( "This is another test" )=> returns "This is rehtona test"

"""
def spinWords(sentence):
    words = sentence.split()
    new_words = [""]
    for word in words:
        if len(word) <= 5:
            new_words.append(word)
        else:
            new_words.append(word[::-1])
    new_sentence = " ".join(new_words)
    return new_sentence
sentence = input("Enter your sentence here")
print(spinWords(sentence))