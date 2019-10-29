#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 21:54:26 2019

@author: elliott
"""

import spacy                                                                                                                            

nlp = spacy.load('en_core_web_sm')                                                                                                                

def parser(string):
    sents = nlp(string) 
    for ent in sents.ents:
        if ent.label_ == "PERSON":
            output.write(ent.text)
            output.write("\n")

def reader(file):
    source = open(file,"r")
    line = source.readlines()
    for x in range(10000):
        parser(line[x])

if __name__ == "__main__":
    output = open("answer.txt", "w+")
    reader("sents_BNCbaby.txt")      
    output.close()
#    output = open("answer.txt", "r")
#    if output.mode == 'r':
#        contents = output.read()
#        print(contents) 
                                                                                        