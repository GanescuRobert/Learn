# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 09:25:13 2020

@author: robyb
"""

import random
import string 

students_marks = []
number_tests=random.randint(5,10)
number_students =random.randint(10,20)

for _ in range(number_students):
    students_name = ''.join(random.choice(string.ascii_letters) for _ in range(random.randint(3,7)))
    marks_student = list(random.randint(50,100) for _ in range(number_tests))
    students_marks.append([students_name,marks_student])


avg_tests = [0]*number_tests
for name,marks in students_marks:
    print(name,marks)
    for test in range(number_tests):
        avg_tests[test]+=marks[test]

_=1
for avg_test in avg_tests:
    print(_,avg_test/number_students,sep=':')
    _+=1