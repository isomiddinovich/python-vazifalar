"""11-dars Tarmoqlanish if va else
"""
 
mahsulotlar=["olma","anor","banan","pomidor","tarvuz","qovun","bodiring","gilos","nok","apelsin"]
savat=[]
for n in range(5):
    savat.append(input(f"{n+1}-mahsulotni tanlang: "))
for mahsulot in savat:
    if mahsulot in mahsulotlar:
        print(f"Do'konimizda {mahsulot} bor")
    else:
        print(f"Do'konimizda {mahsulot} yo'q")
        
        
        
        
        
        
        
        
        
        
        
        
        
        