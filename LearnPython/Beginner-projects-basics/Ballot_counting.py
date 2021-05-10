# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 14:42:13 2020

@author: robyb
"""

polls = ['Ben','Andy','Ben','Andy','Carol','Carol',
         'Andy','Ben','Andy','Carol','Andy','Carol']

candidates = list(set(polls))

votes =[]
for person in candidates:
    votes.append(polls.count(person))

result=sorted(zip(candidates,votes), key=lambda x:x[1],reverse=True)

print ("The winner is:",end=' ')
for candidate,votes in result:
    print (candidate,'with', str(votes) , 'votes')