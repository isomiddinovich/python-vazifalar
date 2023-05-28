# -*- coding: utf-8 -*-
"""
Created on Sun May 28 09:55:10 2023

@author: user
"""

def hisobla(son):
    """Sonni qoldiqsiz bo'linishini tekshiradi"""
    for n in range(2,11):
        if son%n==0:
            print(f"{son} {n}ga qoldiqsiz bo'linadi")
            
hisobla(25)