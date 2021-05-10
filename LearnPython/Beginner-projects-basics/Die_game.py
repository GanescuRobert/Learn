# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 08:57:25 2020

@author: robyb
"""

import random


quit_game = False
user_wins = 0
computer_wins = 0
while quit_game is False:
    print('\nScore is: User {} - Computer {}\nNew game.\nUser position is 0\nComputer position is 0'.format(user_wins,computer_wins))
    start_place = 0
    end_place = 40
    user_place = 0
    computer_place = 0
    user_win = False
    computer_win = False    
    while not user_win or not computer_win:
        
        user_input = input("Enter 't' to toss the die, or 'q' to end: ")
        
        if user_input == 'q':
            quit_game = True
            break
        if user_input == 't':
            #user turn
            user_move = random.randint(1,6)
            user_place += user_move
            print('You move for',user_move,'steps')
            if user_place == end_place:
                user_win = True
                user_wins+=1
                print('User win this game!\n')
                break    
            if user_place > end_place:
                overshoot = user_place - end_place
                user_place = end_place - overshoot
            print('Your position is',user_place,'\n')    
            #computer turn
            computer_move = random.randint(1,6)
            computer_place += computer_move
            print('Computer move for',computer_move,'steps')
            if computer_place == end_place:
                computer_win = True
                computer_wins +=1
                print('Computer win this game!\n')
                break    
            if computer_place > end_place:
                overshoot = computer_place - end_place
                computer_place = end_place - overshoot       
            print('Computer position is',computer_place)
       