# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 12:20:29 2022

@author: yousi
"""

#while loop exercises

count=0
while count <20:
    for count in range(0,10):
        if count<10:
            print('image1.png')
        print(count)
        count+=1
    for count in range(10,20):
        if count<20:
            print('image2.png')
        print(count)
        count+=1
#completed Q1
#Q2
response=input('enter a response')

maxiterations=5

import random   
while response !="1" and response != "2" and maxiterations!=0:
    images=random.randint(0,10)
    response =input("enter response:")
    print(f'image {str(images)}')
    maxiterations -=1

    
