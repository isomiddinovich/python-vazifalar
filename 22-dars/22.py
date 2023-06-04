# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 12:01:13 2023

@author: user
"""

def kupaytma(*sonlar):
    qiymat=1
    for son in sonlar:
        qiymat*=son
    return qiymat
print(kupaytma(1,3,5))










