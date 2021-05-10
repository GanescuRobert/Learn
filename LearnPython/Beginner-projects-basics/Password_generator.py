# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 12:20:44 2020

@author: robyb
"""

import random
import string

def checkConditions(num_char,num_upper,num_lower,num_digits,num_symbols):
    return num_char==(num_upper+num_lower+num_digits+num_symbols)

while True:
    num_char = int(input("Number of characters in your passwrds: "))
    
    num_upper = int(input("How many uppercase letters in your passwrds: "))
    num_lower = int(input("How many lowercase letters in your passwrds: "))
    num_digits = int(input("How many digits in your passwords: "))
    num_symbols = int(input("How many symbols in your passwords: "))
    
    if checkConditions(num_char,num_upper,num_lower,num_digits,num_symbols):
        break;
    else: 
        print("Conditions doesn't match. Try again!")

password = ''
password +=''.join(random.choice(string.ascii_uppercase) for _ in range(num_upper))
password +=''.join(random.choice(string.ascii_lowercase) for _ in range(num_lower))
password +=''.join(random.choice(string.digits) for _ in range(num_digits))
password +=''.join(random.choice(string.punctuation) for _ in range(num_symbols))

_ = list(password)
random.shuffle(_)
password=''.join(_)

print(password)