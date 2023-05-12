"""11-dars Tarmoqlanish if va else
"""
 
mahsulotlar=["olma","anor","banan","pomidor","tarvuz","qovun","bodiring","gilos","nok","apelsin"]
savat=[]
for n in range(5):
    savat.append(input(f"{n+1}-mahsulotni tanlang: "))
bor_mahsulot=[]
mavjud_emas=[]
for mah in savat:
    if mah in mahsulotlar:
        bor_mahsulot.append(mah)
    else:
        mavjud_emas.append(mah)
if mavjud_emas:
   print("Do'konimizda quyidagi mahsulotlar yo'q:")
   for mah in mavjud_emas: 
        print(mah)
else:
    print("Do'konimizda siz so'ragan barcha mahsulot bor")
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        