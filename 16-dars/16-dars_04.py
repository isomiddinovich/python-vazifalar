#kinolar = {
#   "ali": ["Terminator", "Rambo", "Titanic"],
#    "vali": ["Tenet", "Inception", "Interstellar"],
#    "hasan": ["Abdullajon", "Bomba", "Shaytanat"],
#    "husan": ["Mahallada duv-duv gap", "John Wick"]
#           }
#for ism,kino in kinolar.items():
#    print(f" \n{ism.title()} ning sevimli kinolari:")
#    for film in kino:
#        print(film)
    


# buxoriy = {
#     "ism": "Abu Abdulloh Muhammad ibn Ismoil",
#     "tyil": 810,
#     "vyil": 870,
#     "tjoy": "Buxoro",
#     "asarlar": [
#         "Al-jome’ as-sahih",
#         "Al-adab al-mufrad",
#         "At-tarix al-kabir",
#         "At-tarix as-sag‘ir",
#     ],
# }

# qodiriy = {
#     "ism": "Abdulla Qodiriy",
#     "tyil": 1894,
#     "vyil": 1938,
#     "tjoy": "Toshkent",
#     "asarlar": ["O'tkan kunlar", "Mehrobdan Chayon", "Obid ketmon"],
# }

# vohidov = {
#     "ism": "Erkin Vohidov",
#     "tyil": 1936,
#     "vyil": 2016,
#     "tjoy": "Farg'ona",
#     "asarlar": ["Tong nafasi", "Qo'shiqlarim sizga", "O'zbegim", "Qiziquvchan Matmusa"],
# }

# navoiy = {
#     "ism": "Alisher Navoiy",
#     "tyil": 1441,
#     "vyil": 1501,
#     "tjoy": "Xirot",
#     "asarlar": ["Xamsa", "Lison ut-Tayr", "Mahbub Al-Qulub", "Munojot"],
# }

# shaxslar = [buxoriy, qodiriy, vohidov, navoiy]
 
davlatlar={"o'zbekiston":{'poytaxti':'toshkent',
                          'hududi':448978,
                          'aholi':35000000,
                          'valyuta':"so'm"
                           },
           'aqsh':{'poytaxti':'washington',
                   'hududi':6433959,
                   'aholi':327000000,
                   'valyuta':'dollar'},
           'rossiya':{'poytaxti':'moskva',
                      'hududi':17028408,
                      'aholi':144000000,
                      'valyuta':'rubl'},
           
           'malayziya':{'poytaxti':'kuala lumpur',
                        'hududi':329332,
                        'aholi':27000000,
                        'valyuta':'ringit'}
           }    
# for davlat,info in davlatlar.items():
#     poytaxt=info['poytaxti']
#     hudud=info['hududi']
#     aholi=info['aholi']
#     valyuta=info['valyuta']
#     if davlat.lower()=='aqsh':
#         davlat=davlat.upper()
#     else:
#         davlat=davlat.capitalize()
#     print(f"\n{davlat} ning poytaxti {poytaxt.title()} shahri"
#           f"\nHududi : {hudud} kv.km"
#           f"\nAholisi : {aholi}"
#           f"\nPul birligi : {valyuta}")
user=input('Davlat nomini kiriting: ').lower()
# davlat=davlatlar.get(user)
# if user=='aqsh':
#     user=user.upper()
# else:
#     user=user.capitalize()

# if davlat!=None:
#     print(f"\n{user} ning poytaxti {davlat['poytaxti'].title()}"
#           f"\nHududi : {davlat['hududi']} kv.km"
#           f"\nAholisi : {davlat['aholi']}"
#           f"\nPul birligi : {davlat['valyuta']}")

# else:
#     print("Kechirasiz bizda bu haqida ma'lumot yo'q")

if user in davlatlar:
    info=davlatlar[user]
    if user=='aqsh':
        user=user.upper()
    else:
        user=user.capitalize()
    print(f"\n{user}ning poytaxti {info['poytaxti'].title()} shahri"
          f"\nHududi : {info['hududi']}kv.km"
          f"\nAholisi : {info['aholi']}"
          f"\nPul birligi : {info['valyuta']}")
else:
    print("Kechirasiz bizda bunaqa ma'lumot yo'q")








    
    
    
    