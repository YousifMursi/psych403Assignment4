# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 16:34:24 2022

@author: yousi
"""
#Q1
name=['Y','O','U','S','I','F']
for index in name:
    print(name)

#Q2
counter = ['1','2','3','4','5','6']
for i in range(6):
    combin=name[i]+counter[i]
    print(combin)
        
#NESTED Q3&4

list=['AMY','RORY','RIVER']
count=0
#NESTED LOOP LETTERS
for names in list:
    for letters in names:
        print(letters)

#NESTED LOOP WITH COUNTER !!NEED TO MAKE  START OVER FOR EACH STRING
for names in list:
    for letters in names:
        print(letters+str(count))
        count +=1


    