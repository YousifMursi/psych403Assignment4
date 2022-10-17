# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 16:34:20 2022

@author: yousi
"""

#Conditional Exercises

#Q1
response=input('enter response')

if response== '1' or response== '2':
    print("OK")
elif len(response) == 0:
    print('subject did not respond')
else: print('subject pressed wrong key')

#Q2
if response=='1' and not response=='2':
        print('Correct!')
if response=='2':
    print('Incorrect!')
    
#Q3 - The script replied in the fashion it should, with an input of 1 in the console we get the response "OK" and "Correct!", and for the response 2 we get "OK" and "Incorrect!"


