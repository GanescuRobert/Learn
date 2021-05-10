# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 19:40:03 2020

@author: robyb
"""

import random
import time


class ArithmeticGame:
    def __init__(self,num_questions):
        self.num_questions = num_questions
        self.num_correct_questions = 0
    
    def generate_question(self):
        operand_1 = random.randint(1,30)
        operand_2 = random.randint(1,30)
        operator = random.choice('+-*/')
        question = '{}{}{}='.format(operand_1,operator,operand_2)
        if operator == '+':
            answer = operand_1+operand_2
        elif operator == '-':
            answer = operand_1-operand_2
        elif operator == '*':
            answer = operand_1*operand_2
        elif operator == '/':
            answer = int(operand_1/operand_2)
        return question,answer

    def play_game(self):
        start_time = time.time()

        for i in range(self.num_questions):
            print('Question',i+1,':')
            question,answer=self.generate_question()
            user_answer=int(input(question))
            if user_answer==answer:
                self.num_correct_questions+=1
                print('Correct answer')
            else:
                print('Wrong answer, Correct answer is',answer)
            
        end_time = time.time()
        print ('It took you',end_time-start_time,'seconds to solve',self.num_questions)
        print('Which correct solved is',self.num_correct_questions)

new_game = ArithmeticGame(10)
new_game.play_game()