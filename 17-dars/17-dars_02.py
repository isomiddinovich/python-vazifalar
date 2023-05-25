# print("Muzeyga kirish menyusi:")
# savol='Yoshingizni kiriting\n'
# savol+="To'xtatish uchun 'exit' yoki 'quit' deb yozing : "
# while True:
#     yosh=input(savol)
#     if yosh=='exit' or yosh=='quit':
#         break
#     yosh=int(yosh)
#     if yosh<=7:
#         narx=2000
#     elif 7<yosh<18:
#         narx=3000
#     elif 18<=yosh<=64:
#         narx=4000
#     if yosh>=65:
#         print("Sizga kirish tekin")
#     else:
#         print(f"Sizga kirish {narx} so'm")
# print("Xush kelibsiz")
print("Muzeyga kirish menyusi:")
savol='Yoshingizni kiriting\n'
savol+="To'xtatish uchun 'exit' yoki 'quit' deb yozing : "
ishora=True
while ishora:
    yosh=input(savol)
    if yosh=='exit' or yosh=='quit':
        ishora=False
    
    # yosh=int(yosh)
    if int(yosh)<=7:
        narx=2000
    elif 7<int(yosh)<18:
        narx=3000
    elif 18<=int(yosh)<=64:
        narx=4000
    if int(yosh)>=65:
        print("Sizga kirish tekin")
    else:
        print(f"Sizga kirish {narx} so'm")
print("Xush kelibsiz")
























