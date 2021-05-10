# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 21:59:10 2020

@author: robyb
"""

import random

def get_average(a_list):
    total=0
    for mark in a_list:
        total+=mark
    avg=total/len(a_list)
    return avg

mark_list = []
average_list = []
mark_list=list(list(random.randint(50,100) for cols in range(random.randint(5,10))) for lines in range(5))
    
for lis in mark_list:
    average_list.append(get_average(lis))
    
print(average_list)
print('The school',average_list.index(max(average_list)),'has the highest avarage equal with:',max(average_list))