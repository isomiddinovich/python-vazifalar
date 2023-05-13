# -*- coding: utf-8 -*-
"""
Created on Sat May 13 10:24:31 2023
14-dars dictionary(lug'at')

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
key=input("Kalit so'zni koiriting: ").lower()
kalit=py_syntaxs.get(key)
if kalit==None:
    print("Bunday so'z mavjud emas!")
else:
    print(f"{key} so'zining ma'nosi {kalit} deb tarjima qilinadi")