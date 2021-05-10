# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 18:27:48 2020

@author: robyb
"""

def print_queue(*personList,**patientDict):
    for person in personList:
        notFound=True
        for patient,info in patientDict.items():
            if person==patient:
                notFound=False
                print(patient+':')
                for key,value in info.items():
                    print('{}={}'.format(key,value))
                print()     
        if notFound:
            print(person,'is not a patient')
                

queue_list = ['Nelson','Tiffany','Raymond','Michelle','Polly']
patient_dict ={'Tiffany':{'age':15,'weight':50},
               'Raymond':{'age':25,'weight':40},
               'Michelle':{'age':35,'weight':30},
               'Sabrina':{'age':45,'weight':20},
                }
print('These waiting people are on the record.')
print_queue(*queue_list,**patient_dict)