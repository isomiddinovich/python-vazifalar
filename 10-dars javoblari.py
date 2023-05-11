"""10-dars Tarmoqlanish if va else
"""
cars=["toyotta","mazda","hyundai","gm","kia"]
for avto in cars:
    if avto=="gm":
       print(avto.upper())
    else:
       print(avto.title())
for avto in cars:
    if avto!="gm":
        print(avto.title())
    else:
        print(avto.upper())
ism=input("Ismingizni kiriting: ")
admin="anvar"
if ism.lower()==admin:
    print("Salom admin foydalanuvchilar ro'yxatini ko'rasizmi")
else:
    print("Xush kelibsiz ",ism.title())
x=float(input("Birinchi sonni tanlang: "))
y=float(input("Ikkinchi sonni tanlang: "))
if x==y:
    print("Sonlar teng ekan!")
#son=float(input("Istalgan sonni kiriting: "))
#if son<0:
#    print("Manfiy son!")
#else:
 #   print("Musbat son!")
son=float(input("Istalgan sonni kiriting: "))
if  son>=0:
     print(son**0.5)
else:
     print("Musbat son kiriting")