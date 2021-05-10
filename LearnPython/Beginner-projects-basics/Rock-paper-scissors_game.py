# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 11:13:50 2020

@author: robyb
"""
import random


possible_moves=['rock','paper','scissors']
quit_game = False
while not quit_game:
    user_wins = 0
    computer_wins =0
    draw_match=0
    play=True
    while play: 
        print("Score is:\n User {} - Draw {} - Computer {}\n Game start\n".format(user_wins,draw_match,computer_wins))
        user_move=input("Type your move: 'rock', 'paper' or 'scissors' (q for exit)")
        if user_move=='q':
           quit_game=True
           break
        computer_move=random.choice(possible_moves)
        if user_move==computer_move:
            print("Draw match")
            draw_match+=1
            continue
        elif (user_move=='rock' and computer_move=='scissors') or\
             (user_move=='paper' and computer_move=='rock') or\
             (user_move=='scissors' and computer_move=='paper'):
                 print('User win')
                 user_wins+=1
        else:
            print('Computer win')
            computer_wins+=1
                    
               
            