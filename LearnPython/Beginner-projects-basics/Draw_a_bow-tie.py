# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 10:01:28 2020

@author: robyb
"""

size=12
stars = [*range(1,int(size/2)+1)]+[*range(int(size/2)+int(size%2==1),0,-1)]
print(stars)

for line in stars:
    fStars = '*'    *   (line)
    iSpaces= ' '    *   (2* (int(size/2)+(size%2==1)-line)  )
    eStars = '*'    *   (line)
    print(fStars+iSpaces+eStars)
    