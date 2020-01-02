##!/usr/bin/env python3
## -*- coding: utf-8 -*-
#"""
#Created on Sat Nov 23 07:52:28 2019
#
#@author: elliott
#"""

#Name set is taken from http://answers.google.com/answers/threadview/id/711284.html

import spacy                                                                                                                            
nlp = spacy.load('en_core_web_sm')    
nameL = open('/Users/elliott/Documents/Frostburg_Fall2019/Data_Mining/names.txt', 'r')
nameList = [row.rstrip('\n') for row in nameL]   
lwrList = [word.lower() for word in nameList]                                                                                                         

def truecaser(string, nameList, lwrList):
#    This function uses Spacy to tokenize text and use those tokens
#    to identify whether a word needs ensure the correct casing of 
#    the word. First it checks to see if the word is at the beginning 
#    of the sentence, then whether it is a proper noun. If it is a 
#    proper noun, it then uses a binary search of a list of names 
#    with multiple capital letters to ensure correct casing. If the
#    words do not fit in these specifications, it ensures that the 
#    words is in lowercase. The function accepts a string and makes a
#    new and corrected version, and includes spacing. It returns the 
#    corrected sentence.
    sents = nlp(string)
    newstr = ''
    for token in sents:
        word = token.text
        if token.is_sent_start==True:
            word = word.lower().capitalize()
            newstr += word 
        elif token.pos_ == 'PROPN':
            lwrcase = word.lower()
            possibleName = Binary_Search(lwrList,lwrcase)
            if possibleName != -1:
                word = nameList[possibleName]
            else:
                word = word.lower().capitalize()
            newstr += ' ' + word 
        elif word !='.':
            word = word.lower()
            newstr+= ' ' + word    
        else:
            newstr += word
    return newstr
        
        
def Binary_Search(lst, word):
#    This function does a binary search on a list of strings and 
#    returns the index of the string if found, or -1 if not found. 
    start = 0
    end = len(lst) - 1
    while start <= end:
        middle = (start + end)// 2
        mid = lst[middle]
        if mid > word:
            end = middle - 1
        elif mid < word:
            start = middle + 1
        else:
            return middle
    return -1
       
testStr = 'jAmes mCnett iS A PerSon whO Loves fISHing.' 
print(truecaser(testStr, nameList, lwrList))
#This function call outputs: 'James McNett is a person who loves fishing.'