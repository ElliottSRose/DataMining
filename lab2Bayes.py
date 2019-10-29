#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 14:58:03 2019

@author: elliott
"""
#This program uses a regular expression in the parser function to 
#find all of the capitalized words. It then sends those words to the 
#bayesCheck function and runs a simplified naive bayes function to 
#further prune the words most-likely to be names. 

import re


def parser(lineNum, string):
    ans = re.findall( '[a-zA-Z]+\w+', string)
    ans = bayesCheck(ans)
    for i in ans:
        output.write(i + " ")
    output.write("\n")

def bayesCheck(ans):
    rating = 0
    toRemove= []
    if len(ans)>=1:
        for i in ans:
            if i[0].isupper()==True:
                rating+=1
            if len(ans)>1:
                rating+=1
            if len(i)>3:
                rating+=1
            if len(i)<9:
                rating+=1
            if rating<=3:
                toRemove.append(i)
            rating = 0
    for i in toRemove:
        ans.remove(i)
    return ans

def reader(file):
    source = open(file,"r")
    line = source.readlines()
    for x in range(10000):
        output.write(str(x+1) + " ")
        parser(x, line[x])

if __name__ == "__main__":
    output = open("answer.txt", "w+")
    reader("sents_BNCbaby.txt")      
    output.close()
    output = open("answer.txt", "r")
    if output.mode == 'r':
        contents = output.read()
        print(contents) 
        
#
    