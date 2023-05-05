# -*- coding: utf-8 -*-
"""
Created on Thu May  4 17:53:40 2023

@author: User
"""

#mahsulotlar=["olma","uzum","non","sut","tuxum","go'sht","saryog'","tuz","gugurt","choy"]
#savat=[]
##xarid=savat.append(input("Ikkinchi mahsulotni kiriting:\n>>> "))
#xarid=savat.append(input("Uchinchi mahsulotni kiriting:\n>>> "))
#xarid=savat.append(input("To'rtinchi mahsulotni kiriting:\n>>> "))
#xarid=savat.append(input("Beshinchi mahsulotni kiriting:\n>>> "))

#bor_mahsulotlar=[]
#mavjud_emas=[]
#if savat:
#  for xarid in savat:
 #   if xarid.lower() in mahsulotlar:
#      bor_mahsulotlar.append(xarid)
 #   else:
#      mavjud_emas.append(xarid)
#if len(mavjud_emas)==0:      
 #  print(f"Do'konimizda siz so'ragan hamma mahsulot mavjud!")
#else:
#   print(f"Do'konimizda quyidagi mahsulotlar yo'q:\n {mavjud_emas}") 

#users=["anvar","nurbek","jasur","ixtiyor","nodir"]
#login=input("Yangi login kiriting: ")
#if not login.lower() in users:
   # print(f"Xush kelibsiz, {login.title()}")
#else: 
 #   ism=input("Login band, boshqasini tanlang: ")
  #  print(f"Xush kelibsiz, {ism.title()} !")
  
son=float(input("Butun sonni kiriting: "))
a=son%2
a=son%4
a=son%6
a=son%8
if a==0:
    print(f"{son} soni 2 ga qoldiqsiz bo'linadi ")
    print(f"{son} soni 4 ga qoldiqsiz bo'linadi ")
    print(f"{son} soni 6 ga qoldiqsiz bo'linadi ")
    print(f"{son} soni 8 ga qoldiqsiz bo'linadi ")