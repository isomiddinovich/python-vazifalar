"""
15-dars lug'at bilan amallar
"""
menu={'osh':18000,
      'mastava':15000,
      "sho'rva":16000,
      "tandir go'sht":1300000,
      "lag'mon":14000,
      'bifshteks':17000,
      'jiz':100000,
      'shashlik':45000,
      'manti':5000}
zakaz=[]
print("3ta taomga buyurtma bering")
for n in range(3):
    zakaz.append(input(f"{n+1}-taom:").lower())
for buyurtma in zakaz:
    if buyurtma in menu:
        print(f"{buyurtma.title()} {menu[buyurtma]} so'm")
    else:
        print(f"Kechirasiz bizda {buyurtma} yo'q")