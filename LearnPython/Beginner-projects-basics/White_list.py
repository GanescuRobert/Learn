# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 14:26:07 2020

@author: robyb
"""

black_list = ['Susan','John','Michael','Robert']

num_students= int(input('Enter number of students: '))
student_list=[]
white_list = []

for student in range(num_students):
    temp_student = input('Input a student name: ')
    while temp_student=='':
        temp_student = input('Input a non-empty student name: ')
    student_list.append(temp_student)
    
for student in student_list:
    if student not in black_list:
        white_list.append(student)

print('These students: ' + str(white_list) + ' graduated!')