
buxoriy = {
    "ism": "Abu Abdulloh Muhammad ibn Ismoil",
    "tyil": 810,
    "vyil": 870,
    "tjoy": "Buxoro",
    'asarlar':['Al-jome as-sahih','Al-Adab al-murfad',
               'At-tarix al-kabir','At-tarix as-sag\'ir']
}

qodiriy = {"ism": "Abdulla Qodiriy", 
           "tyil": 1894,
           "vyil": 1938,
           "tjoy": "Toshkent",
           'asarlar':["O'tgan kunlar","mehrobdam chayon",
                      "Obid ketmon"]}

vohidov = {"ism": "Erkin Vohidov", "tyil": 1936, "vyil": 2016, 
           "tjoy": "Farg'ona",
           "asarlar":["O'zbegim","Qiziquvcha Matmusa",
                      "Tong nafasi","Qo'shiqlarim sizga"]}

navoiy = {"ism": "Alisher Navoiy", "tyil": 1441, "vyil": 1501,
          "tjoy": "Xirot",
          "asarlar":["Xamsa","Lison ut-tayir",
                     "Mahbub ul qulub","Munojot"]}

shaxslar = [buxoriy, qodiriy, vohidov, navoiy]
for shaxs in shaxslar:
     ism=shaxs['ism']
     asarlar=shaxs['asarlar']
     print(f"{ism} ning mashhur asarlari:")
     for asar in asarlar:
         print(asar)








