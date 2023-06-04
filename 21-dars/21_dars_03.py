# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 11:37:05 2023

@author: user
"""

def bahola(ismlar):
    baholar = {}
    for ism in ismlar:
        baho=int(input(f"Talaba {ism.title()} ning bahosini kiritng : "))
        baholar[ism]=baho
    return baholar

talabalar = ['ali', 'vali', 'hasan', 'husan']
baholar = bahola(talabalar)
print(baholar)