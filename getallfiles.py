# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 14:37:42 2019

@author: Akshay
"""
from os import listdir

filepath = "C:/Users/Akshay/Desktop/MillionSongSubset/data"

level_one = 65
level_two = 65
level_three = 65

while level_one < 66:
    while level_two<66:
        while level_three<66:
            mypath = filepath+"/"+chr(level_one)+"/"+chr(level_two)+"/"+chr(level_three)
            #onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
            for f in listdir(mypath):
                print(f)
            level_three+=1
        level_two+=1
    level_three+=1
            
        