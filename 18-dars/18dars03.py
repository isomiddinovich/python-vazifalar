# -*- coding: utf-8 -*-
"""
Created on Fri May 26 19:04:21 2023

@author: user
"""

e_bozor={'olma': 5000,
         'anor': 6000, 
         'mandarin': 14000,
         'non': 5000,
         'nok': 20000, 
         'uzum': 30000, 
         'qulupnay': 35000,
         'banan': 17000,
         'pomidor': 10000}
savat=[]
while True:
    mahsulot=input("Mahsulotni kiriting: ")
    savat.append(mahsulot)
    javob=input("Davom etasizmi(ha/yoq)")
    if javob!='ha':
        break
# while savat:
#     if savat in e_bozor.keys():
#         narh=e_bozor[savat]
#         print(f"{savat}ninig narhi {narh} so'm")
summa=[]
# for mahsulot in savat:
#     if mahsulot in e_bozor.keys():
#         narh=e_bozor[mahsulot]
#         summa.append(narh)
#         print(f"{mahsulot.title()} ning narhi {narh} so'm")
#     else:
#         print(f"Bizda {mahsulot.title()} yo'q")
# print(f"Jami {sum(summa)} so'm")
while savat:
    mahsulot=savat.pop()
    if mahsulot in e_bozor.keys():
        narh=e_bozor[mahsulot]
        print(f"{mahsulot.title()} ninig narhi {narh} so'm")
        summa.append(narh)
    else:
        print(f"Bizda {mahsulot.title()} yo'q")

print(f"Bizda bor mahsulotlar jami {sum(summa)} so'm")



















