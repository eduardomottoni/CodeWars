# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 10:44:15 2023

@author: eotoni
"""
from itertools  import groupby
def xo(s):
    s = s.lower()
    list_s = sorted(list(s))
    dic_list = {key: len(list(group)) for key, group in groupby(list_s)}
    
    if "o" in dic_list and "x" in dic_list:
        return dic_list["o"] == dic_list["x"]
    if "o" not in dic_list and "x" not in dic_list:
        return True
    return False
        
xo("")