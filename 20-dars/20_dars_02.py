# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 16:31:07 2023

@author: user
"""

def user_info(ism,familiya,manzil,tyil,email='',tel=None):
    user={'ism':ism,
          'familiya':familiya,
          'manzil':manzil,
          'yosh':2023-tyil,
          'email':email,
          'tel':tel
          }
    return user
users=[]
while True:
    ism=input("Ismingiz: ")
    familiya=input("Familiyangiz: ")
    manzil=input("Yashash manzili : ")
    tyil=int(input("Tug'ulgan yili: "))    
    email=input("Email: ")
    tel=input("Telefon raqami: ")
    javob=input("Yana qo'shasizmi ? (yes/no) : ")
    users.append(user_info(ism, familiya, manzil, tyil,email,tel))
    if javob=='no':
        break
print("Foydalanuvchilar :")
for user in users:
    print(f"{user['ism'].title()} {user['familiya'].title()}"
          f"{user['yosh']} yoshda, {user['manzil'].title()} shahrida yashaydi"
          f"\nTelefon raqami: {user['tel']}")
    