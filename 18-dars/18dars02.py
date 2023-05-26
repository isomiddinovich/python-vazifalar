# -*- coding: utf-8 -*-
"""
Created on Fri May 26 18:56:23 2023

@author: user
"""
e_bozor={}
ishora=True
while ishora:
    mahsulot=input("Mahsulotni kriting: ")
    narh=input(f"{mahsulot.title()} ning narhini kiriting: ")
    e_bozor[mahsulot]=int(narh)
    javob=input("Davom etasizmi(ha/yo'q): ")
    if javob!='ha':
        ishora=False
print("Ro'yxat shakllandi!")