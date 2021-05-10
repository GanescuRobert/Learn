# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 21:32:05 2020

@author: robyb
"""

import random as rd
import time

def printDot():
    print('.',end=' ')
    time.sleep(0.5)
    
def printDots(quantity):
    for q in range(quantity):
        printDot()
        
play_game=''
start=1
end=100
case='N'
while play_game!='q':
    smallest=start
    biggest=end
    try_number_times=1
    
    print("Computer generate number:")
    printDots(3)
   
    try_number=rd.randint(smallest,biggest)
    print("\nNumber generated is "+str(try_number))
    case=input("Number is to large(L)\nNumber is to small(S)\nNumber is found(F)\nHow it is ?")    
    
    while case!='F':
        print("Computer generate number:")
        printDots(3)
        if case == 'L':
           biggest=try_number-1
        else:
           smallest=try_number+1
           
        try_number=rd.randint(smallest,biggest)    
        print("\nNumber generated is "+str(try_number))
        case=input("Number is to large(L)\nNumber is to small(S)\nNumber is found(F)\nHow it is ?")    
        try_number_times+=1
        
    print('Well, I got it! I tried '+str(try_number_times)+' times')
    play_game=input('Press enter to play again!\nType "q" to exit: ')
   
        
    