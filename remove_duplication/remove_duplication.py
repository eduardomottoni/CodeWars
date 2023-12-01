# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 10:19:05 2023

@author: eotoni
"""

def unique_in_order(sequence):
    filtered_sequence = sequence[:1]
    for item in sequence:
        if item != filtered_sequence[-1]:
            filtered_sequence.append(item)
    return filtered_sequence


unique_in_order(["A"])