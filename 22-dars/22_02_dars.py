# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 12:06:56 2023

@author: user
"""

def talaba_info(ism,familiya,**malumotlar):
    malumotlar['ism']=ism
    malumotlar['familiya']=familiya
    return malumotlar
print(talaba_info('ali', 'valiyev', yosh=20,manzili='qarshi',kurs=3))