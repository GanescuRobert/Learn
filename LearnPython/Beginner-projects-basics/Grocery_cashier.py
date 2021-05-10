# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 18:45:15 2020

@author: robyb
"""


def get_total_price(buying_dict,price_dict):
    bill=0
    for key,value in buying_dict.items():
        print('{}x{}={}$'.format(value,key,value*price_dict[key]))
        bill += value*price_dict[key]
    return bill
def get_discount(bill_price,membership,membership_dict):
    return round(bill_price*(membership_dict[membership]/100),2) 
    
    
buying_dict = {'biscuit': 2,'chicken': 3,'egg': 20}
price_dict = {'biscuit':2, 'fish':3,'chicken':5,'cabbage':2,'egg':0.2} 
membership_dict = {'diamond':30,'gold':20,'silver':10,'bronze':5}
bill_price = 0
discount = 0
bill_price = get_total_price(buying_dict,price_dict)
print('Total without discount is: $',bill_price)

membership = 'diamond'
discount = get_discount(bill_price,membership,membership_dict)

print('Total with discount is: $',bill_price-discount)
print('Saved moneys',discount)