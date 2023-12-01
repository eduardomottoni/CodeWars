# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 11:04:28 2023

@author: eotoni
"""

def row_sum_odd_numbers(n):
    odd_num = list(range(1, 1+n**3, 2))
    row = 1
    item = 0
    while row < n:
        item += row
        row += 1
    result = sum(odd_num[item:item+n])
    return result
    
n = row_sum_odd_numbers(20)
