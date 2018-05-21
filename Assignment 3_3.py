# -*- coding: utf-8 -*-
"""
Created on Fri May 18 10:59:40 2018  @author: krishna.i

Assignment 3.3: Implement a function longestWord() that takes a list of words 
and returns the longest one

"""
def longestWord(myStr):
    myls = myStr.split(sep=" ")
    print("List of words as entered: ",myls)
    return max(myls,key=len)

sampleStr = input("Please Enter a String: ")
longWord = longestWord(sampleStr)
print("Here is the longest word in in the list: ", longWord)
