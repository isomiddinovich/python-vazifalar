# -*- coding: utf-8 -*-
"""
Created on Sat Jun  3 11:39:46 2023

@author: user
"""

def aylana_hisobla(r, pi=3.14159):
    """aylana o'lchamlarini hisoblaydi"""
   
    aylana={'radiusi':r,
            'diamentri':r*2,
            'peremetr':pi*(r*2),
            'yuzi':pi*(r**2)
        }
    return aylana
aylana_hisobla(4)