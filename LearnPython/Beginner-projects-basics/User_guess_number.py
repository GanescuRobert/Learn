# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 20:57:19 2020

@author: robyb
"""

import random as rd

play_game=''

while play_game!='q':
    answer=rd.randint(1,100)
    try_number=int(input('Guess a number between 1-100:'))
    try_number_times=1
    while answer!=try_number:
        if try_number>answer:
            print('Number is too large !')
        else:
            print('Number is too small !')
        try_number=int(input('Guess a number between 1-100:'))
        try_number_times+=1
    print('Well, you got it! You tried '+str(try_number_times)+' times')
    play_game=input('Press enter to play again!\nType "q" to exit: ')