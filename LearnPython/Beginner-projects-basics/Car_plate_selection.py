# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 21:04:52 2020

@author: robyb
"""

import random as rd
import string


def generate_days():
    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    odd_days=[]
    even_days=[]
    for d in range(len(days)):
        if((d+1)%2):
            odd_days.append(days[d])
        else:
            even_days.append(days[d])
    return odd_days,even_days

def generate_plates():
    car_plates=[]
    for i in range(10):
        char_plate = ''.join(rd.choice(string.ascii_letters)for i in range(2))
        numeric_plate = ''.join(rd.choice(string.digits)for i in range(4))
        car_plates.append(char_plate+numeric_plate)
    return car_plates

car_plates = generate_plates()
odd_days,even_days = generate_days()

today = input('Enter the current day of the week: ')

car_plates_availabale= []
for car_plate in car_plates:
    last_digit=int(car_plate[-1])
    if today in odd_days and last_digit%2==1:
        car_plates_availabale.append(car_plate)
    elif today in even_days and last_digit%2==0:
        car_plates_availabale.append(car_plate)        

print(odd_days,even_days,sep='\n')
print(car_plates)
print(car_plates_availabale)