# -*- coding: utf-8 -*-
"""
Created on Sun May 14 06:27:55 2023

@author: user
"""
py_syntaxs={'integer':'butun son',
          'float':"o'nlik son",
          'string':'matn',
          'boolean':'mantiqiy',
          'list':"ro'yxat",
          'dictionary':"lug'at",
          'for':'aylanma sikl',
          'if':'agar',
          'elif':"bo'lmasa agar",
          'else':"bo'lmasa"
          }
for k,q in sorted(py_syntaxs.items()):
    print(f"{k.title()}-{q.title()}")