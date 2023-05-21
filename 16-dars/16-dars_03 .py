countrys={"o'zbekisto":{"poytaxti":"Toshkent",
                        'hududi':443978,
                        "aholi":33000000,
                        'valyuta':"so'm"},
          "aqsh":{"poytaxti":"Washington",
                  "hududi":9631418,
                  "aholi":327000000,
                  "valyuta":"dollar"},
          "rossiya":{"poytaxti":"Moskva",
                     "hududi":17098246,
                     "aholi":144000000,
                     "valyuta":"rubl"},
          "malayziya":{"poytaxti":"Kuala-Lumpur",
                       "hududi":329750,
                       "aholi":25000000,
                       "valyuta":"ringit"}
         }
for dav,info in countrys.items():
    print(f"\n {dav.capitalize()} ning poytaxti {info['poytaxti']}"
          f"\n Hududi: {info['hududi']}kv.km"
          f"\n Aholisi: {info['aholi']}"
          f"\n Pul birligi: {info['valyuta']}")
                        