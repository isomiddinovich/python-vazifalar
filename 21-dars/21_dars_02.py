# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 11:33:29 2023

@author: user
"""

def kattaharf(matnlar):
    matnlar=matnlar[:]
    for ism in range(len(matnlar)):
        matnlar[ism]=matnlar[ism].title()
    return matnlar
        
ismlar=['ali','vali','hasan','husan']
matn=kattaharf(ismlar)
print(matn)
print(ismlar)