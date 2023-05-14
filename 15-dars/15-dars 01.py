"""
15-dars lug'at bilan amallar
"""
countruys={'aqsh':'washington','angliya':'london','germaniya':'berlin',
           'italiya':'rim','eron':'tehron','qozoqiston':'ostona',
           "o'zbekiston":'toshkent','yaponiya':'tokio','rossiya':'moskva'}
print("Dunyo mamlakatlari:")
for n in sorted(countruys.keys()):
    print(n.upper())
print("\nDavlatlar poytaxtlari:")
for poytaxt in sorted(countruys.values()):
    print(poytaxt.title())
user=input("Istalgan davlatni kiriting: ").lower()
capital=countruys.get(user)
if capital==None:
    print("Kechirasiz bizda bu haqida ma'lumot yo'q!")
else:
    print(f"{user.upper()} davlatining poytaxti {capital.title()} shahri")
 