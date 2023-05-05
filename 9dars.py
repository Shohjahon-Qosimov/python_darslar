# -*- coding: utf-8 -*-
"""
Created on Wed May  3 11:17:56 2023

@author: Shohjahon Qosimov
"""

#ismlar=["Anvar","Nurbek","Jasur","Javlon","Ixtiyor"]
#ismlar.append('Diyor')
#for m in ismlar:
   # print(f"Qalesan {m}, ishlaring yaxshimi?")
#print(f"Kod {len(ismlar)} marta takrorlandi")

#sonlar=list(range(11,100,2))
#for kub in sonlar:
  # print(kub**3)
  
#sevimli_kinolar=[]
#print("5 ta eng sevimli kinoyingizni kiriting:")
#for n in range(1,6):
   # sevimli_kinolar.append(input(f"{n}-chi kinoyingizni kiriting:"))

#print(sevimli_kinolar.upper(0,6))
odamlar=[]

print(input(f"Bugun nechta odam gaplashdingiz?\n>>> "))
for n in range(1,4):
    odamlar.append(input(f"{n}-chi odamning ismi nima? "))
print(odamlar)