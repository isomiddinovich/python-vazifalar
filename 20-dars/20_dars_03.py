# -*- coding: utf-8 -*-
"""
Created on Sat Jun  3 11:34:05 2023

@author: user
"""
def son_taqqosla(x,y,z):
    """Sonning kattasini taqqoslaydi"""
    son=x
    if son<y:
        son=y
    else:
        son=z
    print(son)
son_taqqosla(9,8,11)